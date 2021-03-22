

import urllib.request # Usada pra consultar uma URL
from prettytable import PrettyTable
import csv
from bs4 import BeautifulSoup # Analisa os dados retornados do site


f = csv.writer(open('dados2.csv', 'w'))
f.writerow(['Name', 'Phone', 'E-mail'])

lista = []

names = ''
phones = ''
emails = ''
ver_phone = ''
ver_names = ''
ver_emails = ''
for i in range(1, 10000):
	
	wiki = "http://www.ceagesp.gov.br/guia-ceagesp/?atacadista=" + str(i)
	
	#wiki = "http://sistemas.agricultura.gov.br/vitrine/produto/abacate-6198-32"
	try:
			page = urllib.request.urlopen(wiki)
	except:
			pass
	
	soup = BeautifulSoup(page, 'html5lib')


	table = soup.find('div', attrs={'class': 'col-md-8'}) # Pega o valor que tem na classe numero
	#all_table = table.find_all('b')
	
	if table is not None:
		all_table = table.find_all('b') # Pega o local onde esta o nome, numero e email
		# print(links_items) # Mostra o que tem dentro de 'a'
	elif table is None:
		table = ''
	
	# Pega names - Inicio
	names = all_table[3]
	
	
	if ver_names == names:
		names = ''
	else:
		names = all_table[3]
		ver_names = names
	# Fim
	
	
	# Pega phones - Inicio
	phones = all_table[4]
	
	
	if ver_phone == phones:
		phones = ''
	else:
		phones = all_table[4]
		ver_phone = phones
	# Fim
	
	
	# Pega email - Inicio
	emails = all_table[5]
	
	
	if ver_emails == emails:
		emails = ''
	else:
		emails = all_table[5]
		ver_emails = emails
	# Fim
	
	for name in names:
		print(name)
    
    
	
	for phone in phones:
		print(phone)
    
    
	
	for email in emails:
		print(email)
		print('--------------------------')
	i	

	f.writerow([name, phone, email])




