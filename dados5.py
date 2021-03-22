
import urllib.request # Usada pra consultar uma URL
import csv
import requests
from bs4 import BeautifulSoup # Analisa os dados retornados do site

f = csv.writer(open('dados5.csv', 'w'))
f.writerow(['Name', 'Phone1', 'Phone2', 'E-mail'])

name = ''
phone = ''
email = ''
repeti_email = ''
repeti_name = ''
repeti_num = ''
repeti_num2 = ''

for i in range(1, 569):
	wiki = "https://vitrine.alimentodeorigem.com.br/fornecedor/" + str(i)
	
	try:
			page = urllib.request.urlopen(wiki)
	except:
			pass
	
	soup = BeautifulSoup(page, 'html5lib')
	
	
	for span_tag in soup.findAll('span'):
		span_tag.replace_with('')
		
		
	ul_dados = soup.find('ul', attrs={'class': 'portfolio-meta bottommargin'})
	
	if ul_dados is not None:
		val_dados = ul_dados.find_all('li')
	elif ul_dados is None:
		ul_dados = '' 
	
	# Dados nome
	try:
			h2_name = soup.find('h2')
			name = soup.h2.string
			print(name)
	except:
			pass
		
	# Dados numero 1
	try:
			
			numero = val_dados[2]
			for vals in numero:
				num = vals.strip()
				
				if repeti_num == num:
					print('')
					num = ''
				else:
					repeti_num = num
					print(num)
	except:
			pass
			
	# Dados numero 2
	try:
			
			numero = val_dados[3]
			for vals in numero:
				num2 = vals.strip()
				
				if repeti_num == num2:
					print('')
					num2 = ''
				else:
					repeti_num2 = num2
					print(num2)
	except:
			pass
			
		
	# Dados email
	try:
			val_email = val_dados[0]
			for valor in val_email:
				email = valor.strip()
				
				if repeti_email == email:
					print('')
					num = ''
				else:
					repeti_email = email
					print(email)
	except:
			pass
		
	print('--------------', i)
			
	f.writerow([name, num, num2, email])
	
	

