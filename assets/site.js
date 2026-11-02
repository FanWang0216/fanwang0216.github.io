'use strict';
document.querySelectorAll('[data-wechat]').forEach(button => {
  button.addEventListener('click', async () => {
    const status = document.getElementById('copy-status');
    try { await navigator.clipboard.writeText(button.dataset.wechat); status.textContent = 'Copied'; }
    catch { status.textContent = 'Select the ID to copy it manually.'; }
  });
});
