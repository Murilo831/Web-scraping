#!/usr/bin/env python
# coding: utf-8

# In[3]:


import urllib.request # Usada pra consultar uma URL
from prettytable import PrettyTable
import csv
from bs4 import BeautifulSoup # Analisa os dados retornados do site


# In[4]:


wiki = "http://sistemas.agricultura.gov.br/vitrine/produto/abacate-1"
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page, 'html5lib')


# In[5]:


list_item_num = soup.find('span', attrs={'class': 'nu_telefone'}) # Pega o valor que tem na classe numero
num = list_item_num.text.strip()
print(num) # Mostra o numero


# In[6]:


links = soup.find(class_='col-md-12') # Pega a classe da tabela
links_items = links.find_all('a') # Pega o local onde esta o nome
# print(links_items) # Mostra o que tem dentro de 'a'

for result in links_items:
    names = result.contents[0] # pega o nome da pessoa
    print(names)


# In[7]:


list1_item_name = soup.find('div', attrs={'class': 'col-md-12'})
lista = list1_item_name.find_all('p')
#print(lista)

for result_email in lista:
    val_email = result_email.contents[-1]
    #val_email = email.text.strip()
print(val_email)


# In[11]:


f = csv.writer(open('dados.csv', 'w'))
f.writerow(['Name', 'Phone', 'E-mail'])
f.writerow([names, num, val_email])


# In[ ]:




