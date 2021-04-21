from django.shortcuts import redirect, render, resolve_url
from .forms import PhotoForm, SignUpForm, UserForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from .mixins import OnlyYouMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photo



def index(request):
    form = PhotoForm()
    context = {
        'form': form
    }
    return render(request, 'cardboardapp/index.html', context)


def predict(request):
    if not request.method == 'POST':
        return redirect('cardboardapp:index')
    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
        raise ValueError('投稿が不正です')

    # formに正しくデータが入っているか、初期のデータにimage与える、cleaned_dataでできる
    photo = Photo(image=form.cleaned_data['image'])
    predicted, percentage = photo.predict()  # 予測の値を渡す
    context = {
        'predicted': predicted,
        'percentage': percentage,
    }
    return render(request, 'cardboardapp/predict.html', context)



@login_required
def home(request):
    return render(request, 'cardboardapp/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) # UserCreationform:新しいユーザーを作成するためのModelForm
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect('cardboardapp:home')
    else:
        form = SignUpForm()
        context = {
            'form': form
        }
    return render(request, 'cardboardapp/signup.html', context)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "cardboardapp/users/detail.html"


class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = 'cardboardapp/users/update.html'
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('cardboardapp:users_detail', pk=self.kwargs['pk'])