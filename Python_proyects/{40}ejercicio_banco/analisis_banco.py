'''
datos tomados de https://www.youtube.com/watch?v=bGnD1Ki7j-g&list=WL&index=168&t=716s&ab_channel=CodificandoBits
1. El problema del negocio

Una entidad bancaria contrata a una empresa de marketing encargada de contactar telefónicamente a posibles clientes para
determinar si están interesados o no en adquirir un certificado de depósito a término con el banco.

¿Qué perfil tienen los clientes con mayor potencial de conversión?
'''

#librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #también es de gráficas

ruta_archivo=r"Python_proyects\{40}ejercicio_banco\dataset_banco.csv"
datos_banco=pd.read_csv(ruta_archivo)
#no hay que hacer ningún tipo de conversion en los datos para su lectura
print("las filas y columnas de los datos son :",datos_banco.shape)
print(datos_banco.head(3))
print(datos_banco.tail(3))
print("las columnas del conjunto de datos son: \n",datos_banco.columns)
datos_banco.info()#consulta de datos categóricos y numéricos
'''
datos esperados

1. “age': edad (numérica)

2. "job": tipo de trabajo (categórica: 'admin.'. 'unknown', 'unemployed'. 'management', 'housemaid', "entrepreneur', "student".
"blue—collar",'self-employed', 'retired', 'technician', 'services')

3. "marital': estado civil (categórica: 'married', 'divorced', 'single')

4. "education": nivel educativo (categórica: 'unknown'. 'secondary', 'primary', *tertiary')

5. "default": si dejó de pagar sus obligaciones (categórica: 'yes', 'no')

6. "balance'z saldo promedio anual en euros (numérica)

7. "housing': ¿tiene o no crédito hipotecario? (categórica: 'yes'. 'no')

8. "loan": ¿tiene créditos de consumo? (categórica: 'yes', 'no')

9. "contact": medio a través del cual fue contactado (categórica: 'unknown', 'telephone', 'cellular')

10. "day': último dia del mes en el que fue contactada (numérica)

11. ”month': último mes en el que fue contactada (categórica: 'jan', 'feb', 'mar', …, 'nov', 'dec')

12. "duration“: duración (en segundos) del último contacto (numérica)

13. "campaign": número total de veces que fue contactada durante la campaña (numérica)

14. "pdays" número de días transcurridos después de haber sido contactado antes de la campaña actual (numérica. -1 indica que
no fue contactado previamente)

15. "previous': número de veces que ha sido contactada antes de esta campaña (numérica)

16. ”poutcome": resultado de la campaña de marketing anterior (categórica: 'unknown', 'other', 'failure', 'success")

17. "y": categoría ¿el cliente se suscribió a un depósito a término? (categórica: 'yes'. 'no')
'''

# identificar que datos faltan
print("faltan los siguientes datos: \n",datos_banco.isnull().sum())
# de la info de los datos faltan solo 3 o 2 datos por columna, se procederá a borrar

datos_banco.dropna(inplace=True)
datos_banco.info()

# identificar las columnas irrelevantes
# depende de la pregunta planteada al principio

#para el caso de las variables numéricas identificar un poco mas de ellas
print("\n")
print(datos_banco.describe())#se identifica el rango de valores mirando la desviación estándar (si es 0 todos los datos son iguales)
print("\n")

columnas_object_nombres=datos_banco.select_dtypes(include=['object']).columns.to_list()
for columna in columnas_object_nombres:
    print(f'columna {columna} : {datos_banco[columna].nunique()} sub niveles') #si aca hay un 1 esa columna se omite para el análisis

print("\n")

#eliminar filas repetidas
print("el tamaño del conjunto de datos es : ",datos_banco.shape)
datos_banco.drop_duplicates(inplace=True)
print("el tamaño del conjunto de datos después es : ",datos_banco.shape)

# identificar los valores extremos (numéricos)

columnas_numéricas_nombres=datos_banco.select_dtypes(exclude=['object']).columns.to_list()

print("\n")
print(columnas_numéricas_nombres)
print("\n")

