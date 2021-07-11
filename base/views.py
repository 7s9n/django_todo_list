from .models import Task
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
class Test(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().user == self.request.user

class TaskList(LoginRequiredMixin , ListView):
    model = Task
    ordering = ['-created_at']

    # def get_login_url(self) -> str:
    #     """
    #     Override this method to override the login_url attribute.
    #     or define LOGIN_URL in settings
    #     """
    #     return reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(TaskList , self).get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user = self.request.user)
        context['incomplete_count'] = context['task_list'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task_list'] = context['task_list'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context

class TaskDetail(Test , LoginRequiredMixin , DetailView):
    model = Task

class TaskCreate(LoginRequiredMixin , SuccessMessageMixin , CreateView):
    model = Task
    fields = ['title' , 'description' , 'complete']
    success_message = 'New task created successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate , self).form_valid(form)

    def get_form(self) :
        form =  super().get_form()
        form.fields['title'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Task\'s title',
        }
        form.fields['description'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Task\'s description',
        }
        form.fields['complete'].widget.attrs = {
            'class':'form-check-input col-md-6',
        }
        return form

class TaskUpdate(Test ,LoginRequiredMixin , SuccessMessageMixin , UpdateView):
    model = Task
    fields = ['title' , 'description' , 'complete']
    success_message = 'Task updated successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate , self).form_valid(form)

    def get_form(self):
        form =  super().get_form()
        form.fields['title'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Task\'s title',
        }
        form.fields['description'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Task\'s description',
        }
        form.fields['complete'].widget.attrs = {
            'class':'form-check-input col-md-6',
        }
        return form

class TaskDelete(Test ,LoginRequiredMixin , SuccessMessageMixin , DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    success_message = 'Task deleted successfully'
