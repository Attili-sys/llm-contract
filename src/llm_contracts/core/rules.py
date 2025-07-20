"""Content linting and validation rules."""

import re
from typing import Any, Dict, List, Union, Optional


class RuleError(Exception):
    """Raised when there's an error in rule validation."""
    
    def __init__(self, message: str, rule_name: Optional[str] = None):
        super().__init__(message)
        self.message = message
        self.rule_name = rule_name


def validate_rules(
    content: Union[str, Dict[str, Any]], 
    rules: List[Dict[str, Any]]
) -> List[str]:
    """
    Validate content against a list of rules.
    
    Args:
        content: Content to validate (string or dict)
        rules: List of rule dictionaries
        
    Returns:
        List of validation error messages
    """
    errors: List[str] = []
    
    # Convert content to string for text-based rules
    if isinstance(content, dict):
        content_str = str(content)
    else:
        content_str = str(content)
    
    for rule in rules:
        rule_errors = _validate_single_rule(content_str, rule)
        errors.extend(rule_errors)
    
    return errors


def _validate_single_rule(
    content: str, 
    rule: Dict[str, Any]
) -> List[str]:
    """
    Validate content against a single rule.
    
    Args:
        content: Content string to validate
        rule: Rule dictionary
        
    Returns:
        List of validation error messages
    """
    errors: List[str] = []
    
    for rule_type, rule_value in rule.items():
        try:
            if rule_type == "keyword_must_include":
                if isinstance(rule_value, str):
                    if rule_value.lower() not in content.lower():
                        errors.append(f"Must include keyword: '{rule_value}'")
                elif isinstance(rule_value, list):
                    for keyword in rule_value:
                        if keyword.lower() not in content.lower():
                            errors.append(f"Must include keyword: '{keyword}'")
            
            elif rule_type == "keyword_must_not_include":
                if isinstance(rule_value, str):
                    if rule_value.lower() in content.lower():
                        errors.append(f"Must not include keyword: '{rule_value}'")
                elif isinstance(rule_value, list):
                    for keyword in rule_value:
                        if keyword.lower() in content.lower():
                            errors.append(f"Must not include keyword: '{keyword}'")
            
            elif rule_type == "no_placeholder_text":
                pattern = re.compile(rule_value, re.IGNORECASE)
                if pattern.search(content):
                    errors.append(f"Contains placeholder text: '{rule_value}'")
            
            elif rule_type == "word_count_min":
                word_count = len(content.split())
                if word_count < rule_value:
                    errors.append(f"Word count ({word_count}) below minimum ({rule_value})")
            
            elif rule_type == "word_count_max":
                word_count = len(content.split())
                if word_count > rule_value:
                    errors.append(f"Word count ({word_count}) above maximum ({rule_value})")
            
            elif rule_type == "phrase_proximity":
                if isinstance(rule_value, dict):
                    terms = rule_value.get("terms", [])
                    max_distance = rule_value.get("max_distance", 10)
                    
                    if len(terms) >= 2:
                        proximity_errors = _check_phrase_proximity(
                            content, terms, max_distance
                        )
                        errors.extend(proximity_errors)
            
            elif rule_type == "phrase_order":
                if isinstance(rule_value, dict):
                    first_phrase = rule_value.get("first", "")
                    then_phrase = rule_value.get("then", "")
                    
                    if first_phrase and then_phrase:
                        order_errors = _check_phrase_order(content, first_phrase, then_phrase)
                        errors.extend(order_errors)
            
            elif rule_type == "section_must_start_with":
                pattern = re.compile(rule_value, re.IGNORECASE)
                if not pattern.match(content.strip()):
                    errors.append(f"Content must start with pattern: '{rule_value}'")
            
            elif rule_type == "list_item_pattern":
                pattern = re.compile(rule_value)
                lines = content.splitlines()
                for i, line in enumerate(lines):
                    if line.strip().startswith("-") or line.strip().startswith("*"):
                        continue  # skip unordered lists
                    if re.match(r"^\d+\.", line.strip()):
                        if not pattern.match(line.strip()):
                            errors.append(f"Line {i+1} does not match list item pattern: '{rule_value}'")
            
            # New advanced rules
            elif rule_type == "regex_must_match":
                pattern = re.compile(rule_value, re.IGNORECASE)
                if not pattern.search(content):
                    errors.append(f"Content must match regex pattern: '{rule_value}'")
            
            elif rule_type == "no_duplicate_sentences":
                sentences = re.split(r'[.!?]+', content)
                sentences = [s.strip() for s in sentences if s.strip()]
                
                seen_sentences = set()
                duplicates = []
                
                for sentence in sentences:
                    sentence_lower = sentence.lower()
                    if sentence_lower in seen_sentences:
                        duplicates.append(sentence)
                    else:
                        seen_sentences.add(sentence_lower)
                
                if duplicates:
                    errors.append(f"Duplicate sentences found: {len(duplicates)} instances")
            
            elif rule_type == "min_list_items":
                # Count list items (bullet points, numbered lists)
                list_pattern = re.compile(r'^[\s]*[•\-\*]\s|^[\s]*\d+\.\s', re.MULTILINE)
                list_items = list_pattern.findall(content)
                
                if len(list_items) < rule_value:
                    errors.append(f"Must have at least {rule_value} list items, found {len(list_items)}")
            
            elif rule_type == "max_passive_voice_ratio":
                # Simple passive voice detection
                passive_patterns = [
                    r'\b(am|is|are|was|were|be|been|being)\s+\w+ed\b',
                    r'\b(am|is|are|was|were|be|been|being)\s+\w+en\b',
                    r'\b(am|is|are|was|were|be|been|being)\s+\w+ing\b'
                ]
                
                total_sentences = len(re.split(r'[.!?]+', content))
                passive_sentences = 0
                
                for pattern in passive_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    passive_sentences += len(matches)
                
                if total_sentences > 0:
                    passive_ratio = passive_sentences / total_sentences
                    if passive_ratio > rule_value:
                        errors.append(f"Passive voice ratio ({passive_ratio:.2f}) exceeds maximum ({rule_value})")
            
            else:
                errors.append(f"Unknown rule type: '{rule_type}'")
                
        except Exception as e:
            errors.append(f"Error applying rule '{rule_type}': {str(e)}")
    
    return errors


