from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from hashlib import sha256
from .models import Usuario, ImgUsuario


def home(request):
    
    return render(request, 'home.html')

def reserva(request):

    return render(request, 'reserva.html')

def contato(request):

    return render(request, 'contato.html')

def login(request):
    if request.method == 'GET':
        # if request.user.is_authenticated:
        #     return redirect(reverse('home'))
        
        status = request.GET.get('status')
        return render(request, 'login.html', {'status':status})
    
    elif request.method == 'POST':
        try:
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            nova_senha = sha256(senha.encode()).hexdigest()
            user = Usuario.objects.get(email=email)

            if user:
                if user.senha == nova_senha:
                   
                
                    request.session['user'] = user.id
                    #return redirect(f'home/?id_usuario={request.session["user"]}')
                    return redirect(reverse('perfil'))
                    #return HttpResponse('usuario ou senha invalidos')
                return redirect(f'/mega_lanches/login/?status=1')
            return redirect(f'/mega_lanches/register/?status=2')
        except:
            return redirect(f'/mega_lanches/register/?status=2')
        
def register(request):
    
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastro_usuario.html', {'status': status})
    
    elif request.method == 'POST':
        
        imagem = request.FILES.get('img_perfil')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')


        #verificar se usuario ja existe
        user = Usuario.objects.filter(email=email).first()
        
        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect(f'/mega_lanches/register/?status=3')
        
        if len(senha.strip()) <8:
            return redirect(f'/mega_lanches/register/?status=4')
        
        if user:
            #TODO: redirecionar para pagina de cadastro com message do django
            return redirect(f'/mega_lanches/register/?status=5')
        
        try:
            senha_criptografada = sha256(senha.encode()).hexdigest()
            user = Usuario(nome = nome, email = email, cpf = cpf, senha = senha_criptografada)
            user.save()
            request.session['user'] = user.id
            return HttpResponse('login ok')
        except:

            return redirect(f'/mega_lanches/register/?status=6')


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))