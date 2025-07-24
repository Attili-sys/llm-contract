/**
 * Schema Builder for LLM Contracts Validator
 */

class SchemaBuilder {
    constructor() {
        this.schema = {
            schema: {},
            rules: []
        };
        this.fieldCounter = 0;
        this.ruleCounter = 0;
    }

    /**
     * Initialize the schema builder UI
     */
    init() {
        // Add field button
        document.getElementById('addSchemaField').addEventListener('click', () => {
            this.showAddFieldModal();
        });

        // Add rule button
        document.getElementById('addRule').addEventListener('click', () => {
            this.showAddRuleModal();
        });

        // Save field button
        document.getElementById('saveField').addEventListener('click', () => {
            this.addFieldFromModal();
        });

        // Save rule button
        document.getElementById('saveRule').addEventListener('click', () => {
            this.addRuleFromModal();
        });

        // Field type change event
        document.getElementById('fieldType').addEventListener('change', (e) => {
            this.toggleFieldOptions(e.target.value);
        });

        // Rule type change event
        document.getElementById('ruleType').addEventListener('change', (e) => {
            this.updateRuleValueUI(e.target.value);
        });

        // Load schema button
        document.getElementById('loadSchemaBtn').addEventListener('click', () => {
            this.loadSchemaFromFile();
        });

        // Save schema button
        document.getElementById('saveSchemaBtn').addEventListener('click', () => {
            this.saveSchemaToFile();
        });

        // Generate schema from description
        document.getElementById('generateSchema').addEventListener('click', () => {
            this.generateSchemaFromDescription();
        });

        // YAML editor changes
        document.getElementById('yamlEditor').addEventListener('input', (e) => {
            this.updateSchemaFromYaml(e.target.value);
        });

        // Template selection
        document.querySelectorAll('[data-template]').forEach(button => {
            button.addEventListener('click', (e) => {
                const templateName = e.target.closest('[data-template]').getAttribute('data-template');
                this.loadTemplate(templateName);
            });
        });

        // Initialize with empty schema
        this.updateYamlFromSchema();
    }

    /**
     * Show the add field modal
     */
    showAddFieldModal() {
        // Reset form
        document.getElementById('fieldName').value = '';
        document.getElementById('fieldType').value = 'str';
        document.getElementById('fieldRequired').checked = false;
        document.getElementById('minLength').value = '';
        document.getElementById('maxLength').value = '';
        document.getElementById('pattern').value = '';
        document.getElementById('minValue').value = '';
        document.getElementById('maxValue').value = '';
        document.getElementById('minItems').value = '';
        document.getElementById('maxItems').value = '';

        // Show string options by default
        this.toggleFieldOptions('str');

        // Show modal
        const modal = new bootstrap.Modal(document.getElementById('addFieldModal'));
        modal.show();
    }

    /**
     * Show the add rule modal
     */
    showAddRuleModal() {
        // Reset form
        document.getElementById('ruleType').value = 'keyword_must_include';
        
        // Update rule value UI
        this.updateRuleValueUI('keyword_must_include');

        // Show modal
        const modal = new bootstrap.Modal(document.getElementById('addRuleModal'));
        modal.show();
    }

    /**
     * Toggle field options based on field type
     * @param {string} fieldType - Type of the field
     */
    toggleFieldOptions(fieldType) {
        const stringOptions = document.getElementById('stringOptions');
        const numberOptions = document.getElementById('numberOptions');
        const listOptions = document.getElementById('listOptions');

        // Hide all options first
        stringOptions.classList.add('d-none');
        numberOptions.classList.add('d-none');
        listOptions.classList.add('d-none');

        // Show relevant options based on field type
        if (fieldType === 'str') {
            stringOptions.classList.remove('d-none');
        } else if (fieldType === 'int' || fieldType === 'float') {
            numberOptions.classList.remove('d-none');
        } else if (fieldType === 'list') {
            listOptions.classList.remove('d-none');
        }
    }

