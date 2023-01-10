function eliminarFila(btn_element){
    // remover fila de la tabla
    
    const tabla = document.getElementById('tbbody')

    cell= btn_element.parentElement
    row= cell.parentElement
    tabla.deleteRow(row.rowIndex-1)

    calcula_subtotal()
    calcula_total()

}

async function calcular_impuesto_parcial(id_item, cantidad){

    try {
        const respuesta = await fetch(`http://127.0.0.1:8000/product_and_services/obtener_item/${id_item}/`)

        if (respuesta.status === 200){

            const datos = await respuesta.json()

            var impuesto = Number((datos.precio*cantidad)*datos.impuesto).toFixed(2)

            return impuesto 
           
        } 

    } catch (error) {

        const toastLiveExample_danger = document.getElementById('liveToast_danger')

        const toastBody_danger = toastLiveExample_danger.querySelector('.toast-body')
        toastBody_danger.textContent = `Ha ocurrido un error.`

        const toast = new bootstrap.Toast(toastLiveExample_danger)
        
        toast.show()

        console.log(error)
    }
}

function calcular_monto_parcial(preciound, cantidad, impuesto){

    return Number((preciound*cantidad)+Number(impuesto)).toFixed(2)

}

function calcula_subtotal(){

    var tabla = document.getElementById('tbbody')
    var inputSubtotal = document.getElementById('inputSubtotal')

    var subtotal = Number(0.00).toFixed(2)

    for (var r = 0; r < tabla.rows.length; r++){
        subtotal = (Number(subtotal) + Number(tabla.rows[r].cells[5].innerHTML)).toFixed(2)
    }
    
    inputSubtotal.value = Number(subtotal).toFixed(2)
}

function calcula_total(){

    var subtotal = document.getElementById('inputSubtotal').value
    var descuento = document.getElementById('inputDescuento').value
    const inputtotal = document.getElementById('inputTotal')
    
    inputtotal.value = (Number(subtotal)-Number(descuento)).toFixed(2)

}

const btbuscarcliente = document.getElementById('btbuscarcliente')
btbuscarcliente.addEventListener('click', async () => {

    const input_tipo_documento = document.getElementById('id_tipo_documento')
    const input_documento_cliente = document.getElementById('id_documento_cliente')
    const toastLiveExample_danger = document.getElementById('liveToast_danger')
    const toastBody_danger = toastLiveExample_danger.querySelector('.toast-body')

    var id_tipo_documento = input_tipo_documento.value
    var no_documento = input_documento_cliente.value

    try {

        const respuesta = await fetch(`http://127.0.0.1:8000/customers_management/obtener_cliente/${id_tipo_documento}/${no_documento}/`)

        if (respuesta.status === 200){
            const input_cliente = document.getElementById('id_nombre_cliente')
            const input_telefono = document.getElementById('id_telefono_cliente')
            const input_id_cliente = document.getElementById('id_id_cliente')

            const datos = await respuesta.json()

            input_cliente.value= datos.fullname
            input_telefono.value= datos.telefono
            input_id_cliente.value= datos.id

            input_cliente.setAttribute('readonly','true')

        } else if (respuesta.status === 404) {
            
            toastBody_danger.textContent = `No existe un cliente con el documento No. ${no_documento}`

            const toast = new bootstrap.Toast(toastLiveExample_danger)
            
            toast.show()
        }

    } catch(error){

        toastBody_danger.textContent = `Ha ocurrido un error.`

        const toast = new bootstrap.Toast(toastLiveExample_danger)
        
        toast.show()

        console.log(error)
    }
})

