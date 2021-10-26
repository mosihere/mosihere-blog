from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'mosihere@gmail.com', ['mostafakhoshhal@yahoo.com'])

            except BadHeaderError:

                return HttpResponse('Invalid header error found!')

            return redirect ('blog:home')
        
    
    else:
        form = ContactForm()
        context = {'form':form}
        return render(request, 'contact_us/contact.html', context)
