from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from cita.models import Cita
from especialidades.models import Especialidades
from medico.models import Medico
from paciente.models import Paciente
from .tokens import generate_token
from hospital import settings
from django.db.models import Count



# Create your views here.
def inicio(request):
    return render(request, 'landing/inicio.html')

def crearcuenta(request):
    if request.method == "POST":
        print('REGISTRO POST...')
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if User.objects.filter(username=username):
            messages.error(request, "¡El nombre de usuario ya existe! Por favor intenta con otro.")
            return redirect('iniciosesion')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "¡El correo electrónico ya está registrado!")
            return redirect('iniciosesion')
        
        if len(username) > 20:
            messages.error(request, "¡El nombre de usuario debe tener menos de 20 caracteres!")
            return redirect('iniciosesion')
        
        if pass1 != pass2:
            messages.error(request, "¡Las contraseñas no coinciden!")
            return redirect('iniciosesion')
        
        if not username.isalnum():
            messages.error(request, "¡El nombre de usuario debe ser alfanumérico!")
            return redirect('iniciosesion')
        
        #almacena recién los datos
        myuser = User.objects.create_user(username, email, pass1)
        myuser.fname = fname
        myuser.lname = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "¡Tu cuenta ha sido creada exitosamente! Por favor revisa tu correo electrónico para confirmar tu dirección de correo y activar tu cuenta.")

        #guardar en tabla paciente
        paciente = Paciente.objects.create(
            nombre_completo = fname + lname,
            user_id_id = myuser.id
        )
        
        # Welcome Email
        subject = "Bienvenido Hospital Isidro Ayora"
        message = "Hola " + myuser.first_name + "!! \n" + "Confirma tu cuenta"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirma tu correo!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        send_mail(email_subject, message2, from_email, to_list, fail_silently=True)
        
        return redirect('crearcuenta')
        
        
    return render(request, "landing/sign-up.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Tu cuenta ha sido activada")
        return redirect('crearcuenta')
    else:
        return render(request,'activation_failed.html')
    
def iniciosesion(request):
    if request.method == "POST":
        logout(request)
        
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            username = user.username
            
            url_redirect = ''
            
            if(user.is_superuser == True):
                request.session['tipo_usuario'] = 'Admin'
                #url_redirect = 'landing/dashboard_admin.html'
                return redirect('dashboard_admin')
            else:
                paciente = Paciente.objects.filter(user_id=user.id)
                
                if(paciente.exists()):
                    request.session['tipo_usuario'] = 'Paciente'
                    request.session['id_paciente'] = paciente.first().id
                    #url_redirect = 'paciente/dashboard_paciente.html'
                    return redirect('dashboard_paciente')
                    
                medico = Medico.objects.filter(user_id=user.id)
                
                if(medico.exists()):
                    request.session['tipo_usuario'] = 'Medico'
                    print(medico.first())
                    request.session['id_medico'] = medico.first().id
                    #url_redirect = 'medico/dashboard_medico.html'
                    return redirect('dashboard_medico')
            
            return render(request,url_redirect ,{'username' : username})

        else:
            messages.error(request, "Error en las credenciales")
            return redirect("crearcuenta")
    return render(request, "landing/sign-in.html")

def signout(request):
    logout(request)
    messages.success(request, "Inicio de sesión cerrado")
    return redirect("inicio")


def dashboard_admin(request):
    # Obtener el total de médicos activos e inactivos
    total_medicos_activos = Medico.objects.filter(estado="Activo").count()
    total_medicos_inactivos = Medico.objects.filter(estado="Dado de baja").count()

    # Obtener el total de pacientes con y sin COVID
    total_pacientes_covid = Cita.objects.filter(estado_covid="s").count()
    total_pacientes_no_covid = Cita.objects.filter(estado_covid="n").count()
    
    # Obtener el total de especialidades y su distribución
    total_especialidades = Especialidades.objects.count()
    especialidades_data = Especialidades.objects.annotate(total=Count('medico'))

    # Obtener otros contadores
    contador_pacientes = Paciente.objects.count()
    contador_citas = Cita.objects.count()
    
    #contados de citas atendidas y citas no atendidas
    total_citas_atendidas = Cita.objects.filter(atendida=True).count()
    total_citas_no_atendidas = Cita.objects.filter(atendida=False).count()


    # Crear el contexto combinado
    context = {
        'section': 'dashboard_medico',
        'total_medicos_activos': total_medicos_activos,
        'total_medicos_inactivos': total_medicos_inactivos,
        'total_pacientes_covid': total_pacientes_covid,
        'total_pacientes_no_covid': total_pacientes_no_covid,
        'contador_pacientes': contador_pacientes,
        'contador_citas': contador_citas,
        'total_especialidades': total_especialidades,
        'especialidades_data': list(especialidades_data),  # Convertir a lista para facilitar su uso en JavaScript
        'total_citas_atendidas': total_citas_atendidas,
        'total_citas_no_atendidas': total_citas_no_atendidas,
        
    }

    # Renderizar la plantilla con el contexto
    return render(request, 'landing/dashboard_admin.html', context)



from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def login_required_and_check_session(variable_name, expected_value):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            # Verificar si la variable de sesión tiene el valor esperado
            if request.session.get(variable_name) != expected_value:
                return HttpResponseForbidden("No tienes permisos para acceder a esta página.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator