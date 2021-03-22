



import urllib.request # Usada pra consultar uma URL
from prettytable import PrettyTable
import csv
from bs4 import BeautifulSoup # Analisa os dados retornados do site


f = csv.writer(open('dados4.csv', 'w'))
f.writerow(['Name', 'Phone', 'E-mail', 'Instagram', 'Facebook', 'Site'])

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
repeti_insta = ''
repeti_site = ''
repeti_face = ''
insta = ''
face = ''
site = ''
for i in range(52, 1001):# ate 30.000 -> parei no 1999 a 3000
	
	wiki = "https://dfrural.emater.df.gov.br/poenacesta/contato?id=" + str(i)
	
	#wiki = "https://dfrural.emater.df.gov.br/poenacesta/contato?id=155"
	try:
			page = urllib.request.urlopen(wiki)
	except:
			pass
	
	soup = BeautifulSoup(page, 'html5lib')
	
	
	# Configuração do nome
	table_name = soup.find('h3', attrs={'class': 'product-title'}) # Pega o valor que tem na classe numero
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


	table = soup.find('p', attrs={'class': 'product-description'}) # Pega o valor que tem na classe numero
	#all_table = table.find_all('b')
	
	# Configuração do numero
	if table is not None:
		links_items = table.find_all('a')# Pega o local onde esta o nome, numero e email
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
			
	
	# Local onde esta o email	
	tables = soup.find('div', attrs={'class': 'details col-md-6'})
	
	# Configuração do email
	if tables is not None:
		links_email = tables.find_all('p') # Pega o local onde esta o nome
	elif tables is None:
		tables = ''
		
	try:
		
		
			# pega o email falta email
			for link in links_email:
				
				email = link.contents[-1]
				rec_email = email.split()[0]
				
				if repeti_email == rec_email:
					print('')
					rec_email = ''
				else:
					repeti_email = rec_email
					print(rec_email.split()[0])
				
	except:
			pass
			
	
	# Local onde esta o site, instagram e Facebook	
	tables = soup.find('div', attrs={'class': 'details col-md-6'})
	
	try:
			if tables is not None:
				links_items = tables.find_all('p') # Pega o local onde esta o nome
				vals = links_items[2].find_all('span')	
			elif tables is None:
				tables = ''
	except:
			pass
	
	
	try:
			# pega o Site
			for site in vals[2]:
				
				if repeti_site == site:
					print('')
					site = ''
				else:
					repeti_site = site
					print(site)
				
	except:
			pass
			
			
	
	try:
			# pega o Facebook
			for face in vals[1]:
				
				if repeti_face == face:
					print('')
					face = ''
				else:
					repeti_face = face
					print(face)
				
	except:
			pass
			
			
	try:
			# pega o Instagram
			for insta in vals[0]:
				
				if repeti_insta == insta:
					print('')
					insta = ''
				else:
					repeti_insta = insta
					print(insta)
				
	except:
			pass
	
	
	
		
	print('--------------', i)
	
		

	f.writerow([name, phone, rec_email, insta, face, site])




