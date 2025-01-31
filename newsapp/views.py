from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsPost
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import NewsPostForm
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

class IndexView(ListView):

    template_name = 'index.html'

    context_object_name = 'orderby_records'

    queryset = NewsPost.objects.order_by('-posted_at')

    paginate_by = 4

class NewsDetail(DetailView):
    template_name ='post.html'
    model = NewsPost

class SeiziView(ListView):
    template_name='seizi.html'#サイエンス
    model = NewsPost
    context_object_name = 'seizi_records'
    queryset = NewsPost.objects.filter(
        category='seizi').order_by('-posted_at')
    paginate_by = 2

class SportsView(ListView):
    template_name='sports.html'#ダイアリーライフ
    model = NewsPost
    context_object_name = 'sports_records'
    queryset = NewsPost.objects.filter(
        category='sports').order_by('-posted_at')
    paginate_by = 2

class TenkiView(ListView):
    template_name='tenki.html'#music
    model = NewsPost
    context_object_name = 'tenki_records'
    queryset = NewsPost.objects.filter(
        category='tenki').order_by('-posted_at')
    paginate_by = 2

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('newsapp:login')
    template_name = 'signup.html'


# トップページに投稿一覧を表示
def post_list(request):
    posts = NewsPost.objects.all().order_by('-posted_at')
    return render(request, 'index.html', {'orderby_records': posts})

# 記事の投稿
def post_create(request):
    if request.method == "POST":
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsapp:index')
    else:
        form = NewsPostForm()
    return render(request, 'post_create.html', {'form': form})

#    """記事の削除
def post_delete(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('newsapp:index')  # 削除後はトップページにリダイレクト
    return render(request, 'post_delete.html', {'post': post})