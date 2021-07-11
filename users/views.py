from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.urls import reverse_lazy
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')

    def get_form(self):
        form = super(CustomLoginView , self).get_form()
        form.fields['username'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Username',
            'autocomplete':'false',
        }
        form.fields['password'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Password',
            'autocomplete':'false',
        }
        return form

class RegisterFormView(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(request=self.request , user=user)
        return super(RegisterFormView , self).form_valid(form)

    def get_form(self):
        form = super(RegisterFormView , self).get_form()
        form.fields['username'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Username',
            'autocomplete':'false',
        }
        form.fields['password1'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Password',
            'autocomplete':'false',
        }
        form.fields['password2'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Password confirmation',
            'autocomplete':'false',
        }
        return form
