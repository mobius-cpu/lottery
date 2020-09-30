#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : federal_retriever.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 19.01.2020
# Last Modified Date: 27.04.2020
# Last Modified By  : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>

import pandas as pd
import requests
from bs4 import BeautifulSoup
import random as rd
import numpy as np


# Ho to web scraping:https://medium.com/data-hackers/
# como-fazer-web-scraping-em-python-23c9d465a37f
# Goal: reproductibility, scalability

# TABELAS
url = "http://loterias.caixa.gov.br/wps/portal/loterias"
req = requests.get(url)
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content
soup = BeautifulSoup(content, 'html.parser')
table = soup.find_all(name='table')  # , attrs={'id'='simple-table lotomania'})
table_str = str(table)
df = pd.read_html(table_str, skiprows=0)


# Assigning tables:
federal = df[2]
