/**
 * Main JavaScript for LLM Contracts Validator
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize components
    initApiHandler();
    initSchemaBuilder();
    initValidation();
    
    // Enable tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

/**
 * Initialize API handler
 */
function initApiHandler() {
    apiHandler.init();
    
    // Check for saved API key
    const apiKey = apiHandler.getApiKey();
    if (apiKey) {
        document.getElementById('apiKeyInput').value = apiKey;
        updateApiKeyBadge(true);
    }
    
    // API key input event
    document.getElementById('apiKeyInput').addEventListener('input', function() {
        const apiKey = this.value.trim();
        if (apiKey) {
            apiHandler.saveApiKey(apiKey);
            updateApiKeyBadge(true);
        } else {
            apiHandler.saveApiKey('');
            updateApiKeyBadge(false);
        }
    });
    
    // Toggle API key visibility
    document.getElementById('toggleApiKey').addEventListener('click', function() {
        const apiKeyInput = document.getElementById('apiKeyInput');
        const eyeIcon = this.querySelector('i');
        
        if (apiKeyInput.type === 'password') {
            apiKeyInput.type = 'text';
            eyeIcon.classList.remove('fa-eye');
            eyeIcon.classList.add('fa-eye-slash');
        } else {
            apiKeyInput.type = 'password';
            eyeIcon.classList.remove('fa-eye-slash');
            eyeIcon.classList.add('fa-eye');
        }
    });
    
    // Test API key
    document.getElementById('testApiKey').addEventListener('click', async function() {
        const apiKey = document.getElementById('apiKeyInput').value.trim();
        const apiKeyStatus = document.getElementById('apiKeyStatus');
        
        if (!apiKey) {
            apiKeyStatus.innerHTML = '<span class="api-status-error"><i class="fas fa-times-circle me-1"></i> No API key provided</span>';
            updateApiKeyBadge(false);
            return;
        }
        
        // Show loading state
        this.disabled = true;
        this.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i> Testing...';
        apiKeyStatus.innerHTML = '<span class="text-muted"><i class="fas fa-spinner fa-spin me-1"></i> Testing...</span>';
        
        try {
            const result = await apiHandler.testApiKey();
            
            if (result.success) {
                apiKeyStatus.innerHTML = '<span class="api-status-success"><i class="fas fa-check-circle me-1"></i> Valid</span>';
                updateApiKeyBadge(true, true);
            } else {
                apiKeyStatus.innerHTML = `<span class="api-status-error"><i class="fas fa-times-circle me-1"></i> ${result.message}</span>`;
                updateApiKeyBadge(true, false);
            }
        } catch (error) {
            apiKeyStatus.innerHTML = `<span class="api-status-error"><i class="fas fa-times-circle me-1"></i> ${error.message}</span>`;
            updateApiKeyBadge(true, false);
        } finally {
            // Restore button
            this.disabled = false;
            this.innerHTML = '<i class="fas fa-vial me-1"></i> Test Key';
        }
    });
}

/**
 * Update API key badge
 * @param {boolean} exists - Whether API key exists
 * @param {boolean|null} valid - Whether API key is valid (null if not tested)
 */
function updateApiKeyBadge(exists = false, valid = null) {
    const badge = document.getElementById('apiKeyBadge');
    
    if (!exists) {
        badge.textContent = 'Not Set';
        badge.className = 'badge bg-secondary';
        return;
    }
    
    if (valid === null) {
        badge.textContent = 'Set';
        badge.className = 'badge bg-primary';
    } else if (valid) {
        badge.textContent = 'Valid';
        badge.className = 'badge bg-success';
    } else {
        badge.textContent = 'Invalid';
        badge.className = 'badge bg-danger';
    }
}

/**
 * Initialize schema builder
 */
function initSchemaBuilder() {
    schemaBuilder.init();
}

/**
 * Initialize validation
 */
function initValidation() {
    validationHandler.init();
    
    // Enable report download buttons when validation is successful
    document.addEventListener('validationComplete', function(e) {
        const downloadHtmlBtn = document.getElementById('downloadHtmlReport');
        const downloadMdBtn = document.getElementById('downloadMdReport');
        
        if (e.detail && e.detail.isValid !== undefined) {
            downloadHtmlBtn.disabled = false;
            downloadMdBtn.disabled = false;
        } else {
            downloadHtmlBtn.disabled = true;
            downloadMdBtn.disabled = true;
        }
    });
}

/**
 * Update output status badge
 * @param {string} status - Status (ready, generating, success, error)
 */
function updateOutputStatus(status) {
    const badge = document.getElementById('outputStatus');
    
    switch (status) {
        case 'ready':
            badge.textContent = 'Ready';
            badge.className = 'badge bg-secondary';
            break;
        case 'generating':
            badge.textContent = 'Generating';
            badge.className = 'badge bg-primary';
            break;
        case 'success':
            badge.textContent = 'Valid';
            badge.className = 'badge bg-success';
            break;
        case 'error':
            badge.textContent = 'Invalid';
            badge.className = 'badge bg-danger';
            break;
        default:
            badge.textContent = 'Ready';
            badge.className = 'badge bg-secondary';
    }
} 