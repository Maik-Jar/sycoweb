const btbuscar = document.getElementById('btbuscarcliente')
btbuscar.addEventListener('click', async () => {

    const input_tipo_documento = document.getElementById('id_tipo_documento')
    const input_documento_cliente = document.getElementById('id_documento_cliente')

    var id_tipo_documento = input_tipo_documento.value
    var no_documento = input_documento_cliente.value

    try {

        const respuesta = await fetch(`http://127.0.0.1:8000/customers_management/obtener_cliente/${id_tipo_documento}/${no_documento}/`)

        if (respuesta.status === 200){
            const input_cliente = document.getElementById('id_nombre_cliente')
            const input_telefono = document.getElementById('id_telefono_cliente')

            const datos = await respuesta.json()

            input_cliente.value= datos.fullname
            input_telefono.value= datos.telefono

        } else if (respuesta.status === 404) {

            const toastLiveExample = document.getElementById('liveToast')

            const toastBody = toastLiveExample.querySelector('.toast-body')
            toastBody.textContent = `No existe un cliente con el documento No. ${no_documento}`

            const toast = new bootstrap.Toast(toastLiveExample)
            
            toast.show()
        }

    } catch(error){
        const toastLiveExample = document.getElementById('liveToast')

        const toastBody = toastLiveExample.querySelector('.toast-body')
        toastBody.textContent = `Ha ocurrido un error.`

        const toast = new bootstrap.Toast(toastLiveExample)
        
        toast.show()

        console.log(error)
    }
})

const btbuscaritem = document.getElementById('btbuscaritem')
btbuscaritem.addEventListener('click', async () => {

    const input_id_item = document.getElementById('id_item')

    const id_item = input_id_item.value

    try {
        const respuesta = await fetch(`http://127.0.0.1:8000/product_and_services/obtener_item/${id_item}/`)

        if (respuesta.status === 200){

            const datos = await respuesta.json()

            if (datos.tipo == 1) {
                var new_content =`
                                <th scope="row">${datos.codigo}</th>
                                <td class="text-start text-capitalize">
                                    <span class="row mx-auto align-middle">
                                        ${datos.nombre}
                                        <span class="col-sm-8 aling-items-center">
                                            <input type="text" name="detalle" id="${datos.nombre}" class="form-control form-control-sm" placeholder="Detalle">
                                        </span>
                                    </span>
                                </td>
                                <td>${datos.precio}</td>
                                <td><input type="number" name="cant" id="cant_item" class="form-control" value="1" style="width:80%;"></td>
                                <td>${Number(datos.precio*datos.impuesto).toFixed(2)}</td>
                                <td>${(Number(datos.precio)+Number(datos.precio*datos.impuesto)).toFixed(2)}</td>
                                <td>
                                    <button class="btn btn-sm btn-danger" onClick=eliminarFila(this)>
                                        <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" style="fill:#FFF"><path d="M7 21q-.825 0-1.412-.587Q5 19.825 5 19V6H4V4h5V3h6v1h5v2h-1v13q0 .825-.587 1.413Q17.825 21 17 21ZM17 6H7v13h10ZM9 17h2V8H9Zm4 0h2V8h-2ZM7 6v13Z"/></svg>
                                    </button>
                                </td>
                            `
            } else {
                var new_content =`
                                <th scope="row">${datos.codigo}</th>
                                <td class="text-start text-capitalize">${datos.nombre}</td>
                                <td>${datos.precio}</td>
                                <td><input type="number" name="cant" id="cant_item" class="form-control" value="1" style="width:80%;"></td>
                                <td>${Number(datos.precio*datos.impuesto).toFixed(2)}</td>
                                <td>${(Number(datos.precio)+Number(datos.precio*datos.impuesto)).toFixed(2)}</td>
                                <td>
                                    <button class="btn btn-sm btn-danger" onClick=eliminarFila(this)>
                                        <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" style="fill:#FFF"><path d="M7 21q-.825 0-1.412-.587Q5 19.825 5 19V6H4V4h5V3h6v1h5v2h-1v13q0 .825-.587 1.413Q17.825 21 17 21ZM17 6H7v13h10ZM9 17h2V8H9Zm4 0h2V8h-2ZM7 6v13Z"/></svg>
                                    </button>
                                </td>
                            `
            }

            const tbbody = document.getElementById('tbbody').insertRow(-1).innerHTML= new_content

            calcula_monto()

            input_id_item.value= ''
            input_id_item.focus()
           
        } else if (respuesta.status === 404) {

            const toastLiveExample = document.getElementById('liveToast')

            const toastBody = toastLiveExample.querySelector('.toast-body')
            toastBody.textContent = `No existe un item con este ID: ${id_item}`

            const toast = new bootstrap.Toast(toastLiveExample)
            
            toast.show()
        }

    } catch (error) {

        const toastLiveExample = document.getElementById('liveToast')

        const toastBody = toastLiveExample.querySelector('.toast-body')
        toastBody.textContent = `Ha ocurrido un error.`

        const toast = new bootstrap.Toast(toastLiveExample)
        
        toast.show()

        console.log(error)
    }
})

function eliminarFila(bt){
    // remover fila de la tabla
    
    const tabla = document.getElementById('tbbody')

    cell= bt.parentElement
    row= cell.parentElement
    tabla.deleteRow(row.rowIndex-1)

}

function calcula_monto(){

    var tabla = document.getElementById('tbbody')
    
    for (var r = 0; r < tabla.rows.length; r++){
        alert(tabla.rows[r].cells[5].innerHTML)
    }

}
