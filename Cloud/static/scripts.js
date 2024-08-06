document.addEventListener("DOMContentLoaded", function() {
    // Dil Seçimi Menüsünü Yönetme
    const langButtons = document.querySelectorAll('.lang-button');
    langButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const lang = this.getAttribute('data-lang');
            window.location.href = `/set_lang/${lang}`;
        });
    });

    // Dosya Yükleme Formu Kontrolü
    const uploadForm = document.querySelector('#upload-form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function(event) {
            const fileInput = document.querySelector('#file');
            if (!fileInput.files.length) {
                alert('Please select a file to upload.');
                event.preventDefault();  // Formun gönderilmesini engeller
            }
        });
    }

    // Dosya Kopyalama Formu Kontrolü
    const copyForm = document.querySelector('#copy-form');
    if (copyForm) {
        copyForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const targetFolder = document.querySelector('#target_folder').value;
            if (targetFolder.trim() === '') {
                alert('Please enter a target folder path.');
                return;
            }
            this.submit();
        });
    }

    // Dosya Silme
    const deleteLinks = document.querySelectorAll('.delete-file');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this file?')) {
                event.preventDefault();  // Silme işlemini engeller
            }
        });
    });
});