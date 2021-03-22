
import urllib.request # Usada pra consultar uma URL
from prettytable import PrettyTable
import csv
from bs4 import BeautifulSoup # Analisa os dados retornados do site


f = csv.writer(open('dados6.csv', 'w'))
f.writerow(['Name', 'Email', 'Phone'])

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


	
for i in range(2, 102):
	table_name = ''
	table = ''
	
	wiki = "https://organicossuldeminas.com.br/produtores-e-produtos/"
	page = urllib.request.urlopen(wiki)
	soup = BeautifulSoup(page, 'html5lib')
	
	# Todos os valores
	listas = soup.find('tr', attrs={'class': 'row-'+str(i)+' even'})
	
	
	
	# Configuração do nome
	table_name = soup.find('td', attrs={'class', 'column-1'}) # Pega o valor que tem na classe numero
	if table_name is not None:
		nomes = table_name # Pega o local onde esta o nome
		# print(links_items) # Mostra o que tem dentro de 'a'
	elif table_name is None:
		table_name = ''
	
	try:
			# pega o nome
			for name in nomes:
						
				if repeti_name == name:
					print('')
					name = ''
				else:
					repeti_name = name
					print(name)
	except:
			pass


	table = soup.find('td', attrs={'class', 'column-6'}) # Pega numero e email
	#all_table = table.find_all('b')
	
	# Configuração do numero
	if table is not None:
		links_items = table# Pega o local onde esta o nome, numero e email
		# print(links_items) # Mostra o que tem dentro de 'a'
	elif table is None:
		table = ''
		
	try:
			# pega o numero 
			for phone in links_items:
						
				if repeti_num == phone:
					print('')
					phone = ''
				else:
					repeti_num = phone
					print(phone)
	except:
			pass
			
	
	
		
	print('--------------', i)
	
		

	f.writerow([name, phone])




