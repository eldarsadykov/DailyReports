document.addEventListener('alpine:init', () => {
  Alpine.data('dailyReports', () => ({
    selected: [],
    copyToClipboard() {
      if (this.selected.length === 0) {
        alert('No items selected.');
        return;
      }

      const today = new Date().toLocaleDateString('ru-RU', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      });

      const text = `${today}\n\n${this.selected.join('\n')}`;

      navigator.clipboard.writeText(text)
      .then(() => alert('Copied:\n' + text))
      .catch(err => console.error('Copy failed:', err));
    }
  }));
});
