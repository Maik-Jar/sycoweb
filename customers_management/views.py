from django.shortcuts import render, redirect, get_object_or_404
from .models import TipoDocumento, Cliente, TipoCliente
from .forms import FormCrearTipoDocumento, FormModificarTipoDocumento, FormCrearTipoCliente, FormModificarTipoCliente, FormCrearClienteEmpresa, FormCrearClientePersona, FormModificarClienteEmpresa, FormModificarClientePersona
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def gestion_tipodocumento(request):

    if request.method == 'GET':

        tipodocumento= Paginator(TipoDocumento.objects.all().order_by('id'), 10)

        if request.GET.get('page'):

            page_number= request.GET.get('page')

            tipodocumento_page= tipodocumento.get_page(page_number)
        
            return render(request, 'gestion_documentos.html',
            {'tipodocumentos': tipodocumento_page,
            'form':FormModificarTipoDocumento}
            )

        else:

            tipodocumento_page= tipodocumento.get_page(1)
        
            return render(request, 'gestion_documentos.html',
            {'tipodocumentos': tipodocumento_page,
            'form':FormModificarTipoDocumento}
            )

@login_required
def crear_tipodocumento(request):

    if request.method == 'GET':

        return render(request, 'formulario_crear_tipo_documento.html', {'form': FormCrearTipoDocumento})

    else:

        formcreartipodocumento = FormCrearTipoDocumento(request.POST)

        if formcreartipodocumento.is_valid():

            formcreartipodocumento.save()

            return redirect('gestion tipo documento')

        else:

            return render(request, 'formulario_crear_tipo_documento.html',
                        {'form': formcreartipodocumento,
                        'error':'Formulario invalido, no se ha podido crear el tipo de documento.'}
                        )

@login_required
def modificar_tipodocumento(request, idtipodocumento):

    if request.method == 'GET':

        tipodocumento= get_object_or_404(TipoDocumento, pk= idtipodocumento)

        formmodificartipodocumento= FormModificarTipoDocumento(instance=tipodocumento)

        return render(request, 'formulario_modificar_tipo_documento.html', {'form':formmodificartipodocumento})

    else:

        tipodocumento= get_object_or_404(TipoDocumento, pk= idtipodocumento)

        formmodificartipodocumento= FormModificarTipoDocumento(request.POST, instance=tipodocumento )

        if formmodificartipodocumento.is_valid():

            formmodificartipodocumento.save()

            return render(request, 'formulario_modificar_tipo_documento.html', 
                            {'form':formmodificartipodocumento,
                            'success':'El tipo de documento ha sido modificado.'}
                        )

        else:
            return render(request, 'formulario_modificar_tipo_documento.html',
                            {'form': formmodificartipodocumento,
                            'error':'Formulario invalido, no se ha podido realizar los cambios.'
                            }
                        )

@login_required
def eliminar_tipo_documento(request, idtipodocumento):

    if request.method == 'POST':

        tipodocumento= get_object_or_404(TipoDocumento, pk= idtipodocumento)
        tipodocumento.delete()
        return redirect('gestion tipo documento')

@login_required
def gestion_tipo_cliente(request):

    if request.method == 'GET':

        tipo_cliente= Paginator(TipoCliente.objects.all().order_by('id'), 10)

        if request.GET.get('page'):

            page_number= request.GET.get('page')

            tipo_cliente_page= tipo_cliente.get_page(page_number)
        
            return render(request, 'gestion_tipo_clientes.html',
                            {'tipoclientes': tipo_cliente_page,
                             'form': FormCrearTipoCliente}
                        )

        else:

            tipo_cliente_page= tipo_cliente.get_page(1)

            return render(request, 'gestion_tipo_clientes.html',
                            {'tipoclientes': tipo_cliente_page,
                             'form': FormCrearTipoCliente}
                        )

@login_required
def crear_tipo_cliente(request):

    if request.method == 'GET':

        return render(request, 'formulario_crear_tipo_cliente.html', {'form':FormCrearTipoCliente})

    else:

        formulario_tipo_cliente= FormCrearTipoCliente(request.POST)

        if formulario_tipo_cliente.is_valid():

            formulario_tipo_cliente.save()

            return redirect('gestion tipo cliente')

        else:

            return render(request, 'formulario_crear_tipo_cliente.html',                               {'form':formulario_tipo_cliente,
                'error':'Formularion invalido, no se ha podido crear tipo de cliente.'
            })

@login_required
def modificar_tipo_cliente(request, idtipo_cliente):

    if request.method == 'GET':

        tipo_cliente= get_object_or_404(TipoCliente, pk= idtipo_cliente)

        form_modificar_tipo_cliente= FormModificarTipoCliente(instance=tipo_cliente )

        return render(request, 'formulario_modificar_tipo_cliente.html', {'form':form_modificar_tipo_cliente})

    else:

        tipo_cliente= get_object_or_404(TipoCliente, pk= idtipo_cliente)

        form_modificar_tipo_cliente= FormModificarTipoCliente(request.POST, instance=tipo_cliente )

        if form_modificar_tipo_cliente.is_valid():

            form_modificar_tipo_cliente.save()

            return render(request, 'formulario_modificar_tipo_cliente.html', 
                            {'form':form_modificar_tipo_cliente,
                            'success':'El tipo de cliente ha sido modificado.'}
                        )

        else:

            return render(request, 'formulario_modificar_tipo_cliente.html',
                    {'form': form_modificar_tipo_cliente,
                    'error':'Formulario invalido, no se ha podido realizar los cambios.'
                    }
            )

