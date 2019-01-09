from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from posts.models import Post


class PostListView(ListView):
	template_name = "home_page.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Post.objects.all()