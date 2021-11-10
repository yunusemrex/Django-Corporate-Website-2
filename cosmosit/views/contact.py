from django.shortcuts import render, redirect
from cosmosit.models.contact import Contact
from cosmosit.forms.contact import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('sent-email')
    
    return render(request, 'sections/contact-page.html', context = {
         'form':form
     })