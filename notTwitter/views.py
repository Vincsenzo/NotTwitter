from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Posts
from .forms import PostForm


def index(request):
    posts = Posts.objects.all()
    paginate = Paginator(posts, 10)
    page = request.GET.get('page')
    paginate_posts = paginate.get_page(page)

    context = {'paginate_posts': paginate_posts}
    return render(request, 'notTwitter/index.html', context)


@login_required
def make_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("notTwitter:index")
        
    context = {'form':form,}
    return render(request, 'notTwitter/make_post.html', context)
