#writing into files
cities = ["Adelaide","Alice Springs","Darwin","Melbourne","Sydney"]
with open("cities.txt","w") as city_files: #now a cities.txt file is created
    for city in cities:
        print(city,file=city_files)#or print(city,file=city_files,flush=True)

        #what's the use of flush ???