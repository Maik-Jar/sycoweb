
$(document).ready(function(){

    const select_tipo_cliente = document.getElementById('id_tipo')

    select_tipo_cliente.addEventListener('change', async (event) => {

        if (event.target.value == 2){ // Cuando sea una Persona 
            
            const r = event.target.value
            
            window.location.href= `?clientType=${r}`

        } else if (event.target.value == 1) { // Cuando sea una Empresa

            const r = event.target.value
            
            window.location.href= `?clientType=${r}`
        }
    })
    
})

