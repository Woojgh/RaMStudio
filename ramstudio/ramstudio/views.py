from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from contact.forms import ContactForm

def Home(request):
    return render(request, 'home.html')
    

def About(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['flippygonmad@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success.html')
    return render(request, 'about.html', {'form': form})

    
def Contact(request):
    return render(request, 'contact.html')


def Login(request):
    return render(request, 'login.html')

