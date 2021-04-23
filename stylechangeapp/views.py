from django.shortcuts import render, redirect
from .forms import LoginForm, ImageForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import User, ModelFile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from PIL import Image
from django.conf import settings
from model import *
import subprocess


output_path = settings.BASE_DIR + "/media/documents/output.jpg" 

def top(request):
    return render(request, 'stylechangeapp/top.html')

@login_required
def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            content_image = request.FILES['content_image']
            output_path = settings.BASE_DIR + "/media/documents/output.jpg" 
            style_image = settings.BASE_DIR + "/media/documents/"
            if '1' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/candy.pth', '--output-image', output_path, '--cuda', '0'])
            elif '2' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/mosaic.pth', '--output-image', output_path, '--cuda', '0'])
            elif '3' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/rain_princess.pth', '--output-image', output_path, '--cuda', '0'])
            elif '4' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/udnie.pth', '--output-image', output_path, '--cuda', '0']) 
            elif '5' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/gohho.pth', '--output-image', output_path, '--cuda', '0'])
            elif '6' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/ginga.pth', '--output-image', output_path, '--cuda', '0'])  
            elif '7' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/pezury.pth', '--output-image', output_path, '--cuda', '0'])
            elif '8' in request.POST:
                subprocess.run(['python3', settings.BASE_DIR+'/model/neural_style.py', 'eval', '--content-image', settings.BASE_DIR+'/media/documents/'+str(content_image), 
                                '--model', settings.BASE_DIR+'/model/weight/wave.pth', '--output-image', output_path, '--cuda', '0'])             
            else:
                form = ImageForm()
                return render(request, 'stylechangeapp/index.html', {'form' : form})
            img_url = 'media/documents/output.jpg'
            return render(request, 'stylechangeapp/result.html', {'img_url' : img_url})
    else:
        form = ImageForm()
        return render(request, 'stylechangeapp/index.html', {'form' : form})

def test(request):
    return render(request, 'stylechangeapp/test.html')

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "stylechangeapp/signup.html" 
    success_url = reverse_lazy('top')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレク
# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'stylechangeapp/login.html'
    success_url = reverse_lazy('top.html')
    


class Logout(LogoutView):
    template_name = 'stylechangeapp/base.html'
    