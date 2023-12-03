from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from blog.forms import CommentPostForm, PostForm
from blog.models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.filter(published=True)


class EditPost(View):
    def post(self, request, slug):
        new_title = request.POST.get("newTitle")
        new_content = request.POST.get("newContent")

        post = get_object_or_404(Post, slug=slug)
        post.title = new_title
        post.content = new_content
        post.slug = slugify(new_title)
        post.save()

        return HttpResponseRedirect(reverse("blog:detail", args=(post.slug, )))


class DeletePost(DeleteView):
    model = Post
    success_url = "/"


class PostDetail(View):
    form_class = CommentPostForm
    template_name = "blog/detail.html"

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, self.template_name, context={
            "post": post,
            "form": self.form_class(),
            "comments": post.comments.all()
        })

    def post(self, request, slug):
        user = request.user
        post = get_object_or_404(Post, slug=slug)
        if user.is_authenticated:
            form = self.form_class(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = user
                comment.post = post
                comment.save()
            else:
                print(f"Error: {form.errors}")

        return HttpResponseRedirect(reverse("blog:detail", args=(slug, )))


class NewPostView(LoginRequiredMixin, View):
    form_class = PostForm
    template_name = "blog/new_post.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={
            "form":form
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.author = request.user
            new_post.save()

            return HttpResponseRedirect(reverse("blog:detail", args=(new_post.slug, )))
        

class SearchView(View):
    model = Post
    template_name = "blog/index.html"

    def get(self, request):
        query = request.GET.get("q").strip().lower()
        return render(request, self.template_name, context={
            "post_list": Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        })