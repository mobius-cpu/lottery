#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : lotomania_retriever.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 19.01.2020
# Last Modified Date: 19.01.2020
# Last Modified By  : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>

import pandas as pd
import requests
from bs4 import BeautifulSoup
import random as rd
import numpy as np

# TABELAS
url = "http://loterias.caixa.gov.br/wps/portal/loterias"
req = requests.get(url)
content = req.content
soup = BeautifulSoup(content, 'html.parser')
table = soup.find_all(name='table')  # , attrs={'id'='simple-table lotomania'})
table_str = str(table)
df = pd.read_html(table_str, skiprows=0)

# Assigning tables:
lotomania = df[1]
lotomania = lotomania.values
lotomania_1D = np.reshape(lotomania, 20)
lotomania_list = lotomania_1D.tolist()

# Output
print(lotomania_list)
