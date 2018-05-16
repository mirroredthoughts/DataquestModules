## 2. Parsing the File ##

weather_data=[]
data=open('la_weather.csv','r').read()
rows = data.split('\n')
for r in rows:
    row_data=r.split(',')
    weather_data.append(row_data)


## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for w in weather_data:
    data=w[1]
    weather.append(data)
    
 

## 4. Counting the Items in a List ##

count = 0
for w in weather:
    count +=1
    


## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

    

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for w in weather_types:
    weather_type_found.append(w in new_weather)
    