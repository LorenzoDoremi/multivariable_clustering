
from json.encoder import INFINITY


class avg_classifier:

    def __init__(self, keys, c_class):
        self.keys = keys
        self.c_class = c_class
        self.classes = []

    def train_avg_classifier(self, data):

        for element in data:
            found = False
            # update existing class in the list
            if len(self.classes) > 0:
                for curr_class in self.classes:
                    if curr_class[self.c_class] == element[self.c_class]:
                        found = True

                        for k in self.keys:
                            curr_class[k] += element[k]
                        curr_class["size"] += 1
                        break
                # add new class
                if not found:
                    new_class = {"class": element[self.c_class], "size": 1}
                    for k in self.keys:
                        new_class[k] = element[k]
                    self.classes.append(new_class)
            # empty list = new class
            else:
                new_class = {"class": element[self.c_class], "size": 1}
                for k in self.keys:
                    new_class[k] = element[k]
                self.classes.append(new_class)
        # calculate all averages of classes
        for curr_class in self.classes:
            for k in self.keys:
                curr_class[k] /= curr_class["size"]
        return self.classes

    def avg_classify(self, element):
        

        best_match = 0
        min_distance = INFINITY
        for index, curr_class in enumerate(self.classes):
           
           dist = 0
           for k in self.keys:
                dist+= abs( 1- max(curr_class[k], element[k])/max(0.0001, min(curr_class[k], element[k])))
           if dist < min_distance:
                best_match = index
                min_distance = dist

        
        return self.classes[best_match][self.c_class]

''' 
# example dataset
animali = [{"name": "gatto", "weight": 48, "age": 3, "length": 155, "class": "felino"},
           {"name": "leone", "weight": 160, "age": 8,
               "length": 250, "class": "felino"},
           {"name": "tigre", "weight": 170, "age": 4,
               "length": 270, "class": "felino"},
           {"name": "ragno", "weight": 0.27, "age": 2,
            "length": 14, "class": "invertebrato"},
           {"name": "cane", "weight": 17, "age": 10,
               "length": 120, "class": "canide"},
           {"name": "squalo", "weight": 5700, "age": 150,
               "length": 520, "class": "pesce"},
           {"name": "balena", "weight": 10000, "age": 50,
            "length": 1220, "class": "cetaceo"},
           {"name": "formica", "weight": 0.1, "age": 1,
            "length": 5, "class": "invertebrato"},
           {"name": "caracal", "weight": 8, "age": 3,
               "length": 105, "class": "canide"},
           {"name": "lupo", "weight": 100, "age": 8,
               "length": 200, "class": "canide"},
           {"name": "pesce palla", "weight": 1,
               "age": 14, "length": 70, "class": "pesce"},
           {"name": "elefante", "weight": 5000, "age": 80,
            "length": 500, "class": "pachiderma"},
           {"name": "uomo", "weight": 80, "age": 80,
               "length": 180, "class": "umano"},
           {"name": "mucca", "weight": 1000, "age": 15,
            "length": 320, "class": "ruminante"},
           {"name": "toro", "weight": 1200, "age": 10,
            "length": 350, "class": "ruminante"},
           {"name": "farfalla", "weight": 0.05, "age": 1,
            "length": 10, "class": "invertebrato"},
            {"name": "gatto", "weight": 108, "age": 2, "length": 75, "class": "felino"},
           {"name": "leone", "weight": 180, "age": 18,
               "length": 230, "class": "felino"},
           {"name": "tigre", "weight": 200, "age": 4,
               "length": 300, "class": "felino"},
           {"name": "ragno", "weight": 0.2, "age": 1,
            "length": 18, "class": "invertebrato"},
           {"name": "cane", "weight": 60, "age": 12,
               "length": 180, "class": "canide"},
           {"name": "squalo", "weight": 3700, "age": 100,
               "length": 320, "class": "pesce"},
           {"name": "balena", "weight": 32000, "age": 30,
            "length": 2220, "class": "cetaceo"},
           {"name": "formica", "weight": 0.05, "age": 1,
            "length": 4, "class": "invertebrato"},
           {"name": "caracal", "weight": 12, "age": 3,
               "length": 125, "class": "canide"},
           {"name": "lupo", "weight": 70, "age": 4,
               "length": 190, "class": "canide"},
           {"name": "pesce palla", "weight": 1,
               "age": 4, "length": 80, "class": "pesce"},
           {"name": "elefante", "weight": 4000, "age": 10,
            "length": 400, "class": "pachiderma"},
           {"name": "uomo", "weight": 100, "age": 30,
               "length": 190, "class": "umano"},
           {"name": "mucca", "weight": 800, "age": 12,
            "length": 280, "class": "ruminante"},
           {"name": "toro", "weight": 1300, "age": 5,
            "length": 375, "class": "ruminante"},
           {"name": "farfalla", "weight": 0.03, "age": 1,
            "length": 11, "class": "invertebrato"},

           ]

# example keys used
keys = ["length", "age", "weight"]
save_key = "name"
c_class = "class"


classifier = avg_classifier(keys, c_class)
classifier.train_avg_classifier(animali)

precision = 0
for el in animali: 
    if el[c_class] == classifier.avg_classify(el):
        precision+=1
 


print(precision/len(animali))
        '''




