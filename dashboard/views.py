from django.shortcuts import render, redirect

from django.http import HttpResponse


def homePageView(response):
  return render(response, "dashboard/dashboard.html", {})