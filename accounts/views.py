from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import SignUpForm


# Create your views here.
# @login_required
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(title='Homepage')


def SignUp(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = SignUpForm

    return render(request, 'accounts/register.html', {'user_form': user_form})