    /**
     * Update rule value UI based on rule type
     * @param {string} ruleType - Type of the rule
     */
    updateRuleValueUI(ruleType) {
        const container = document.getElementById('ruleValueContainer');
        container.innerHTML = '';

        switch (ruleType) {
            case 'keyword_must_include':
            case 'keyword_must_not_include':
                container.innerHTML = `
                    <label class="form-label">Keywords (comma-separated)</label>
                    <input type="text" class="form-control" id="ruleValue" placeholder="quality, premium, durable">
                `;
                break;
            
            case 'no_placeholder_text':
            case 'regex_must_match':
                container.innerHTML = `
                    <label class="form-label">Pattern (regex)</label>
                    <input type="text" class="form-control" id="ruleValue" placeholder="\\[YOUR_TEXT_HERE\\]">
                `;
                break;
            
            case 'word_count_min':
            case 'word_count_max':
            case 'min_list_items':
                container.innerHTML = `
                    <label class="form-label">Value</label>
                    <input type="number" class="form-control" id="ruleValue" min="1" placeholder="100">
                `;
                break;
            
            case 'max_passive_voice_ratio':
                container.innerHTML = `
                    <label class="form-label">Ratio (0-1)</label>
                    <input type="number" class="form-control" id="ruleValue" min="0" max="1" step="0.1" placeholder="0.3">
                `;
                break;
            
            case 'no_duplicate_sentences':
                container.innerHTML = `
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="ruleValue" checked>
                        <label class="form-check-label" for="ruleValue">
                            Enable duplicate sentence detection
                        </label>
                    </div>
                `;
                break;
            
            case 'phrase_proximity':
                container.innerHTML = `
                    <div class="mb-3">
                        <label class="form-label">Terms (comma-separated)</label>
                        <input type="text" class="form-control" id="proximityTerms" placeholder="warranty, 30">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Max Distance (words)</label>
                        <input type="number" class="form-control" id="proximityDistance" min="1" placeholder="20">
                    </div>
                `;
                break;
            
            case 'phrase_order':
                container.innerHTML = `
                    <div class="mb-3">
                        <label class="form-label">First Phrase</label>
                        <input type="text" class="form-control" id="phraseFirst" placeholder="features">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Then Phrase</label>
                        <input type="text" class="form-control" id="phraseThen" placeholder="buy now">
                    </div>
                `;
                break;
        }
    }