@login_required
def eliminar_tipo_cliente(request, idtipo_cliente):

     if request.method == 'POST':

        tipo_cliente= get_object_or_404(TipoCliente, pk= idtipo_cliente)
        tipo_cliente.delete()
        return redirect('gestion tipo cliente')

@login_required
def gestion_clientes(request):

    if request.method == 'GET':

        cliente= Paginator(Cliente.objects.all().order_by('id'), 10)

        if request.GET.get('page'):

            page_number= request.GET.get('page')

            cliente_page= cliente.get_page(page_number)
        
            return render(request, 'gestion_clientes.html',
                            {'clientes': cliente_page,
                             'form': FormCrearClientePersona}
                        )

        else:

            cliente_page= cliente.get_page(1)

            return render(request, 'gestion_clientes.html',
                            {'clientes': cliente_page,
                             'form': FormCrearClientePersona}
                        )

@login_required
def crear_cliente(request):

    if request.method == 'GET':
        
        if request.GET.get('clientType'):

            tipo_de_cliente = int(request.GET.get('clientType'))

            if tipo_de_cliente == 2:
                return render(request, 'formulario_crear_cliente.html', {'form':FormCrearClientePersona})

            else:
                return render(request, 'formulario_crear_cliente.html', {'form':FormCrearClienteEmpresa(initial= {'tipo':1, 'tipo_documento':4})})

        else:
            return render(request, 'formulario_crear_cliente.html', {'form':FormCrearClientePersona(initial= {'tipo':2, 'tipo_documento':1})})

    else:
        try:
            tipo_de_cliente = int(request.POST.get('tipo'))

            if tipo_de_cliente == 1: # Es una Empresa.
                form_crear_cliente = FormCrearClienteEmpresa(request.POST)

                if form_crear_cliente.is_valid():
                    form_crear_cliente.save()
                    return redirect('gestion clientes')

                else: 
                    form_cliente = FormCrearClienteEmpresa(request.POST)
                    return render(request, 'formulario_crear_cliente.html',
                                {'form':form_cliente,
                                'error':'No se ha podido crear el cliente, error: %s.' %(form_cliente.errors.as_text())}
                                )

            else: # Es una Persona.

                form_crear_cliente = FormCrearClientePersona(request.POST)

                if form_crear_cliente.is_valid():
                    form_crear_cliente.save()
                    return redirect('gestion clientes')

                else: 
                    form_cliente = FormCrearClientePersona(request.POST)
                    return render(request, 'formulario_crear_cliente.html',
                                {'form':form_cliente,
                                'error':'No se ha podido crear el cliente, error: %s.' %(form_cliente.errors.as_text())}
                                )

        except Exception as error: 
        
            return render(request, 'formulario_crear_cliente.html',
                                  {'form':'',
                                  'error':'No se ha podido crear el cliente. error %s.' %(error)}
                        )

@login_required
def modificar_cliente(request, id_cliente):

    if request.method == 'GET':

        cliente = get_object_or_404(Cliente, pk= id_cliente)

        if cliente.tipo == 1: # Empresa

            form_modificar_cliente_empresa = FormModificarClienteEmpresa(instance= cliente)

            return render(request, 'formulario_modificar_cliente.html', {'form':form_modificar_cliente_empresa})

        else:

            form_modificar_cliente_persona = FormModificarClientePersona(instance= cliente)

            return render(request, 'formulario_modificar_cliente.html', {'form':form_modificar_cliente_persona})

    else:

        cliente= get_object_or_404(Cliente, pk= id_cliente)

        if cliente.tipo == 1: # Empresa

            form_modificar_cliente_empresa = FormModificarClienteEmpresa(request.POST, instance= cliente)

            if form_modificar_cliente_empresa.is_valid():

                form_modificar_cliente_empresa.save()

                return render(request, 'formulario_modificar_cliente.html', 
                              {'form':form_modificar_cliente_empresa,
                               'success':'El cliente ha sido modificado.'}
                            )

            else:

                return render(request, 'formulario_modificar_cliente.html', 
                              {'form':form_modificar_cliente_empresa,
                               'error':'No se ha podido modificar el cliente. Error: %s.' %(form_modificar_cliente_empresa.errors.as_text())}
                            )

        else: # Persona

            form_modificar_cliente_persona = FormModificarClientePersona(request.POST, instance= cliente)

            if form_modificar_cliente_persona.is_valid():

                form_modificar_cliente_persona.save()

                return render(request, 'formulario_modificar_cliente.html', 
                              {'form':form_modificar_cliente_persona,
                               'success':'El cliente ha sido modificado.'}
                            )

            else:

                return render(request, 'formulario_modificar_cliente.html', 
                              {'form':form_modificar_cliente_persona,
                               'error':'No se ha podido modificar el cliente. Error: %s.' %(form_modificar_cliente_persona.errors.as_text())}
                            )

@login_required
def eliminar_cliente(request, id_cliente):

    if request.method == 'POST':

        cliente = get_object_or_404(Cliente, pk= id_cliente)
        cliente.delete()
        return redirect('gestion clientes')