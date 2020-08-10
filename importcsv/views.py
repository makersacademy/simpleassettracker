from django.shortcuts import render

# Create your views here.
def importView(response):
  return render(response, "importcsv/importcsv.html", {})