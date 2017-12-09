from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse

class IndexView(TemplateView):
    template_name = "index.html"

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"



class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)