def _check_phrase_proximity(
    content: str, 
    terms: List[str], 
    max_distance: int
) -> List[str]:
    """
    Check if terms appear within the specified distance of each other.
    
    Args:
        content: Content to check
        terms: List of terms to find
        max_distance: Maximum word distance between terms
        
    Returns:
        List of proximity error messages
    """
    errors: List[str] = []
    
    if len(terms) < 2:
        return errors
    
    words = content.lower().split()
    term_positions = {}
    
    # Find positions of all terms
    for i, word in enumerate(words):
        for term in terms:
            if term.lower() in word:
                if term not in term_positions:
                    term_positions[term] = []
                term_positions[term].append(i)
    
    # Check if all terms are found
    missing_terms = [term for term in terms if term not in term_positions]
    if missing_terms:
        errors.append(f"Missing terms: {', '.join(missing_terms)}")
        return errors
    
    # Check proximity between all pairs of terms
    for i in range(len(terms)):
        for j in range(i + 1, len(terms)):
            term1, term2 = terms[i], terms[j]
            
            found_proximity = False
            for pos1 in term_positions[term1]:
                for pos2 in term_positions[term2]:
                    if abs(pos1 - pos2) <= max_distance:
                        found_proximity = True
                        break
                if found_proximity:
                    break
            
            if not found_proximity:
                errors.append(
                    f"Terms '{term1}' and '{term2}' must be within "
                    f"{max_distance} words of each other"
                )
    
    return errors


def _check_phrase_order(
    content: str, 
    first_phrase: str, 
    then_phrase: str
) -> List[str]:
    """
    Check if first_phrase appears before then_phrase.
    
    Args:
        content: Content to check
        first_phrase: Phrase that should appear first
        then_phrase: Phrase that should appear after
        
    Returns:
        List of order error messages
    """
    errors: List[str] = []
    
    content_lower = content.lower()
    first_pos = content_lower.find(first_phrase.lower())
    then_pos = content_lower.find(then_phrase.lower())
    
    if first_pos == -1:
        errors.append(f"Missing required phrase: '{first_phrase}'")
    elif then_pos == -1:
        errors.append(f"Missing required phrase: '{then_phrase}'")
    elif first_pos > then_pos:
        errors.append(
            f"Phrase '{first_phrase}' must appear before '{then_phrase}'"
        )
    
    return errors 