const btbuscaritem = document.getElementById('btbuscaritem')
btbuscaritem.addEventListener('click', async () => {

    const input_id_item = document.getElementById('id_item')
    const id_item = input_id_item.value
    const toastLiveExample_danger = document.getElementById('liveToast_danger')
    const toastBody_danger = toastLiveExample_danger.querySelector('.toast-body')

    let existe = false

    for (var r = 0; r < tbbody.rows.length; r++){
        if (Number(tbbody.rows[r].cells[0].innerHTML) == input_id_item.value){
            existe = true
            break
        }
    }
                
    if (existe){

        toastBody_danger.textContent = `Ya ha insertado un item con este ID: ${id_item}`

        const toast = new bootstrap.Toast(toastLiveExample_danger)

        toast.show()

    } else { 

        try {
            const respuesta = await fetch(`http://127.0.0.1:8000/product_and_services/obtener_item/${id_item}/`)
    
            if (respuesta.status === 200){
    
                const tbbody = document.getElementById('tbbody')
                const datos = await respuesta.json()
    
                if (datos.tipo == 1) { // Servicio
                    var new_content =`
                                    <th scope="row">${datos.codigo}</th>
                                    <td class="text-start text-capitalize">${datos.nombre}<input type="hidden" name="detalle" id="${datos.nombre}"></td>
                                    <td>${datos.precio}</td>
                                    <td><input type="number" name="cant" class="form-control" value="1" style="width:80%;"></td>
                                    <td>${Number(datos.precio*datos.impuesto).toFixed(2)}</td>
                                    <td>${(Number(datos.precio)+Number(datos.precio*datos.impuesto)).toFixed(2)}</td>
                                    <td>
                                        <button class="btn btn-sm btn-danger" onClick=eliminarFila(this)>
                                            <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" style="fill:#FFF"><path d="M7 21q-.825 0-1.412-.587Q5 19.825 5 19V6H4V4h5V3h6v1h5v2h-1v13q0 .825-.587 1.413Q17.825 21 17 21ZM17 6H7v13h10ZM9 17h2V8H9Zm4 0h2V8h-2ZM7 6v13Z"/></svg>
                                        </button>
                                        <button class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
                                            <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" style="fill:#FFF"><path d="M8 17q.425 0 .713-.288Q9 16.425 9 16t-.287-.713Q8.425 15 8 15t-.713.287Q7 15.575 7 16t.287.712Q7.575 17 8 17Zm0-4q.425 0 .713-.288Q9 12.425 9 12t-.287-.713Q8.425 11 8 11t-.713.287Q7 11.575 7 12t.287.712Q7.575 13 8 13Zm0-4q.425 0 .713-.288Q9 8.425 9 8t-.287-.713Q8.425 7 8 7t-.713.287Q7 7.575 7 8t.287.712Q7.575 9 8 9Zm3 8h6v-2h-6Zm0-4h6v-2h-6Zm0-4h6V7h-6ZM5 21q-.825 0-1.413-.587Q3 19.825 3 19V5q0-.825.587-1.413Q4.175 3 5 3h14q.825 0 1.413.587Q21 4.175 21 5v14q0 .825-.587 1.413Q19.825 21 19 21Zm0-2h14V5H5v14ZM5 5v14V5Z"/></svg>
                                        </button>
                                    </td>
                                `
    
                    tbbody.insertRow(-1).innerHTML= new_content
    
                    calcula_subtotal()
                    calcula_total()
    
                } else { // Articulo
    
                    var new_content =`
                                <th scope="row">${datos.codigo}</th>
                                <td class="text-start text-capitalize">${datos.nombre}</td>
                                <td>${datos.precio}</td>
                                <td><input type="number" name="cant" class="form-control" value="1" style="width:80%;"></td>
                                <td>${Number(datos.precio*datos.impuesto).toFixed(2)}</td>
                                <td>${(Number(datos.precio)+Number(datos.precio*datos.impuesto)).toFixed(2)}</td>
                                <td>
                                    <button class="btn btn-sm btn-danger" onClick=eliminarFila(this)>
                                        <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" style="fill:#FFF"><path d="M7 21q-.825 0-1.412-.587Q5 19.825 5 19V6H4V4h5V3h6v1h5v2h-1v13q0 .825-.587 1.413Q17.825 21 17 21ZM17 6H7v13h10ZM9 17h2V8H9Zm4 0h2V8h-2ZM7 6v13Z"/></svg>
                                    </button>
                                </td>
                            `

                    tbbody.insertRow(-1).innerHTML= new_content

                    calcula_subtotal()
                    calcula_total()
                
                }
    
                input_id_item.value= ''
                input_id_item.focus()
               
            } else if (respuesta.status === 404) {
    
                toastBody_danger.textContent = `No existe un item con este ID: ${id_item}`
    
                const toast = new bootstrap.Toast(toastLiveExample_danger)
                
                toast.show()
            }
    
        } catch (error) {
    
            toastBody_danger.textContent = `Ha ocurrido un error.`
    
            const toast = new bootstrap.Toast(toastLiveExample_danger)
            
            toast.show()
    
            console.log(error)
        }

    }

})

const tabla = document.getElementById('tbbody')
tabla.addEventListener('input', async (element) => {// AGREGA UN EVENTLISTENER INPUT AL PADRE PARA QUE LOS HIJOS LO HEREDEN
    if (element.target && element.target.tagName === 'INPUT' && element.target.name === 'cant') { // Se valida que el elemento que haya disparado el evento sea el input con el name=cant
        
        cell= element.target.parentElement // Obtengo la celda donde esta el input
        row= cell.parentElement // Obtengo la fila que corresponde a la celda

        var item = tabla.rows[row.rowIndex-1].cells[0].innerHTML
        var preciound = tabla.rows[row.rowIndex-1].cells[2].innerHTML
        var cantidad = element.target.value
        var impuesto= await calcular_impuesto_parcial(item, cantidad)
        var monto = calcular_monto_parcial(preciound, cantidad, impuesto)

        tabla.rows[row.rowIndex-1].cells[4].innerHTML= impuesto
        tabla.rows[row.rowIndex-1].cells[5].innerHTML= monto

        calcula_subtotal()
        calcula_total()
    }
    
})

const inputdescuento = document.getElementById('inputDescuento')
inputdescuento.addEventListener('change', (element) => {
    element.target.value = Number(element.target.value).toFixed(2)
    calcula_subtotal()
    calcula_total()
})

