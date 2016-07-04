from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.dispatch import Signal
from django.core.mail import send_mail
from .models import Post
from .models import Comment
from .forms import PostForm
from .forms import CommentForm
from pkg_resources import iter_entry_points


# Register the Signal
email_signal = Signal(providing_args=['author', 'text'])


# Define a receiver method
def send_not_aproved_email_receiver(**kwargs):
    author, text = kwargs['author'], kwargs['text']

    send_mail('You have a new comment to aprove.',
              '\nThe following message needs aprove:\n\nAuthor: ' + author + '\nComment: ' + text,
              author,
              ['ruyther@me.com'],
              fail_silently=False,
              )

# Connect the receiver with the log_it
email_signal.connect(send_not_aproved_email_receiver)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    ######
    for entry_point in iter_entry_points(group='cms.plugin', name=None):
        print(entry_point)

    available_methods = []
    for entry_point in iter_entry_points(group='authkit.method', name=None):
        available_methods.append(entry_point.load())
    ######
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            email_signal.send(sender='email_sender',
                              author=comment.author,
                              text=comment.text)
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)
