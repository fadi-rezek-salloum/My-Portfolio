from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .forms import ContactForm

class ContactView(generic.View):

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)

        if form.is_valid():
            form.save()

            messages.success(self.request, 'Your message was sent successfully! Thank you for your trust.')
            return redirect(reverse('main:index'))
        else:
            print('Error :', form.errors)
            messages.error(self.request, form.errors.as_text())
            return redirect(reverse('main:index'))