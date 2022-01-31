from django.shortcuts import redirect, render

from .forms import FormsContact

from django.core.mail import EmailMessage
# Create your views here.

def contact(request): 
    forms_contact=FormsContact()
    if request.method=='POST':
        forms_contact=FormsContact(data=request.POST)
        if forms_contact.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            content=request.POST.get('content')

            email=EmailMessage(
                'Mensaje desde App Django',
                'El usuario con el nombre{} con la dirección {} escribe lo siguiente:\n\n {}'.format(name,email,content),
                '',
                ['testfemtjah@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect('/contact/?valido')
            except:
                return redirect('/contact/?novalido')

    return render(request, 'contact.html', {'miForms':forms_contact})
