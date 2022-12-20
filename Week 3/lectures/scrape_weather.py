import bs4
import requests

def send_request (website_url):
    return requests.get(website_url)