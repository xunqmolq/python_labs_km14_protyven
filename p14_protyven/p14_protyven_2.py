import json
import os

x = os.path.abspath(__file__).replace("\\p14_protyven_2.py", "")
os.chdir(x)

with open("image_info_test-dev2017.json", "r") as pictures:
    data = json.load(pictures)
    count, categ, numb = [], [], []
    for i in data["images"]:
        count.append(i)
        i = dict(i)
        numb.append(i["file_name"])
        if i["file_name"] == "000000000001.jpg":
            url = i["coco_url"]
            height = i["height"]
            width = i["width"]
            id = i["id"]
    for i in data["categories"]:
        categ.append(i)
    print("Numbers of photos:", len(count), "\nNumber of categories:", len(categ))
    print("Url for 000000000001.jpg:", url, "\nHeight:", height, "Width:", width, "Id:", id )
    print("Maximum photo number:",max(numb))