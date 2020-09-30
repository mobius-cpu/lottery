#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : retriever.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 19.01.2020
# Last Modified Date: 19.01.2020
# Last Modified By  : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>

import pandas as pd
import requests
from bs4 import BeautifulSoup


def scraper(url, name='table', whole=True):
    """This function retrives data and converts to dataframe"""
    req = requests.get(url)
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    if whole == 1:
        table = soup.find_all(name=name)
    else:
        table = soup.find(name=name)
    table_str = str(table)
    global df
    df = pd.read_html(table_str, skiprows=0)
    return df


# Searching for tables:
def searching_tables(n):
    for i in range(0, n):
        print("df[" + str(i) + "]")
        print(df[i])
        print('---------------------------------------------------------')


scraper("http://loterias.caixa.gov.br/wps/portal/loterias")
searching_tables(6)
