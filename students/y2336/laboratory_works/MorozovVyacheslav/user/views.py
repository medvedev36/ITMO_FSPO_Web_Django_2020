from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import UserRegisterForm, UpdateUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = UpdateUserForm(instance=self.request.user)
        return context
    
    def post(self, *args, **kwargs):
        form = UpdateUserForm(self.request.POST, instance=self.request.user)
        if form.is_valid():
            form.save()
        return redirect('profile')