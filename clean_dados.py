
import csv

f = csv.writer(open('dados_nao_repetidos.csv', 'w'))
f.writerow(['Name', 'Phone', 'facebook', 'instagram', 'site'])

def remove_repetidos(linha):
	l = []
	for i in linha:
		if i not in l:
			l.append(i)
	l.sort()
	return l


arquivo = open('dados_repetidos.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
	#print(linha)

	nova_lista = remove_repetidos(linha)
	for lista in nova_lista:
		print(lista)

	f.writerow([lista])
