#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:32:30 2023

@author: nfamartins
"""

import requests
import pandas as pd

def get_data(endpoint, apikey):

    # url API
    url = 'https://guaracrm.com.br/api/v3/'
    
    # Criar objeto de ApiKeyAuth
    headers = {'Authorization': apikey}
    
    # parâmetro de page
    params = {'page': '1'}
    
    # setando o dataframe
    df = pd.DataFrame()
    
    # primeira página
    try:
        # faz a requisição GET para a API com a autenticação básica
        response = requests.get(url+endpoint, headers=headers, params=params)
        metadata = response.json()['metadata']
        totalRecords = metadata['pagination']['total_count']
        pages = metadata['pagination']['total_pages']
        
    except requests.exceptions.RequestException as e:
        # Ocorreu um erro ao fazer a requisição
        print("Erro de conexão:", str(e))
        return None
    
    #paginação
    for page in range(pages):
                
        # converte a resposta em formato JSON
        data = response.json()
        
        # concatena os dados da página ao df principal
        df = pd.concat([df,pd.json_normalize(data['data'])], ignore_index=True)
        
        # próxima página
        params['page'] = str(int(params['page']) + 1)
        response = requests.get(url+endpoint, headers=headers, params=params)
    
    return(df,totalRecords)