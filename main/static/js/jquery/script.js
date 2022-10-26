$(document).ready(function(){

    $('#btinformacion').click(function(){

        var fila = $(this).parent();
        var id = fila.siblings("th:eq(0)").text();

        var token = $('body > div > div > main > input[type=hidden]').val();

        $.ajaxSetup({
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        });

        $.ajax({
            
            type: 'POST',
            data: {json: JSON.stringify({impuestoid:id, codigo:1})},
            dataType: 'json',
            success: function(respuesta){
                if ($('#modal-body').find('#form_impuesto').length) {
                    //$('#form_impuesto').replaceWith(respuesta);
                    $(' #form_impuesto').load(respuesta['data']);
                } else {
                    $('#modal-body').append(respuesta);
                }
                },
            error: function(error){
                    //codigo error
                    console.log(error);
                    
                }
        });
        
    });

});