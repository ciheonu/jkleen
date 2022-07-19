from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
                From:\n\t\t{}\n
                Email:\n\t\t{}\n
                Subject:\n\t\t{}\n
                Message:\n\t\t{}\n
                '''.format(form_data['name'], form_data['email'],
                           form_data['subject'], form_data['message'])
        send_mail('You got a mail!', message, '', ['ciheonu36@gmail.com'])
        if send_mail:
            messages.success(request, f'Message sent successfully! ')
            return HttpResponseRedirect(request.path_info)
    return render(request, 'contact.html', {})
