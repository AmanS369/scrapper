
from django.shortcuts import render
from .scrape import scrape
import requests
from bs4 import BeautifulSoup

def scrape_view(request):
    scraped_data = scrape()
    return render(request, 'scrape.html', {'data': scraped_data})

