import csv
 
#funcion para leer el csv
def read_csv(path):
	with open(path,'r') as csvfile:
		#hacemos un lector del archivo
		reader=csv.reader(csvfile,delimiter=',')
		#obteniendo nombre de columnas que esta en la fila 1
		header=next(reader)
		data=[]
		for row in reader:
			iterable=zip(header,row)
			#diccionario a partir del iterable
			country_dict={key:value for key,value in iterable}
			#data es una lista de diccionarios
			data.append(country_dict)
		return data
#ejecutarlo como un script desde la terminal
if __name__ == '__main__':
	data = read_csv('./data.csv')
	print(data[0:2])