fig, ax=plt.subplots(nrows=7,ncols=1,figsize=(8,30))
fig.subplots_adjust(hspace=0.5)
for i, col in enumerate(columnas_numéricas_nombres):
    sns.boxplot(x=col,data=datos_banco,ax=ax[i])
    ax[i].set_title(col)
plt.show()

# par el caso de la edad se eliminan los que tienen edad después de 100 años
# se eliminaran las llamadas con tiempos negativos
# previous tiene un dato extremadamente alto

print("retira las edades excesivas")
print("el tamaño del conjunto de datos es : ",datos_banco.shape)
datos_banco=datos_banco[datos_banco['age']<=100]
print("el tamaño del conjunto de datos después es : ",datos_banco.shape)

#filas llamadas negativas

print("retira las llamadas negativas")
print("el tamaño del conjunto de datos es : ",datos_banco.shape)
datos_banco=datos_banco[datos_banco['duration']>0]
print("el tamaño del conjunto de datos después es : ",datos_banco.shape)

#mas de 100 llamadas

print("retira las llamadas previas mayores a 100")
print("el tamaño del conjunto de datos es : ",datos_banco.shape)
datos_banco=datos_banco[datos_banco['previous']<=100]
print("el tamaño del conjunto de datos después es : ",datos_banco.shape)

print("\n")

# identificar los errores tipográficos

# como ya se tienen los nombres de las columnas categóricas

fig,ax=plt.subplots(nrows=10,ncols=1,figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(columnas_object_nombres):
    sns.countplot(x=col,data=datos_banco,ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30)
plt.show()


#si hay datos mal escritos se corregirán con
for columna in datos_banco.columns:
    if columna in columnas_object_nombres:
        datos_banco[columna]=datos_banco[columna].str.lower()#pasa los datos a minúscula



fig,ax=plt.subplots(nrows=10,ncols=1,figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(columnas_object_nombres):
    sns.countplot(x=col,data=datos_banco,ax=ax[i])
    ax[i].set_title(col)
    ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30)
plt.show()

print("\n")

#para el caso de job unificar admin. con administrative

print(f"los datos de la variable {columnas_object_nombres[0]} son : ")
print(datos_banco['job'].unique())#ver los nombres exactos
datos_banco['job']=datos_banco['job'].str.replace('admin.','administrative', regex=False)
print("los datos corregidos quedaron como : ")
print(datos_banco['job'].unique())

print("\n")
# para el caso de marital unificar div y divorced

print(f"los datos de la variable {columnas_object_nombres[1]} son : ")
print(datos_banco['marital'].unique())#ver los nombres exactos
datos_banco['marital']=datos_banco['marital'].str.replace('div.','divorced', regex=False)
print("los datos corregidos quedaron como : ")
print(datos_banco['marital'].unique())

print("\n")
#para el caso de education: unificar sec. y secondary, unk y unknown

print(f"los datos de la variable {columnas_object_nombres[2]} son : ")
print(datos_banco['education'].unique())#ver los nombres exactos
datos_banco['education']=datos_banco['education'].str.replace('sec.','secondary', regex=False)
datos_banco.loc[datos_banco['education']=='unk','education']='unknown'
print("los datos corregidos quedaron como : ")
print(datos_banco['education'].unique())

print("\n")
# y para el caso de poutcome: unificar unk y unknown

print(f"los datos de la variable {columnas_object_nombres[8]} son : ")
print(datos_banco['poutcome'].unique())#ver los nombres exactos
datos_banco.loc[datos_banco['poutcome']=='unk','poutcome']='unknown'
print("los datos corregidos quedaron como : ")
print(datos_banco['poutcome'].unique())

print("\n")
# para el caso de contact: unificar telephone y phone
print(f"los datos de la variable {columnas_object_nombres[6]} son : ")
print(datos_banco['contact'].unique())
datos_banco.loc[datos_banco['contact']=='phone','contact'] = 'telephone'
datos_banco.loc[datos_banco['contact']=='mobile','contact'] = 'cellular'
print(datos_banco['contact'].unique())

print("\n")

print("los datos quedaron como : \n",datos_banco.shape)