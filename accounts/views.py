from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, FormView, ListView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(title='Homepage')


# class LoginView(FormView):
#     template_name = ''
#
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(title='Homepage')
#
#
# class LogoutView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(title='Homepage')
