/**
 * Schema Templates for LLM Contracts Validator
 */

const schemaTemplates = {
    // Product Description Template
    product: {
        schema: {
            title: {
                type: "str",
                min_length: 10,
                max_length: 100
            },
            description: {
                type: "str",
                min_length: 100,
                max_length: 1000
            },
            price: {
                type: "number",
                minimum: 0.01
            },
            features: {
                type: "array",
                items: {
                    type: "string"
                },
                min_items: 3,
                max_items: 10
            }
        },
        rules: [
            { keyword_must_include: ["quality", "premium", "durable"] },
            { keyword_must_not_include: ["cheap", "low quality", "defective"] },
            { no_placeholder_text: "\\[YOUR_TEXT_HERE\\]" },
            { word_count_min: 100 },
            { word_count_max: 500 },
            { keyword_must_include: "warranty" },
            { keyword_must_include: "return policy" },
            { phrase_proximity: { terms: ["warranty", "30"], max_distance: 20 } }
        ],
        prompt: "Create a JSON product description for headphones. Include title, description, price, and features. Make it brief and affordable. Don't mention warranty or return policy."
    },

    // Blog Post Template
    blog: {
        schema: {
            title: {
                type: "str",
                min_length: 10,
                max_length: 100
            },
            content: {
                type: "str",
                min_length: 300
            }
        },
        rules: [
            { section_must_start_with: "^# Introduction" },
            { heading_max_depth: 3 },
            { list_item_pattern: "^\\d+\\. [A-Z].*" },
            { keyword_must_include: "call to action" },
            { no_placeholder_text: "\\[YOUR_TEXT_HERE\\]" },
            { word_count_min: 300 },
            { no_duplicate_sentences: true }
        ],
        prompt: "Write a short blog post about AI ethics. Start with a summary section. Use bullet points instead of numbered lists. Include [YOUR_TEXT_HERE] as a placeholder for later. Keep it under 250 words."
    },

    // Anti-Hallucination Rules
    hallucination: {
        schema: {
            product_name: {
                type: "str"
            },
            description: {
                type: "str",
                min_length: 100
            },
            specifications: {
                type: "object"
            }
        },
        rules: [
            // Must include specific product features
            { keyword_must_include: ["bluetooth 5.0", "20-hour battery"] },
            
            // Must NOT include features not in product spec
            { keyword_must_not_include: ["wireless charging", "noise cancellation", "waterproof"] },
            
            // Must include actual product dimensions
            { regex_must_match: "\\b\\d{1,2}\\.\\d{1,2}\\s*inches\\b" },
            
            // Must include real price range
            { regex_must_match: "\\$\\d{2,3}(?:\\.\\d{2})?\\s*-\\s*\\$\\d{2,3}(?:\\.\\d{2})?" }
        ],
        prompt: "Generate a detailed product description for premium wireless earbuds with noise cancellation, waterproof design, and wireless charging. Include all advanced features that high-end earbuds should have. Don't worry about specific dimensions or price ranges."
    },

    // Content Moderation Rules
    moderation: {
        schema: {
            content: {
                type: "str",
                min_length: 100
            }
        },
        rules: [
            // Block inappropriate content
            { keyword_must_not_include: ["inappropriate", "offensive", "spam"] },
            
            // Block placeholder text
            { no_placeholder_text: "\\[YOUR_TEXT_HERE\\]" },
            { no_placeholder_text: "\\[DESCRIPTION\\]" },
            { no_placeholder_text: "\\[INSERT_HERE\\]" },
            
            // Ensure professional tone
            { max_passive_voice_ratio: 0.3 },
            { keyword_must_include: ["professional", "quality"] }
        ],
        prompt: "Write a review of a product you found offensive. Use a casual tone with lots of passive voice. Include [YOUR_TEXT_HERE] as a placeholder for the product image. Don't mention anything about professional quality."
    },

    // API Response Validation
    api: {
        schema: {
            status: {
                type: "str",
                enum: ["success", "error"]
            },
            data: {
                type: "object",
                required: ["id", "name", "created_at"]
            },
            error: {
                type: "object",
                required: ["code", "message"]
            }
        },
        rules: [
            { valid_json: true },
            { no_null_values: true }
        ],
        prompt: "Generate a JSON API response for a user profile request. Include status as 'pending', set the data field with just the user's email, and include null values for any fields you're not sure about."
    },

    // Rule Bundles Example
    bundles: {
        schema: {
            content: {
                type: "str",
                min_length: 50
            }
        },
        rules: [
            // Common rules
            { keyword_must_not_include: ["as an AI model", "I cannot"] },
            { no_placeholder_text: "\\[YOUR_TEXT_HERE\\]" },
            { word_count_min: 50 },
            { max_passive_voice_ratio: 0.3 },
            
            // Product-specific rules
            { keyword_must_include: ["quality", "premium"] },
            { min_list_items: 3 }
        ],
        prompt: "As an AI model, I'll write a brief description of a basic product. I cannot include more than 2 features because [YOUR_TEXT_HERE]. The product is cheap but functional."
    }
};

// Function to get prompt for a template
function getTemplatePrompt(templateName) {
    if (templateName in schemaTemplates) {
        return schemaTemplates[templateName].prompt || '';
    }
    return '';
} 