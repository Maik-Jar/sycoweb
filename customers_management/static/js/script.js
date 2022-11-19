// $(document).ready(function(){

//     $('#btinformacion').click(function(){

//         var fila = $(this).parent();
//         var id = fila.siblings("th:eq(0)").text();

//         var token = $('body > div > div > main > input[type=hidden]').val();

//         $.ajaxSetup({
//             beforeSend: function(xhr) {
//                 xhr.setRequestHeader("X-CSRFToken", token);
//             }
//         });

//         $.ajax({
            
//             type: 'POST',
//             data: {json: JSON.stringify({impuestoid:id, codigo:1})},
//             dataType: 'json',
//             success: function(respuesta){
//                 if ($('#modal-body').find('#form_impuesto').length) {
//                     //$('#form_impuesto').replaceWith(respuesta);
//                     $(' #form_impuesto').load(respuesta['data']);
//                 } else {
//                     $('#modal-body').append(respuesta);
//                 }
//                 },
//             error: function(error){
//                     //codigo error
//                     console.log(error);
                    
//                 }
//         });
        
//     });

// });

$(document).ready(function(){
    
    // const exampleModal = document.getElementById('exampleModalgestion')
    // exampleModal.addEventListener('show.bs.modal', event => {
    //     // Button that triggered the modal
    //     const button = event.relatedTarget
    //     // Extract info from data-bs-* attributes
    //     const recipient = button.getAttribute('data-bs-whatever')
    //     // If necessary, you could initiate an AJAX request here
    //     // and then do the updating in a callback.
    //     // 
    //     // Update the modal's content.
    //     const modalTitle = exampleModal.querySelector('.modal-body')
    //     const modalBodyInput = exampleModal.querySelector('form')

    //     var id = recipient.substring(0, recipient.indexOf(':', 0))
        
    //     var content= recipient.substring(recipient.indexOf(':', 0)+1)

    //     modalTitle.textContent = `¿Está seguro que desea eliminar ${content}?`
        
    //     var url = modalBodyInput.action

    //     modalBodyInput.action= url.replace('/0/','/'+id+'/')
    // })

    const select_tipo_cliente = document.getElementById('id_tipo')

    // const inputrazon_social = document.getElementById('id_razon_social')
    // const inputnombre = document.getElementById('id_nombre')
    // const inputapellido1 = document.getElementById('id_apellido1')
    // const inputapellido2 = document.getElementById('id_apellido2')

    // inputrazon_social.removeAttribute('required')
    // const divparent_inputrazon_social = inputrazon_social.parentNode
    // divparent_inputrazon_social.hidden = true

    select_tipo_cliente.addEventListener('change', async (event) => {

        if (event.target.value == 2){ // Cuando sea una Persona 
            // // Razon social
            // inputrazon_social.removeAttribute('required')
            // divparent_inputrazon_social.hidden = true
            // // Nombre
            // inputnombre.setAttribute('required', true)
            // const divparent_inputnombre = inputnombre.parentNode
            // divparent_inputnombre.hidden = false
            // // 1er. Apellido
            // inputapellido1.setAttribute('required', true)
            // const divparent_inputapellido1 = inputapellido1.parentNode
            // divparent_inputapellido1.hidden = false
            // // 2do. Apellido
            // inputapellido2.setAttribute('required', true)
            // const divparent_inputapellido2 = inputapellido2.parentNode
            // divparent_inputapellido2.hidden = false
            const r = event.target.value
            
            window.location.href= `?clientType=${r}`
            
            
            

        } else if (event.target.value == 1) { // Cuando sea una Empresa
            // // Razon social
            // inputrazon_social.setAttribute('required', true)
            // const divparent_inputrazon_social = inputrazon_social.parentNode
            // divparent_inputrazon_social.hidden = false
            // // Nombre
            // inputnombre.removeAttribute('required')
            // const divparent_inputnombre = inputnombre.parentNode
            // divparent_inputnombre.hidden = true
            // // 1er. Apellido
            // inputapellido1.removeAttribute('required')
            // const divparent_inputapellido1 = inputapellido1.parentNode
            // divparent_inputapellido1.hidden = true
            // // 2do. Apellido
            // inputapellido2.removeAttribute('required')
            // const divparent_inputapellido2 = inputapellido2.parentNode
            // divparent_inputapellido2.hidden = true

            const r = event.target.value
            
            window.location.href= `?clientType=${r}`

            

        }

    })
    
})

