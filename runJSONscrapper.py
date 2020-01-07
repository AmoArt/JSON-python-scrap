import json


with open('text.txt', 'rb') as json_file:
    
    data = json.load(json_file)

    for p in data:
        try:
            print(p['b']+"\n")
        except:
            print("")