    /**
     * Add a field from the modal form
     */
    addFieldFromModal() {
        const fieldName = document.getElementById('fieldName').value.trim();
        const fieldType = document.getElementById('fieldType').value;
        const required = document.getElementById('fieldRequired').checked;

        if (!fieldName) {
            alert('Field name is required');
            return;
        }

        // Create field object
        const field = {
            type: fieldType,
            required: required
        };

        // Add type-specific properties
        if (fieldType === 'str') {
            const minLength = document.getElementById('minLength').value;
            const maxLength = document.getElementById('maxLength').value;
            const pattern = document.getElementById('pattern').value;

            if (minLength) field.min_length = parseInt(minLength);
            if (maxLength) field.max_length = parseInt(maxLength);
            if (pattern) field.pattern = pattern;
        } 
        else if (fieldType === 'int' || fieldType === 'float') {
            const minValue = document.getElementById('minValue').value;
            const maxValue = document.getElementById('maxValue').value;

            if (minValue) field.min = fieldType === 'int' ? parseInt(minValue) : parseFloat(minValue);
            if (maxValue) field.max = fieldType === 'int' ? parseInt(maxValue) : parseFloat(maxValue);
        } 
        else if (fieldType === 'list') {
            const minItems = document.getElementById('minItems').value;
            const maxItems = document.getElementById('maxItems').value;

            if (minItems) field.min_items = parseInt(minItems);
            if (maxItems) field.max_items = parseInt(maxItems);
        }

        // Add to schema
        this.schema.schema[fieldName] = field;

        // Update UI
        this.updateSchemaUI();
        this.updateYamlFromSchema();

        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('addFieldModal')).hide();
    }

    /**
     * Add a rule from the modal form
     */
    addRuleFromModal() {
        const ruleType = document.getElementById('ruleType').value;
        let rule = {};

        switch (ruleType) {
            case 'keyword_must_include':
            case 'keyword_must_not_include':
                const keywords = document.getElementById('ruleValue').value.split(',').map(k => k.trim());
                rule[ruleType] = keywords.length === 1 ? keywords[0] : keywords;
                break;
            
            case 'no_placeholder_text':
            case 'regex_must_match':
                rule[ruleType] = document.getElementById('ruleValue').value;
                break;
            
            case 'word_count_min':
            case 'word_count_max':
            case 'min_list_items':
                rule[ruleType] = parseInt(document.getElementById('ruleValue').value);
                break;
            
            case 'max_passive_voice_ratio':
                rule[ruleType] = parseFloat(document.getElementById('ruleValue').value);
                break;
            
            case 'no_duplicate_sentences':
                rule[ruleType] = document.getElementById('ruleValue').checked;
                break;
            
            case 'phrase_proximity':
                const terms = document.getElementById('proximityTerms').value.split(',').map(t => t.trim());
                const distance = parseInt(document.getElementById('proximityDistance').value);
                rule[ruleType] = {
                    terms: terms,
                    max_distance: distance
                };
                break;
            
            case 'phrase_order':
                const first = document.getElementById('phraseFirst').value;
                const then = document.getElementById('phraseThen').value;
                rule[ruleType] = {
                    first: first,
                    then: then
                };
                break;
        }

        // Add to schema
        this.schema.rules.push(rule);

        // Update UI
        this.updateSchemaUI();
        this.updateYamlFromSchema();

        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('addRuleModal')).hide();
    }

    /**
     * Update schema UI
     */
    updateSchemaUI() {
        // Update fields
        const fieldsContainer = document.getElementById('schemaFields');
        fieldsContainer.innerHTML = '';

        Object.entries(this.schema.schema).forEach(([fieldName, fieldProps]) => {
            const fieldId = `field-${this.fieldCounter++}`;
            const fieldEl = document.createElement('div');
            fieldEl.className = 'schema-field';
            fieldEl.dataset.fieldName = fieldName;
            
            let fieldDetails = '';
            Object.entries(fieldProps).forEach(([key, value]) => {
                if (key !== 'type') {
                    fieldDetails += `<span class="badge bg-light text-dark me-1">${key}: ${value}</span>`;
                }
            });

            fieldEl.innerHTML = `
                <button type="button" class="btn btn-sm btn-outline-danger remove-btn" 
                        onclick="schemaBuilder.removeField('${fieldName}')">
                    <i class="fa fa-times"></i>
                </button>
                <h6>${fieldName}</h6>
                <div class="mb-2">
                    <span class="badge bg-primary">type: ${fieldProps.type}</span>
                    ${fieldDetails}
                </div>
            `;
            fieldsContainer.appendChild(fieldEl);
        });

        // Update rules
        const rulesContainer = document.getElementById('schemaRules');
        rulesContainer.innerHTML = '';

        this.schema.rules.forEach((rule, index) => {
            const ruleId = `rule-${this.ruleCounter++}`;
            const ruleEl = document.createElement('div');
            ruleEl.className = 'schema-rule';
            
            const ruleType = Object.keys(rule)[0];
            const ruleValue = rule[ruleType];
            
            let ruleValueDisplay = '';
            if (typeof ruleValue === 'object' && ruleValue !== null) {
                if (Array.isArray(ruleValue)) {
                    ruleValueDisplay = ruleValue.join(', ');
                } else {
                    ruleValueDisplay = JSON.stringify(ruleValue);
                }
            } else {
                ruleValueDisplay = String(ruleValue);
            }

            ruleEl.innerHTML = `
                <button type="button" class="btn btn-sm btn-outline-danger remove-btn" 
                        onclick="schemaBuilder.removeRule(${index})">
                    <i class="fa fa-times"></i>
                </button>
                <h6>${ruleType}</h6>
                <div>
                    <span class="badge bg-secondary">${ruleValueDisplay}</span>
                </div>
            `;
            rulesContainer.appendChild(ruleEl);
        });
    }

    /**
     * Remove a field from the schema
     * @param {string} fieldName - Name of the field to remove
     */
    removeField(fieldName) {
        delete this.schema.schema[fieldName];
        this.updateSchemaUI();
        this.updateYamlFromSchema();
    }

    /**
     * Remove a rule from the schema
     * @param {number} index - Index of the rule to remove
     */
    removeRule(index) {
        this.schema.rules.splice(index, 1);
        this.updateSchemaUI();
        this.updateYamlFromSchema();
    }

    /**
     * Update YAML editor from schema object
     */
    updateYamlFromSchema() {
        try {
            const yamlText = jsyaml.dump(this.schema);
            document.getElementById('yamlEditor').value = yamlText;
        } catch (error) {
            console.error('Error converting schema to YAML:', error);
        }
    }

    /**
     * Update schema object from YAML editor
     * @param {string} yamlText - YAML text from editor
     */
    updateSchemaFromYaml(yamlText) {
        try {
            const newSchema = jsyaml.load(yamlText);
            if (newSchema && typeof newSchema === 'object') {
                this.schema = newSchema;
                // Don't update UI here to avoid feedback loop
            }
        } catch (error) {
            console.error('Error parsing YAML:', error);
        }
    }

    /**
     * Load schema from file
     */
    loadSchemaFromFile() {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = '.yaml,.yml';
        
        input.onchange = e => {
            const file = e.target.files[0];
            if (!file) return;
            
            const reader = new FileReader();
            reader.onload = event => {
                try {
                    const yamlText = event.target.result;
                    const newSchema = jsyaml.load(yamlText);
                    
                    if (newSchema && typeof newSchema === 'object') {
                        this.schema = newSchema;
                        this.updateSchemaUI();
                        this.updateYamlFromSchema();
                    }
                } catch (error) {
                    alert('Error loading schema: ' + error.message);
                }
            };
            reader.readAsText(file);
        };
        
        input.click();
    }

    /**
     * Save schema to file
     */
    saveSchemaToFile() {
        try {
            const yamlText = jsyaml.dump(this.schema);
            const blob = new Blob([yamlText], { type: 'text/yaml' });
            const url = URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = 'schema.yaml';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        } catch (error) {
            alert('Error saving schema: ' + error.message);
        }
    }

    /**
     * Generate schema from description using AI
     */
    async generateSchemaFromDescription() {
        const description = document.getElementById('schemaDescription').value.trim();
        
        if (!description) {
            alert('Please enter a description');
            return;
        }
        
        // Show loading state
        const generateBtn = document.getElementById('generateSchema');
        const originalText = generateBtn.textContent;
        generateBtn.textContent = 'Generating...';
        generateBtn.disabled = true;
        
        try {
            const result = await apiHandler.generateSchema(description);
            
            if (result.success) {
                // Update YAML editor
                document.getElementById('yamlEditor').value = result.schema;
                
                // Update schema object
                this.updateSchemaFromYaml(result.schema);
                
                // Update UI
                this.updateSchemaUI();
                
                // Switch to YAML tab
                const yamlTab = document.getElementById('yaml-tab');
                bootstrap.Tab.getOrCreateInstance(yamlTab).show();
            } else {
                alert('Error generating schema: ' + result.message);
            }
        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            // Restore button
            generateBtn.textContent = originalText;
            generateBtn.disabled = false;
        }
    }

    /**
     * Load a template schema
     * @param {string} templateName - Name of the template to load
     */
    loadTemplate(templateName) {
        // Get template from templates.js
        if (templateName in schemaTemplates) {
            this.schema = JSON.parse(JSON.stringify(schemaTemplates[templateName]));
            this.updateSchemaUI();
            this.updateYamlFromSchema();
            
            // Set the prompt in the prompt input field
            const promptInput = document.getElementById('promptInput');
            if (promptInput && typeof getTemplatePrompt === 'function') {
                promptInput.value = getTemplatePrompt(templateName);
            }
            
            // Switch to visual tab
            const visualTab = document.getElementById('visual-tab');
            bootstrap.Tab.getOrCreateInstance(visualTab).show();
        } else {
            alert('Template not found');
        }
    }

    /**
     * Get the current schema
     * @returns {Object} - Current schema object
     */
    getSchema() {
        // For YAML tab, make sure we have the latest changes
        const activeTab = document.querySelector('#schemaTabs .nav-link.active');
        if (activeTab && activeTab.id === 'yaml-tab') {
            const yamlText = document.getElementById('yamlEditor').value;
            this.updateSchemaFromYaml(yamlText);
        }
        
        return this.schema;
    }
}

// Create global schema builder instance
const schemaBuilder = new SchemaBuilder(); 