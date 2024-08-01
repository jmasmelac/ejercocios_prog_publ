import csv

def read_csv(path):
    print('datos tomados de : https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset?resource=download')
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)  # estos son los encabezados de las columnas
        data=[]
        for row in reader:
            country_dict = {key: value for key, value in zip(header, row)}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data=read_csv('Python_proyects/{27}lectura_archivos/world_population.csv')
    print(data)


'''
import csv

def read_csv(path):
   # Tu código aquí 👇
   total = 0
   with open (path,'r') as csv_file:
      total=sum(int(r[1]) for r in csv.reader(csv_file))
   return total

response = read_csv('./data.csv')
print(response)
'''