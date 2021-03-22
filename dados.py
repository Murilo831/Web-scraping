
import urllib.request # Usada pra consultar uma URL
from prettytable import PrettyTable
import csv
from bs4 import BeautifulSoup # Analisa os dados retornados do site


f = csv.writer(open('dados.csv', 'w'))
f.writerow(['Name', 'Phone', 'E-mail'])

names = ''
num = ''
val_email = ''

rept_name = ''
rept_num = ''
rept_email = ''

for i in range(0, 101):
	
	
	wiki = "http://sistemas.agricultura.gov.br/vitrine/produto/amendoim-"+ str(i)
	
	try:
			page = urllib.request.urlopen(wiki)
	except:
			pass
	
	
	soup = BeautifulSoup(page, 'html5lib')


	"""Codigo para pegar o numero"""
	list_item_num = soup.find('span', attrs={'class': 'nu_telefone'}) # Pega o valor que tem na classe numero
	
	if list_item_num is not None:
		num = list_item_num.text.strip()
		print(num) # Mostra o numero
	
	elif num is None:
		num = ''
	
	try:	
			if rept_num == num:
				print('')
				num = ''
			else:
				rept_num = num
				print(num)
	except:
			pass



	"""Codigo para pegar o nome"""
	links = soup.find(class_='col-md-12') # Pega a classe da tabela
	
	if links is not None:
		links_items = links.find_all('a') # Pega o local onde esta o nome
		# print(links_items) # Mostra o que tem dentro de 'a'
	elif links is None:
		links = ''
	
	try:
			for result in links_items:
				names = result.contents[0] # pega o nome da pessoa
				
			if rept_name == names:
				print('')
				names = ''
			else:
				rept_name = names
				print(names)
	except:
			pass



	"""Codigo para pegar o email"""
	list1_item_name = soup.find('div', attrs={'class': 'col-md-12'})
	
	if list1_item_name is not None:
		lista = list1_item_name.find_all('p')
		#print(lista)
	elif list1_item_name is None:
		list1_item_name = ''

	try:
			for result_email in lista:
				val_email = result_email.contents[-1]
				#val_email = email.text.strip()
				
			if rept_email == val_email:
				print('')
				val_email = ''
			else:
				rept_email = val_email
				print(val_email)
	except:
		pass
		
	
	print('--------------', i)

	f.writerow([names, num, val_email])




