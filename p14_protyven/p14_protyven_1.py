import csv

with open("boulevard depo.csv", "w") as songs:
    fieldname = ["Song", "Year"]
    wr = csv.DictWriter(songs, fieldnames=fieldname)
    dicto = {"Angry Toy$": "2020", "GoodBoiClek": "2017", "NBA": "2018", "Carousel": "2017", "OFF TOP": "2020", "Drug 2.0": "2021", "DRUГ": "2019", "Louis Vuitton Kiss": "2017", "Autopoetry": "2021"}
    wr.writeheader()
    for key,value in dicto.items():
        wr.writerow({"Song": key,
        "Year":value})
songs.close()
with open("boulevard depo.csv", "r") as songs:
    read = csv.DictReader(songs)
    for headers in read.fieldnames:
        print(headers, end= '       ')
    print("\n----------------------")
    for row in read:  
        print(row["Song"], row["Year"])