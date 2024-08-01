#la función filter se usa para filtrar elementos en una lista
números=[1,2,3,4,5]
nuevos_números=list(filter(lambda x:x%2==0,números))
print(nuevos_números)

#para el caso de un diccionario

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]
#se filtra la lista con los elementos donde se gano

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))#función lambda que verifica el win
            # esta es la forma general para hacer estas funciones de filtrado
print(new_list)
print(len(new_list))

print(matches)
print(len(matches))