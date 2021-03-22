


import urllib.request # Usada pra consultar uma URL
from prettytable import PrettyTable
import csv
from bs4 import BeautifulSoup # Analisa os dados retornados do site


f = csv.writer(open('dados7.csv', 'w'))
f.writerow(['Name', 'Phone', 'E-mail'])

lista = []

name = ''
phone = ''
email = ''
ver_phone = ''
ver_names = ''
ver_emails = ''
repeti_email = ''
repeti_name = ''
repeti_num = ''
for i in range(1999, 30001):# ate 30.000 -> parei no 1999 a 3000
	
	wiki = "http://parr.rr.gov.br/seapa/parr/"
	
	try:
			page = urllib.request.urlopen(wiki)
	except:
			pass
	
	soup = BeautifulSoup(page, 'html5lib')
	
	
	# Configuração do nome
	table_name = soup.find('h2', attrs={'class': 'h-t2 v3'}) # Pega o valor que tem na classe numero
	if table_name is not None:
		nomes = table_name.find_all('span') # Pega o local onde esta o nome
		# print(links_items) # Mostra o que tem dentro de 'a'
	elif table_name is None:
		table_name = ''
	
	try:
			# pega o nome
			for name in nomes[0]:
				
				if repeti_name == name:
					print('')
					name = ''
				else:
					repeti_name = name
					print(name)
	except:
			pass


	table = soup.find('div', attrs={'class': 'the_content_custom produtos'}) # Pega o valor que tem na classe numero
	#all_table = table.find_all('b')
	
	# Configuração do numero e email
	if table is not None:
		links_items = table.find_all('p')# Pega o local onde esta o nome, numero e email
		# print(links_items) # Mostra o que tem dentro de 'a'
	elif table is None:
		table = ''
		
	try:
			# pega o numero 
			for phone in links_items[0]:
				
				if repeti_num == phone:
					print('')
					phone = ''
				else:
					repeti_num = phone
					print(phone)
	except:
			pass
			
			
		
	try:
			# pega o email
			for email in links_items[1]:
				
				if repeti_email == email:
					print('')
					email = ''
				else:
					repeti_email = email
					print(email)
				
	except:
			pass
		
	print('--------------', i)
	
		

	f.writerow([name, phone, email])





