import re
# expresión regular para buscar partidos del año 2012 con más de 5 goles
pattern = re.compile(r'^2012-[\d-]+,(.*),(.*),(\d+),(\d+),.*$')
f = open("la ruta aca //results_partidos.csv", "r", encoding="utf-8")

for line in f:
    res=re.match(pattern, line)
    if res:
        # convertir los goles a enteros
        home_score = int(res.group(3))
        away_score = int(res.group(4))
        # verificar si el partido tuvo más de 10 goles en total
        if home_score + away_score > 10:
            print(f"{res.group(1)} vs {res.group(2)}: {home_score}-{away_score}\n")

f.close()