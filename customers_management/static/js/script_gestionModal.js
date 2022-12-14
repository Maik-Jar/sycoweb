
$(document).ready(function(){
    
    const exampleModal = document.getElementById('exampleModalgestion')
    exampleModal.addEventListener('show.bs.modal', event => {
        // Button that triggered the modal
        const button = event.relatedTarget
        // Extract info from data-bs-* attributes
        const recipient = button.getAttribute('data-bs-whatever')
        // If necessary, you could initiate an AJAX request here
        // and then do the updating in a callback.
        // 
        // Update the modal's content.
        const modalTitle = exampleModal.querySelector('.modal-body')
        const modalBodyInput = exampleModal.querySelector('#form_eliminar')

        var id = recipient.substring(0, recipient.indexOf(':', 0))
        
        var content= recipient.substring(recipient.indexOf(':', 0)+1)

        modalTitle.textContent = `¿Está seguro que desea eliminar ${content}?`
        
        var url = modalBodyInput.action

        modalBodyInput.action= url.replace('/0/','/'+id+'/')
    })
})

