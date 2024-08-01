#uso de la librería matplotlib

'''
verificar la instalación de python (ojo la version exacta) y el path las 2 carpetas
                                    python3x  y  Scripts
 python -m pip install matplotlib           #esto en cmd

'''

import matplotlib.pyplot as plt
# Crea un gráfico simple para probar
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Gráfico de prueba')
plt.show()

def generate_var_chart():
    labels=['a','b','c']
    values=[100,200,300]
    fig,ax=plt.subplots()
    ax.bar(labels,values)
    plt.show()

generate_var_chart()

labels=['d','e','f']
values=[100,50,30]    
def pie_char (values,labels):
    fig,ax =plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()

pie_char(values,labels)