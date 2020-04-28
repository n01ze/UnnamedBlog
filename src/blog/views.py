from src.blog.models import Post
from django.views import View
from django.shortcuts import render
from django.http import Http404


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        args = {'post_items': Post.objects.filter(status=1).order_by('-created_on')}
        return render(request, self.template_name, args)


class PostDetail(View):
    template_name = 'post_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            args = {'post': Post.objects.get(slug=kwargs.get('slug'))}
        except Post.DoesNotExist:
            raise Http404
        return render(request, self.template_name, args)
