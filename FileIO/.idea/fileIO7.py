#to read that what we just wrote in the file cities.txt
cities = []
with open("cities.txt","r") as asd:
    for city in asd: #see difference when
        #citites.append(city) is run
        cities.append(city.strip('\n')) # .strip strips '\n' from list
        print(city)
print("-"*40)
print(cities)
print("-"*40)
for city in cities:
    print(city)