from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountApp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("input_text")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountApp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountApp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountApp/create.html'