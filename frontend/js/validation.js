/**
 * Validation handler for LLM Contracts Validator
 */

class ValidationHandler {
    constructor() {
        this.currentOutput = null;
        this.currentSchema = null;
        this.validationResult = null;
        this.apiBaseUrl = 'http://localhost:5000/api'; // Backend API URL
    }

    /**
     * Initialize validation handler
     */
    init() {
        // Generate button
        document.getElementById('generateBtn').addEventListener('click', () => {
            this.generateAndValidate();
        });

        // Copy output button
        document.getElementById('copyOutput').addEventListener('click', () => {
            this.copyOutputToClipboard();
        });

        // Download report buttons
        document.getElementById('downloadHtmlReport').addEventListener('click', () => {
            this.downloadReport('html');
        });

        document.getElementById('downloadMdReport').addEventListener('click', () => {
            this.downloadReport('markdown');
        });
    }

    /**
     * Generate LLM output and validate against schema
     */
    async generateAndValidate() {
        const prompt = document.getElementById('promptInput').value.trim();
        const outputArea = document.getElementById('llmOutput');
        const generateBtn = document.getElementById('generateBtn');
        
        if (!prompt) {
            alert('Please enter a prompt');
            return;
        }
        
        // Get current schema
        this.currentSchema = schemaBuilder.getSchema();
        
        if (!this.currentSchema || 
            (!this.currentSchema.schema && !this.currentSchema.rules) || 
            (Object.keys(this.currentSchema.schema || {}).length === 0 && 
             (this.currentSchema.rules || []).length === 0)) {
            alert('Please create a schema first');
            return;
        }
        
        // Show loading state
        generateBtn.disabled = true;
        generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i> Generating...';
        outputArea.value = 'Generating output...';
        updateOutputStatus('generating');
        
        try {
            // Generate text from LLM
            const result = await apiHandler.generateText(prompt);
            
            if (result.success) {
                this.currentOutput = result.text;
                outputArea.value = this.currentOutput;
                
                // Validate the output
                await this.validateOutput();
            } else {
                outputArea.value = 'Error: ' + result.message;
                this.showValidationError(result.message);
                updateOutputStatus('error');
            }
        } catch (error) {
            outputArea.value = 'Error: ' + error.message;
            this.showValidationError(error.message);
            updateOutputStatus('error');
        } finally {
            // Restore button
            generateBtn.disabled = false;
            generateBtn.innerHTML = '<i class="fas fa-play me-1"></i> Generate & Validate';
        }
    }

    /**
     * Validate the current output against the schema
     */
    async validateOutput() {
        if (!this.currentOutput || !this.currentSchema) {
            return;
        }
        
        const resultsContainer = document.getElementById('validationResults');
        resultsContainer.innerHTML = `
            <div class="alert alert-info">
                <i class="fas fa-spinner fa-spin me-2"></i>
                Validating output...
            </div>
        `;
        
        try {
            // Convert schema to YAML
            const schemaYaml = jsyaml.dump(this.currentSchema);
            
            // Call the backend API for validation
            const response = await fetch(`${this.apiBaseUrl}/validate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    output: this.currentOutput,
                    schema: schemaYaml
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Store validation result
                this.validationResult = {
                    isValid: data.is_valid,
                    errors: data.errors,
                    schema: this.currentSchema
                };
                
                // Display validation result
                this.displayValidationResult();
                updateOutputStatus('success');
            } else {
                this.showValidationError(data.message);
                updateOutputStatus('error');
            }
        } catch (error) {
            this.showValidationError(error.message);
            updateOutputStatus('error');
        }
    }

    /**
     * Display validation result
     */
    displayValidationResult() {
        const resultsContainer = document.getElementById('validationResults');
        
        if (!this.validationResult) {
            resultsContainer.innerHTML = '<div class="alert alert-warning">No validation result available</div>';
            return;
        }
        
        if (this.validationResult.isValid) {
            resultsContainer.innerHTML = `
                <div class="validation-success">
                    <h5><i class="fas fa-check-circle me-2"></i> Validation Passed!</h5>
                    <p>The output meets all schema requirements and rules.</p>
                </div>
            `;
        } else {
            let errorList = '';
            this.validationResult.errors.forEach(error => {
                errorList += `<li>${error}</li>`;
            });
            
            resultsContainer.innerHTML = `
                <div class="validation-error">
                    <h5><i class="fas fa-times-circle me-2"></i> Validation Failed!</h5>
                    <p>Found ${this.validationResult.errors.length} error(s):</p>
                    <ul>${errorList}</ul>
                </div>
            `;
        }
    }

    /**
     * Show validation error
     * @param {string} message - Error message
     */
    showValidationError(message) {
        const resultsContainer = document.getElementById('validationResults');
        resultsContainer.innerHTML = `
            <div class="alert alert-danger">
                <i class="fas fa-exclamation-triangle me-2"></i>
                <strong>Error:</strong> ${message}
            </div>
        `;
    }

    /**
     * Copy output to clipboard
     */
    copyOutputToClipboard() {
        const outputArea = document.getElementById('llmOutput');
        outputArea.select();
        document.execCommand('copy');
        
        // Show feedback
        const copyBtn = document.getElementById('copyOutput');
        const originalIcon = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fas fa-check"></i>';
        setTimeout(() => {
            copyBtn.innerHTML = originalIcon;
        }, 2000);
    }

    /**
     * Download validation report
     * @param {string} format - Report format (html or markdown)
     */
    async downloadReport(format) {
        if (!this.currentOutput || !this.currentSchema) {
            alert('No validation data available');
            return;
        }
        
        try {
            // Convert schema to YAML
            const schemaYaml = jsyaml.dump(this.currentSchema);
            
            // Call the backend API to generate report
            const response = await fetch(`${this.apiBaseUrl}/generate-report`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    output: this.currentOutput,
                    schema: schemaYaml,
                    format: format
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Create and download the report file
                const blob = new Blob([data.report], { 
                    type: format === 'html' ? 'text/html' : 'text/markdown' 
                });
                const url = URL.createObjectURL(blob);
                
                const a = document.createElement('a');
                a.href = url;
                a.download = format === 'html' ? 'validation_report.html' : 'validation_report.md';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            } else {
                alert('Error generating report: ' + data.message);
            }
        } catch (error) {
            alert('Error: ' + error.message);
        }
    }
}

// Create global validation handler instance
const validationHandler = new ValidationHandler(); 