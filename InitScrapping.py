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

# ## VizEd Website Scrapping
# This analysis is used to test how many information are exploitable through Web Scrapping on our StartUp Website
# Author: Matteo Gevi
# Property: VizEd UG

import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup
