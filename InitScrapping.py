# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# +
'''HTML Analysis'''

url = 'https://www.vizedex.com/'
response = requests.get(url)
# If while printing response you get 200, it means that the code went through



# +
'''Text Parsing'''

# Next we parse the html with BeautifulSoup so that we can work with a nicer, nested BeautifulSoup data structure.
soup = BeautifulSoup(response.text, “html.parser”)
soup.findAll('a')
