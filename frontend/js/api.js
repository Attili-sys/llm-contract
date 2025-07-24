/**
 * API handling for LLM Contracts Validator
 */

class ApiHandler {
    constructor() {
        this.apiKey = localStorage.getItem('geminiApiKey') || '';
        this.apiUrl = 'https://generativelanguage.googleapis.com/v1beta';
        this.model = 'gemini-2.0-flash'; // Updated model name
    }

    /**
     * Save API key to local storage
     * @param {string} apiKey - Gemini API key
     */
    saveApiKey(apiKey) {
        this.apiKey = apiKey;
        localStorage.setItem('geminiApiKey', apiKey);
    }

    /**
     * Get API key from local storage
     * @returns {string} - Gemini API key
     */
    getApiKey() {
        return this.apiKey;
    }

    /**
     * Test if API key is valid
     * @returns {Promise<Object>} - Response object with status and message
     */
    async testApiKey() {
        if (!this.apiKey) {
            return {
                success: false,
                message: 'API key is empty'
            };
        }

        try {
            // Make a simple model list request to test the API key
            const response = await fetch(`${this.apiUrl}/models?key=${this.apiKey}`);
            const data = await response.json();

            if (response.ok) {
                return {
                    success: true,
                    message: 'API key is valid',
                    models: data.models || []
                };
            } else {
                return {
                    success: false,
                    message: data.error?.message || 'Invalid API key'
                };
            }
        } catch (error) {
            return {
                success: false,
                message: `Error: ${error.message}`
            };
        }
    }

    /**
     * Generate text using Gemini API
     * @param {string} prompt - User prompt
     * @returns {Promise<Object>} - Response with generated text
     */
    async generateText(prompt) {
        if (!this.apiKey) {
            return {
                success: false,
                message: 'API key is not set'
            };
        }

        try {
            const url = `${this.apiUrl}/models/${this.model}:generateContent?key=${this.apiKey}`;
            
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    contents: [
                        {
                            parts: [
                                {
                                    text: prompt
                                }
                            ]
                        }
                    ],
                    generationConfig: {
                        temperature: 0.7,
                        topK: 40,
                        topP: 0.95,
                        maxOutputTokens: 2048,
                    }
                })
            });

            const data = await response.json();

            if (response.ok) {
                // Extract the generated text from the response
                const generatedText = data.candidates?.[0]?.content?.parts?.[0]?.text || '';
                
                return {
                    success: true,
                    text: generatedText
                };
            } else {
                return {
                    success: false,
                    message: data.error?.message || 'Failed to generate text'
                };
            }
        } catch (error) {
            return {
                success: false,
                message: `Error: ${error.message}`
            };
        }
    }

    /**
     * Generate schema from description using Gemini API
     * @param {string} description - Schema description
     * @returns {Promise<Object>} - Response with generated schema
     */
    async generateSchema(description) {
        if (!this.apiKey) {
            return {
                success: false,
                message: 'API key is not set'
            };
        }

        try {
            const url = `${this.apiUrl}/models/${this.model}:generateContent?key=${this.apiKey}`;
            
            const prompt = `
            Create a YAML schema for llm-contracts validation based on this description:
            
            "${description}"
            
            The schema should follow this format:
            
            \`\`\`yaml
            schema:
              # Field definitions with types and validation rules
              field_name:
                type: str|int|float|bool|list|dict
                # Other validation properties
            
            rules:
              # Content validation rules - IMPORTANT: Each rule must be formatted as "- rule_name: value"
              - keyword_must_include: "required_word"
              - word_count_min: 100
              - min_list_items: 3
            \`\`\`
            
            IMPORTANT RULES FORMAT INSTRUCTIONS:
            1. Each rule must be a direct key-value pair with a dash prefix
            2. DO NOT use "rule_type" or "rule_value" as keys
            3. The correct format is "- rule_name: value" (e.g., "- keyword_must_include: quality")
            4. Common rule names: keyword_must_include, keyword_must_not_include, word_count_min, word_count_max, min_list_items, no_placeholder_text
            
            Include appropriate validation rules based on the description. Return only the YAML schema without any explanations.
            `;
            
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    contents: [
                        {
                            parts: [
                                {
                                    text: prompt
                                }
                            ]
                        }
                    ],
                    generationConfig: {
                        temperature: 0.2,
                        topK: 40,
                        topP: 0.95,
                        maxOutputTokens: 2048,
                    }
                })
            });

            const data = await response.json();

            if (response.ok) {
                // Extract the generated schema from the response
                let generatedSchema = data.candidates?.[0]?.content?.parts?.[0]?.text || '';
                
                // Clean up the schema (remove markdown code blocks if present)
                generatedSchema = generatedSchema.replace(/```yaml\n/g, '').replace(/```\n?/g, '');
                
                return {
                    success: true,
                    schema: generatedSchema
                };
            } else {
                return {
                    success: false,
                    message: data.error?.message || 'Failed to generate schema'
                };
            }
        } catch (error) {
            return {
                success: false,
                message: `Error: ${error.message}`
            };
        }
    }
}

// Create global API handler instance
const apiHandler = new ApiHandler(); 