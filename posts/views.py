from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from .forms import PostForm, CommentForm


# def home(request):
# 	return render(request, "base.html")

def post_list(request):
	posts = Articles.objects.all()
	return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Articles, pk=pk)
	return render(request, 'post_detail.html', {'post': post})

# @login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.timestamp = timezone.now()            
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: 
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

# @login_required
def post_edit(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.timestamp = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

# @login_required
def post_remove(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    post.delete()
    return redirect('post_list')

	
def add_comment_to_post(request, pk):
	post = get_object_or_404(Articles, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.id = pk
			comment.post = post
			comment.user = request.user
			comment.timestamp = timezone.now()            
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'add_comment_to_post.html', {'form': form})
