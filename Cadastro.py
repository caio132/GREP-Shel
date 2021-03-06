#!/usr/bin/python
#-*- coding: utf8 -*-]
import os, re


def LimpaTela():
    os.system('cls||clear')

try:
    LimpaTela()

    nome = raw_input('Nome: ')
    
    if re.findall(r'^[a-zA-Z ]+$', nome):
        print('Nome Correto')
    else:
        print('Nome Incorreto, Tente Novamente!')

    mail = raw_input('Email: ')
    if re.findall(r'^.{1,}@([A-Z|a-z]{1,})\.(com|com.br|br)$', mail):
        print('Email Correto')
    else:
        print('Email Incorreto, Tente Novamente!')

    data = raw_input('Data de Nascimento: ')
    if re.findall(r'^(0[0-9]|[1,2][0-9]|3[0-1])/(0[0-9]|1[0-2])/(19[0-9]{2}|200[0-9]|201[0-8])$', data):
        print('Data de Nascimento Correto')
    else:
        print('Data de Nascimento Incorreta, Tente Novamente!')

    phone = raw_input('Telefone: ')
    if re.findall(r'^\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}$', phone):
         print('Telefone Correto')
    else:
        print('Telefone Incorreto, Tente Novamente!')

    rg = raw_input('RG: ')
    if re.findall(r'^[0-9]{1,3}(\.[0-9]{3}){2}-[a-z0-9]{1}$', rg):
        print('RG Correto')
    else:
         print('RG Incorreto, Tente Novamente!')

    cpf = raw_input('CPF: ')
    if re.findall(r'^([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}$', cpf):
        print('Cpf Correto')
    else:
        print('Cpf Incorreto, Tente Novamente!')

    ip  = raw_input('IP: ')
    if re.findall(r'^([0-9]\.|[1-9][0-9]\.|1[0-9]{2}\.|2[0-4][0-9]\.|25[0-5]\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2{0-4}[0-9]|25[0-4])$', ip):
        print('IP Correto')
    else:
        print('IP Incorreto, Tente Novamente!')

    mask = raw_input('Mascara: ')
    if re.findall(r'^(25[0-5]{1,3}\.){2}([0-255]{1,3}\.)[0-255]{1,3}$', mask):
         print('Mascara Correto')
    else:
        print('Mascara Incorreta, Tente Novamente!')

except KeyboardInterrupt:
    print()
