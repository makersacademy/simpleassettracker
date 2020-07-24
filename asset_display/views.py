from django.shortcuts import render, redirect

# Create your views here.
def show_assets(response):
    return render(response, "asset_display/asset_display.html", {})