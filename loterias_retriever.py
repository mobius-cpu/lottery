#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : loterias_retriever.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 19.01.2020
# Last Modified Date: 19.01.2020
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


# Searching for tables:
def searching_tables(n):
    for i in range(0, n):
        print("df[" + str(i) + "]")
        print(df[i])
        print('---------------------------------------------------------')


searching_tables(6)

# Assigning tables:
lotofacil = df[0]
lotomania = df[1]
federal = df[2]

# Converting and reshaping:
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html#numpy.reshape.
lotofacil = lotofacil.values
lotofacil_1D = np.reshape(lotofacil, 15)
lotofacil_list = lotofacil_1D.tolist()
lotomania = lotomania.values
lotomania_1D = np.reshape(lotomania, 20)
lotomania_list = lotomania_1D.tolist()

print(lotofacil)
print(lotomania)
