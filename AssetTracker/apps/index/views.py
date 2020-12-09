from django.shortcuts import render, redirect

def index_page_view(response):
  return render(response, "index/index.html", {})
