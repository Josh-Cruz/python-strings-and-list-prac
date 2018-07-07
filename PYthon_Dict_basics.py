josh_C = {
    "name": "Josh",
    "age": 30,
    "country": "Murica",
    "fav_lan": "Python"
}

def print_info(dict):
    print "My name is", dict["name"]
    print "My age is", dict["age"]
    print "My country of origin is", dict["country"]
    print "My favorite language to code in is", dict["fav_lan"]

print(print_info(josh_C))