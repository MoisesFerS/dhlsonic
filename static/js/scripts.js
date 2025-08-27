/* GLOBAL JS */

/*  ============================================================
    MODAL
    ============================================================ */ 

const modals = document.querySelectorAll('.modal-container');
const errorModal = document.querySelector('#error-modal')

modals.forEach(modal => {
    modal.addEventListener('click', function(event){
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
})
