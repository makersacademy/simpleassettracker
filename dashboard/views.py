from django.shortcuts import render, redirect

def homePageView(response):
  return render(response, "dashboard/dashboard.html", {})