from django.shortcuts import render


def homePageView(response):
  return render(response, "dashboard/dashboard.html", {})
