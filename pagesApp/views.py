from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from expertApp.forms import Expertform
from expertApp.models import Expert


def index(request):
    if request.method == 'POST':
        print("entered form")
        submittedForm = Expertform(request.POST)
        if submittedForm.is_valid():
            print("form valid")
            data = submittedForm.cleaned_data
            # save form
            submittedForm.save()
            # display success message for user
            messages.success(request, 'Expert form is submitted successfully')

            createdExpertEmail = submittedForm['email'].value()
            createdExpert = Expert.objects.filter(email=createdExpertEmail)

            # send confirmation email to expert on successful form submission
            name = createdExpert[0].firstName
            email = createdExpert[0].email
            try:
                send_mail('Welcome to MockWiz', f'Hi {name}, thanks for registering with us.We will get back to you soon.',
                          'parvathys0311@gmail.com',
                          [email], fail_silently=False)
            except Exception:
                pass
            return redirect('index')
        else:
            print("Invalid")
            return render(request, "pages/index.html", {'form': submittedForm})
    else:
        form = Expertform()
        return render(request, "pages/index.html",{'form': form})