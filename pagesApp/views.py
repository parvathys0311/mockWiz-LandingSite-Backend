from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect

# Create your views here.
from expertApp.forms import Expertform
from expertApp.models import Expert


def index(request):
    if request.method == 'POST':
        submittedForm = Expertform(request.POST)
        if submittedForm.is_valid():
            data = submittedForm.cleaned_data
            # save form
            submittedForm.save()
            # display success message for user
            messages.success(request, 'Thanks for submitting the form. We will be in touch with you shortly.')

            createdExpertEmail = submittedForm['email'].value()
            createdExpert = Expert.objects.filter(email=createdExpertEmail)
            

            # send confirmation email to expert on successful form submission
            name = createdExpert[0].firstName
            email = createdExpert[0].email
            try:
                email = EmailMessage(
                    'Welcome to MockWiz',
                    f'Hi {name},\n\nThanks for your interest in MockWiz. We will contact you soon regarding the next steps.\n\nTo ensure you don’t miss out on any important messages, please add us to your contact list.\n\nRegards,\nMockWiz Team',
                    'hello@mockwiz.com',
                    [email],
                    ['hello@mockwiz.com']
                )
                email.send(fail_silently=False)

            except Exception:
                pass
            return redirect('index')
        else:
            return render(request, "pages/index.html", {'form': submittedForm})
    else:
        form = Expertform()
        return render(request, "pages/index.html",{'form': form})

def tc(request):
    return render(request, "pages/T&C.html")