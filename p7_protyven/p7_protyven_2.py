def check(x):
    try:
        if int(x) <= 255 and int(x) >= 0:
            return True
    except ValueError:
        return False

def hex(x,a,b,dict):
    a = int(int(x)/16)
    b = int((int(x)/16 - a)*16)
    if a in dict:
        a = dict[a]
    if b in dict:
        b = dict[b]
    return a,b
    
list = []

while True:
    value1 = input ("Enter first value (red): ")
    if check(value1):
        break
    print ("Wrong Value")
list.append(value1)

while True:
    value2 = input ("Enter first value (green): ")
    if check(value2):
        break
    print ("Wrong Value")
list.append(value2)

while True:
    value3 = input ("Enter first value (blue): ")
    if check(value3):
        break
    print ("Wrong Value")
list.append(value3)

color_rgb = list
print ("Your color(rgb): ", str(color_rgb).replace("[","").replace("'","").replace("]",""))

hex_dict = { 10 : "A", 11 : "B", 12 :"C", 13 : "D", 14 : "E", 15: "F"}

hex1 = hex(value1,0,0,hex_dict)
hex2 = hex(value2,0,0,hex_dict)
hex3 = hex(value3,0,0,hex_dict)
color_hex = [hex1, hex2, hex3]

print("Your hex color:", str(color_hex).replace("[","").replace("(","").replace(")","").replace("'","").replace(", ","").replace("]",""))