const btnGuardarCotizacion = document.getElementById('btnGuardarCotizacion')
btnGuardarCotizacion.addEventListener('click', () => {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const toastLiveExample_success = document.getElementById('liveToast_success')
    const toastBody_success = toastLiveExample_success.querySelector('.toast-body')
    const toastLiveExample_danger = document.getElementById('liveToast_danger')
    const toastBody_danger = toastLiveExample_danger.querySelector('.toast-body')

    if (tabla.children.length > 0){

        // Elemento HTML
        const csrftoken = getCookie('csrftoken');
        const input_noCotizacion = document.getElementById('inputNoCotizacion')
        const input_id_cliente = document.getElementById('id_id_cliente')
        const input_cliente = document.getElementById('id_nombre_cliente')
        const input_descuento = document.getElementById('inputDescuento')

        if (input_noCotizacion.value == ''){ // Si no hay un numero de cotizacion se crea la nueva cotizacion.
            
            let encabezado = {'id_cliente':input_id_cliente.value, 'nombre_cliente':input_cliente.value, 'descuento':input_descuento.value}

            let detalle = []

            for(let r = 0; r < tabla.rows.length; r++){
            
                detalle.push({'id_item':tabla.rows[r].cells[0].innerHTML, 'cantidad':tabla.rows[r].cells[3].firstChild.value})
            }

            const data = JSON.stringify({'encabezado':encabezado, 'detalle':detalle})

            const request = new Request(
                'http://127.0.0.1:8000/sales_point/gestion_cotizaciones/crear_cotizacion/',
                {headers: {'X-CSRFToken': csrftoken}}
            );
            
            try {
                fetch(request, {
                    method: 'POST',
                    body: data,
                    mode: 'same-origin'  // Do not send CSRF token to another domain.
                }).then(async function(response) {

                    if (response.status === 200){

                        const data_response = await response.json()
                        
                        const btn_imprimir = document.getElementById('btn_imprimir')
                        const input_fecha = document.getElementById('inputFecha')
                        const input_hora = document.getElementById('inputHora')

                        input_noCotizacion.value= data_response.NoCotizacion
                        input_fecha.value= data_response.fecha
                        input_hora.value= data_response.hora

                        btn_imprimir.classList.remove('disabled')

                        const myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('exampleModal'))
                        myModal.hide()

                        toastBody_success.textContent = `La cotización ha sido creada: ${data_response.NoCotizacion}`

                        const toast = new bootstrap.Toast(toastLiveExample_success)
                        
                        toast.show()

                    } else {

                        const myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('exampleModal'))
                        myModal.hide()

                        toastBody_danger.textContent = `Ha ocurrido un error: ${response.error}`

                        const toast = new bootstrap.Toast(toastLiveExample_danger)
                        
                        toast.show()
                    }
                })
            } catch(error){
                const myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('exampleModal'))
                myModal.hide()

                toastBody_danger.textContent = `Ha ocurrido un error.`

                const toast = new bootstrap.Toast(toastLiveExample_danger)
                
                toast.show()

                console.log(error)
            }

        } else { // Si existe un numero de cotizacion entonces se modifica la cotizacion existente.

            let encabezado = {
                            'noCotizacion':input_noCotizacion.value,
                            'id_cliente':input_id_cliente.value,
                            'nombre_cliente':input_cliente.value,
                            'descuento':input_descuento.value,
                            }

            let detalle = []

            for(let r = 0; r < tabla.rows.length; r++){
            
                detalle.push({'id_item':tabla.rows[r].cells[0].innerHTML, 'cantidad':tabla.rows[r].cells[3].firstChild.value})
            }

            const data = JSON.stringify({'encabezado':encabezado, 'detalle':detalle})

            const request = new Request(
                'http://127.0.0.1:8000/sales_point/gestion_cotizaciones/modificar_cotizacion/',
                {headers: {'X-CSRFToken': csrftoken}}
            );
            
            try {
                fetch(request, {
                    method: 'POST',
                    body: data,
                    mode: 'same-origin'  // Do not send CSRF token to another domain.
                }).then(async function(response) {

                    if (response.status === 200){

                        const data = await response.json()

                        const myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('exampleModal'));
                        myModal.hide();

                        toastBody_success.textContent = 'La cotización ha sido modificada.'

                        const toast = new bootstrap.Toast(toastLiveExample_success)
                        
                        toast.show()

                    } else {

                        const myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('exampleModal'));
                        myModal.hide();

                        toastBody_danger.textContent = 'Ha ocurrido un error, la cotización no ha sido modificada.'

                        const toast = new bootstrap.Toast(toastLiveExample_danger)
                        
                        toast.show()

                    }
                });
            } catch (error){
                const myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('exampleModal'))
                myModal.hide()

                toastBody_danger.textContent = `Ha ocurrido un error.`

                const toast = new bootstrap.Toast(toastLiveExample_danger)
                
                toast.show()

                console.log(error)
            }
        }

    } else {

        toastBody_danger.textContent = 'No hay ningún item para cotizar, por favor agregue al menos uno.'

        const toast = new bootstrap.Toast(toastLiveExample_danger)
        
        toast.show()
    }
})

