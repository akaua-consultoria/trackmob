#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:07:04 2023

@author: nfamartins
"""

from setuptools import setup, find_packages

setup(
    name="trackmob",
    version="0.1",
    description="Um pacote para consumo de dados da API da plataform TrackMob",
    author="Nathália Martins",
    author_email="nathalia@akaua.com.br",
    packages=find_packages(),
		install_requires=[
        'requests',
        'pandas',
        'setuptools'
    ],
)