/**
 * Main JavaScript for LLM Contracts Validator
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize API handler
    initApiHandler();
    
    // Initialize schema builder
    schemaBuilder.init();
    
    // Initialize validation handler
    validationHandler.init();

    // Enable tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Update UI based on initial state
    updateApiKeyBadge();
});

/**
 * Initialize API handler
 */
function initApiHandler() {
    // Load API key from local storage
    const apiKey = apiHandler.getApiKey();
    if (apiKey) {
        document.getElementById('apiKeyInput').value = apiKey;
        updateApiKeyBadge(true);
    }
    
    // API key input event
    document.getElementById('apiKeyInput').addEventListener('input', function(e) {
        apiHandler.saveApiKey(e.target.value);
        updateApiKeyBadge(e.target.value.length > 0);
    });
    
    // Toggle API key visibility
    document.getElementById('toggleApiKey').addEventListener('click', function() {
        const apiKeyInput = document.getElementById('apiKeyInput');
        const toggleBtn = document.getElementById('toggleApiKey');
        
        if (apiKeyInput.type === 'password') {
            apiKeyInput.type = 'text';
            toggleBtn.innerHTML = '<i class="fa fa-eye-slash"></i>';
        } else {
            apiKeyInput.type = 'password';
            toggleBtn.innerHTML = '<i class="fa fa-eye"></i>';
        }
    });
    
    // Test API key button
    document.getElementById('testApiKey').addEventListener('click', async function() {
        const apiKeyStatus = document.getElementById('apiKeyStatus');
        const testBtn = document.getElementById('testApiKey');
        
        // Show loading state
        const originalText = testBtn.textContent;
        testBtn.textContent = 'Testing...';
        testBtn.disabled = true;
        apiKeyStatus.innerHTML = '';
        
        try {
            const result = await apiHandler.testApiKey();
            
            if (result.success) {
                apiKeyStatus.innerHTML = `<span class="api-status-success"><i class="fa fa-check-circle me-1"></i>${result.message}</span>`;
                updateApiKeyBadge(true, true);
            } else {
                apiKeyStatus.innerHTML = `<span class="api-status-error"><i class="fa fa-times-circle me-1"></i>${result.message}</span>`;
                updateApiKeyBadge(true, false);
            }
        } catch (error) {
            apiKeyStatus.innerHTML = `<span class="api-status-error"><i class="fa fa-times-circle me-1"></i>Error: ${error.message}</span>`;
            updateApiKeyBadge(true, false);
        } finally {
            // Restore button
            testBtn.textContent = originalText;
            testBtn.disabled = false;
        }
    });

    // Set up generate button event listener to update output status
    document.getElementById('generateBtn').addEventListener('click', function() {
        updateOutputStatus('generating');
    });
}

/**
 * Update the API key badge status
 * @param {boolean} exists - Whether the API key exists
 * @param {boolean} valid - Whether the API key is valid
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
 * Update the output status badge
 * @param {string} status - Status of the output ('ready', 'generating', 'success', 'error')
 */
function updateOutputStatus(status = 'ready') {
    const badge = document.getElementById('outputStatus');
    const downloadHtmlBtn = document.getElementById('downloadHtmlReport');
    const downloadMdBtn = document.getElementById('downloadMdReport');
    
    switch (status) {
        case 'ready':
            badge.textContent = 'Ready';
            badge.className = 'badge bg-secondary';
            downloadHtmlBtn.disabled = true;
            downloadMdBtn.disabled = true;
            break;
        case 'generating':
            badge.textContent = 'Generating...';
            badge.className = 'badge bg-primary';
            downloadHtmlBtn.disabled = true;
            downloadMdBtn.disabled = true;
            break;
        case 'success':
            badge.textContent = 'Validated';
            badge.className = 'badge bg-success';
            downloadHtmlBtn.disabled = false;
            downloadMdBtn.disabled = false;
            break;
        case 'error':
            badge.textContent = 'Error';
            badge.className = 'badge bg-danger';
            downloadHtmlBtn.disabled = true;
            downloadMdBtn.disabled = true;
            break;
        default:
            badge.textContent = 'Ready';
            badge.className = 'badge bg-secondary';
            downloadHtmlBtn.disabled = true;
            downloadMdBtn.disabled = true;
    }
} 