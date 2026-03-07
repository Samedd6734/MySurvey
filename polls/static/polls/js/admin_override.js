document.addEventListener('DOMContentLoaded', function () {
    function initializeCustomTrashButtons() {
        // Hedef: Standart Django delete checkbox'ları
        const deleteContainers = document.querySelectorAll('.delete:not(.djnesting-remove), td.delete:not(.djnesting-remove)');

        deleteContainers.forEach(container => {
            // Eğer djnesting-remove butonu zaten varsa (yeni eklenen satırlar), bizimkini eklemeyelim
            if (container.querySelector('.djnesting-remove')) return;
            if (container.querySelector('.custom-trash-btn')) return;

            const checkbox = container.querySelector('input[type="checkbox"]');
            if (checkbox) {
                checkbox.style.display = 'none';
                const label = container.querySelector('label');
                if (label) label.style.display = 'none';

                const btn = document.createElement('div');
                btn.className = 'custom-trash-btn';
                btn.title = (typeof gettext !== 'undefined') ? gettext("Delete") : "Delete";
                btn.innerHTML = `<svg viewBox="0 0 24 24"><path d="M19 6l-1.2 14.4A2 2 0 0 1 15.8 22H8.2a2 2 0 0 1-2-1.6L5 6m4 0V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2m-5 5v6m4-6v6"/><line x1="3" y1="6" x2="21" y2="6"/></svg>`;

                btn.addEventListener('click', function (e) {
                    e.preventDefault();
                    const promptMsg = (typeof gettext !== 'undefined') ? gettext("Are you sure?") : "Are you sure?";
                    if (confirm(promptMsg)) {
                        checkbox.checked = true;
                        const row = container.closest('tr.form-row, div.inline-related');
                        if (row) {
                            row.classList.add('row-marked-for-delete');
                        }
                    }
                });
                container.appendChild(btn);
            }
        });
    }

    initializeCustomTrashButtons();

    const observer = new MutationObserver((mutations) => {
        let shouldRun = false;
        mutations.forEach((mutation) => {
            if (mutation.addedNodes.length) shouldRun = true;
        });
        if (shouldRun) initializeCustomTrashButtons();
    });
    observer.observe(document.body, { childList: true, subtree: true });
});
