#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:27:28 2021

@author: douglas
"""
import pandas as pd
import numpy as np
restaurante = pd.read_csv("/home/douglas/Desenvolvimento/Python/datasets/archive/sales_one_hot_encoding.csv")
print(restaurante.columns)

print(restaurante.isnull().sum())
print(restaurante["DATA"].min())
print(restaurante["DATA"].max())
print(restaurante["TEMPERATURA"].describe())
print(restaurante["PRECIPITACAO"].describe())
print(restaurante["UMIDADE"].describe())
print(restaurante[restaurante['QTD_CONCORRENTES'] == 7]['VENDAS'].mean())
print(restaurante[restaurante['QTD_CONCORRENTES'] == 8]['VENDAS'].mean())
print(restaurante[restaurante['QTD_CONCORRENTES'] == 9]['VENDAS'].mean())
print(restaurante[restaurante['QTD_CONCORRENTES'] == 10]['VENDAS'].mean())
print(restaurante[restaurante['QTD_CONCORRENTES'] == 11]['VENDAS'].mean())
print(restaurante[restaurante['QTD_CONCORRENTES'] == 12]['VENDAS'].mean())
print(restaurante[restaurante['QTD_CONCORRENTES'] == 13]['VENDAS'].mean())
print(restaurante[restaurante['FDS'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['DS'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['DATA_FESTIVA'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['POS_DATA_FESTIVA'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['VESPERA_DATA_FESTIVA'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['DATA_NAO_FESTIVA'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['FERIADO'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['NAO_FERIADO'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['IS_SEMANA_PAGAMENTO'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['SEMANA_DE_NAO_PAGAMENTO'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['BAIXA_TEMPORADA'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['ALTA_TEMPORADA'] == 1]['VENDAS'].mean())
print(restaurante[restaurante['PRECIPITACAO'] == 0]['VENDAS'].mean())
print(restaurante[restaurante['PRECIPITACAO'] >= 2.3]['VENDAS'].mean())
print(restaurante[restaurante["TEMPERATURA"]<22.3]["VENDAS"].mean())
print(restaurante[restaurante["TEMPERATURA"]>30]["VENDAS"].mean())

