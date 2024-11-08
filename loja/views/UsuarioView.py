from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import *
def list_usuario_view(request, id=None):
    # carrega somente usuarios, não inclui os admin
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
    'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)

def edit_usuario_view(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    emailUnused = True
    message = None

    if request.method == 'POST':
        # Atribui o POST e as instâncias corretamente
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario)
        userForm = UserForm(request.POST, instance=request.user)

        # Verifica se o email está em uso
        verifyEmail = Usuario.objects.filter(user__email=request.POST.get('email')).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None

        if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
            # Salva se tudo estiver correto
            usuarioForm.save()
            userForm.save()
            message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
        else:
            # Mensagem de erro caso contrário
            if request.method == 'POST':
                if emailUnused:
                    message = { 'type': 'danger', 'text': 'Dados inválidos' }
                else:
                    message = { 'type': 'warning', 'text': 'E-mail já usado' }
    else:
        # Quando o método não for POST, só exibe os formulários
        usuarioForm = UserUsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)

    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
        'message': message
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)
