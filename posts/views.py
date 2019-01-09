from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Post


class PostDetailView(DetailView):
	template_name = "post_page.html"

	def get_object(self, *args, **kwargs):
		pk = self.kwargs.get('pk')

		instance = Post.objects.get(pk=pk)
		if instance is None:
			raise Http404("Post doesn't exist")

		return instance