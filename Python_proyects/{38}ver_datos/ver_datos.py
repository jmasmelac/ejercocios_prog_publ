import numpy as np
import matplotlib.pyplot as plt

sales = np.random.randint(100, 301, size = 12)
print(sales)
# np.save('sales.npy',sales)      #crea un archivo .npy
# np.savetxt('sales.csv',sales,delimiter=",") #crea el .csv

# cargo el archivo
# load_data = np.loadtxt('sales.csv',sales,delimiter=",")
months = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])

#figura
norm = plt.Normalize(min(sales), max(sales))
colors = plt.cm.viridis(norm(sales))#el viridis es el mapa de colores
# mapas de colores
"""
viridis, plasma, inferno, magma, cividis, Greys, Purples, Blues, Greens, Oranges, Reds, YlOrBr, YlOrRd, 
OrRd, PuRd, RdPu, BuPu, GnBu, PuBu, YlGnBu, PuBuGn, BuGn, YlGn, binary, gist_yarg, gist_gray, gray, bone, 
pink, spring, summer, autumn, winter, cool, Wistia, hot, afmhot, gist_heat, copper, PiYG, PRGn, BrBG, PuOr, 
RdGy, RdBu, RdYlBu, RdYlGn, Spectral, coolwarm, bwr, seismic, twilight, twilight_shifted, hsv, Paired, Accent, 
Pastel1, Pastel2, Tab10, Tab20, Tab20b, Tab20c, Set1, Set2, Set3, Dark2, flag, prism, ocean, gist_earth, terrain, 
gist_stern, gnuplot, gnuplot2, CMRmap, cubehelix, brg, gist_rainbow, rainbow, jet, nipy_spectral, gist_ncar

"""

plt.figure(figsize=(10,5))
plt.bar(months,sales,color=colors,label='ventas')
plt.title('ventas mes')
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.show()