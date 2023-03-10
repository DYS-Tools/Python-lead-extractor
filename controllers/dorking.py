from flask import request, render_template, redirect,  url_for, flash, jsonify
from googlesearch import search
import re
import requests
import os
from bs4 import BeautifulSoup

class DorkingController():
    
    """Class for People controller"""
    
    # use this dorking theme with /api/objectofrequest
    def request(self,dorking):
        
        print(dorking)
        query = ' intext:gmail.com intext:"' + dorking  # dorking request 
        
        urlList = self.google_search(query)
        print(urlList) # why is empty ? 
        
        email_list = self.extract_email_in_list_url(urlList)
        print(email_list)
        
        return jsonify(email_list)
    
    
    # return list of url 
    def google_search(self,query):
        num_results = 4
        url = f"https://www.google.com/search?q={query}&num={num_results}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        # Extract links from HTML using regular expressions
        urls = re.findall(r'<a href="(https?://.*?)"', response.text)

        return urls
        
    # return array with all adresse in a url list 
    def extract_email_in_list_url(self,urlList):
        
        email_list = []
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # regex for get email in content

        # get each url in urlList
        for url in urlList:
            response = requests.get(url)
            texte = response.text
            resultats = re.findall(regex, texte)
            email_list.extend(resultats)

        return email_list