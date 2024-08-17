import pandas as pd
ruta_archivo=r"Python_proyects\{39}pandas\Online_Retail.csv"
data_tienda=pd.read_csv(ruta_archivo,encoding='latin-1')
data_tienda['Total_price']=data_tienda['Quantity']*data_tienda['UnitPrice']
print(data_tienda.head(3))

#se pueden crear columnas condicionales pero son de tipo booleano
data_tienda['High_value']=data_tienda['Total_price']>16
print(data_tienda['High_value'].head(6))

#consulta el tipo de las columnas 

data_tienda.info()#ojo,  "InvoiceDate  541909 non-null  object" debería ser fecha

data_tienda['InvoiceDate']=pd.to_datetime(data_tienda['InvoiceDate'])
print("\n")
data_tienda.info()

#aplicación de función lambda

data_tienda['Descuento']=data_tienda['UnitPrice'].apply(lambda x:x*0.9)
print(data_tienda.head(3))


print("\n")
#group by

contar_países=data_tienda['Country'].value_counts()
print(contar_países)
print("\n")

grupo_países_=data_tienda.groupby('Country')['Quantity'].sum()
print(grupo_países_) 

estadísticas_país=data_tienda.groupby('Country')['UnitPrice'].agg(['mean','sum'])
print(estadísticas_país)

país_stock=data_tienda.groupby(['Country','StockCode'])['Quantity'].sum()
print(país_stock)

# identificar cuales son los paises top 3 en ventas y cuales son los peores top 3 en ventas

top_ventas_país=data_tienda.groupby('Country')['UnitPrice'].sum().sort_values(ascending=False)
print("el top ventas de países son :\n")
print(top_ventas_país.head(3))
print("los peores países en ventas son : \n")
print(top_ventas_país.tail(3),"\n")

# filtrado de datos

data_tienda['Total_price']=data_tienda['Quantity']*data_tienda['UnitPrice']
print("mis columnas son : ",data_tienda.columns,"\n")
print(data_tienda.head(3),'\n')

#filtro
uk_sales=data_tienda[data_tienda['Country']=='United Kingdom']
print(uk_sales,'\n')#son los datos de  United Kingdom 

ventas_altas=data_tienda[data_tienda['Quantity']>10]
print(ventas_altas,'\n')#ventas altas

ventas_altas_uk=data_tienda[(data_tienda['Country']=='United Kingdom')&(data_tienda['Quantity']>40)]
print(ventas_altas_uk,'\n')#ventas altas uk 

ventas_2011_=data_tienda[data_tienda['InvoiceDate'].dt.year==2011]
print(ventas_2011_,'\n')#ventas 2011

ventas_dic_2010_=data_tienda[(data_tienda['InvoiceDate'].dt.year==2010)&(data_tienda['InvoiceDate'].dt.month==12)]
print(ventas_dic_2010_,'\n')

#tablas de pivoté

tabla_pivote=pd.pivot_table(data_tienda,values='Quantity',index='Country',columns='StockCode',aggfunc='sum')
                                               #valores           filas            columnas           operación
print(tabla_pivote,'\n')# representa las ventas de ese producto en ese país, el nan dice que no se a vendido ese producto en el país

#fusion de data frames