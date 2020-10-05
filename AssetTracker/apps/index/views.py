from django.shortcuts import render, redirect

def indexPageView(response):
  return render(response, "index/index.html", {})
