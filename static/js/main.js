// main.js

document.addEventListener('DOMContentLoaded', function() {
  /* Dark Mode Toggle */
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('theme');
  const themeToggle = document.getElementById('theme-toggle');

  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-mode');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      document.body.classList.toggle('dark-mode');
      localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
    });
  }

  /* Auto-Dismiss Flash Messages */
  const flashMessages = document.querySelectorAll('.alert');
  flashMessages.forEach(msg => {
    setTimeout(() => {
      msg.classList.add('fade-out');
      setTimeout(() => msg.remove(), 500);
    }, 4000);
  });

  /* Animate Cards */
  const entryCards = document.querySelectorAll('.entry-card');
  entryCards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.07}s`;
    card.classList.add('slide-up');
  });

  /* Confirm Delete */
  window.confirmDelete = function(formId) {
    if (confirm('Are you sure you want to delete this entry? This action cannot be undone.')) {
      document.getElementById(formId).submit();
    }
    return false;
  }

  /* Rich Text Toolbar + Live Markdown Preview */
  const contentArea = document.getElementById('content');
  const previewArea = document.getElementById('markdown-preview');

  if (contentArea && previewArea) {
    contentArea.addEventListener('input', updatePreview);
    updatePreview(); // Initial

    const toolbar = document.createElement('div');
    toolbar.className = 'formatting-toolbar';
    toolbar.innerHTML = `
      <button type="button" data-format="bold" title="Bold"><b>B</b></button>
      <button type="button" data-format="italic" title="Italic"><i>I</i></button>
      <button type="button" data-format="heading" title="Heading">H</button>
      <button type="button" data-format="list" title="List">• List</button>
    `;
    contentArea.parentNode.insertBefore(toolbar, contentArea);

    toolbar.addEventListener('click', (e) => {
      const button = e.target.closest('button');
      if (!button) return;
      const format = button.getAttribute('data-format');
      applyFormatting(format);
    });

    function applyFormatting(format) {
      const start = contentArea.selectionStart;
      const end = contentArea.selectionEnd;
      const selected = contentArea.value.substring(start, end);
      let replacement = '';

      switch(format) {
        case 'bold':
          replacement = `**${selected || 'bold text'}**`;
          break;
        case 'italic':
          replacement = `*${selected || 'italic text'}*`;
          break;
        case 'heading':
          replacement = `# ${selected || 'Heading'}`;
          break;
        case 'list':
          replacement = `- ${selected || 'List item'}`;
          break;
      }

      contentArea.value = contentArea.value.substring(0, start) + replacement + contentArea.value.substring(end);
      contentArea.focus();
      updatePreview();
    }

    function updatePreview() {
      const raw = contentArea.value;
      let html = raw
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        .replace(/\*\*(.*?)\*\*/gim, '<b>$1</b>')
        .replace(/\*(.*?)\*/gim, '<i>$1</i>')
        .replace(/^- (.*$)/gim, '<li>$1</li>')
        .replace(/\n$/gim, '<br>');

      if (html.includes('<li>')) {
        html = html.replace(/(<li>.*<\/li>)+/g, match => `<ul>${match}</ul>`);
      }

      previewArea.innerHTML = html.trim();
    }
  }
});
