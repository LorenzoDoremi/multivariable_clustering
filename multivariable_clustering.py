from random import random
from numpy import Infinity


class multivariable_pivot_set:
    def __init__(self, keys, avg):
        self.s = set()

        
        self.keys = keys
        #avg is a list of averages for each key used
        self.avg = avg
        # the sum value of the i-th key. used for the average calc.
        self.total = [0]*len(self.keys)

        # num of elements in the set
        self.size = 0

    
    def insert(self,data, save_key):
        # in the set i just put the chosen save key for visualization. 
        self.s.add(data[save_key])
        self.size+=1
        # sum on total
        for i in range(0,len(self.keys)):
          self.total[i] += data[self.keys[i]]
        
        # calc average
        for i in range(0,len(self.keys)):
            self.avg[i] = self.total[i]/self.size
    
    def __str__(self):

        return str(self.s) + "\navg = "+str(self.avg) + "\nkeys= "+str(self.keys)

    def get_JSON(self):
        dic = dict(zip(self.keys, self.avg))
        dic["data"] = list(self.s)
        return dic

    



# this function inserts a dictionary data into a particular set who keeps track of the average of keys
def insert_data(sets, data, keys, save_key):
    
    if not isinstance(data, list):
        data = [data]
        
    for element in data:
        # calculate the distance of the dictionary from each given set. find the minimum
        minv = Infinity
        min_set : multivariable_pivot_set = None
        # per ciascun set
        for index in range(0,len(sets)):
            # for each key, calculate the abs difference between dict.key and the set average key
            # sum the differences on distance, and then check. 
            distance = 0
            for key_index in range(0,len(keys)):
                
                max_value = max(element[keys[key_index]],sets[index].avg[key_index])
                min_value = min(element[keys[key_index]],sets[index].avg[key_index])
                if min_value != 0:
                 distance += abs(1 - max_value/min_value)
                else:
                 distance += abs(1 - max_value/(0.1))
            # if distance is lower, save the current set candidate.
            if distance < minv:
                minv = distance
                min_set = sets[index]
        #assign the current dictionary to the candidate set   
        min_set.insert(element, save_key)

# data = a list of dictionaries
# save_key = the name used for indexing and visualization
# keys = a list of keys used to cluster
# iterations = a precision indicator 
# num_sets = how many sets you want            
def multivariable_clustering(data, save_key, keys, iterations, num_sets):
     
     sets = []
     eliminated = []
    
     d = data.copy()
     #creates randomic sets by using the initial data
     for i in range(0,num_sets):
      new_set = multivariable_pivot_set(keys, [0 for x in keys])
      random_pivot = d[int(random()*len(d))]
      new_set.insert(random_pivot,save_key)
      sets.append(new_set)
      #i temporarily remove already visited random pivots
      d.remove(random_pivot)
      eliminated.append(random_pivot)

     
     for el in eliminated:
       d.append(el)

     #for each iteration, insert the data into sets, then get the average a recreate new starting sets.
     for i in range(0,iterations):
            insert_data(sets, data, keys, save_key)
            for set_index in range(0,len(sets)):
                new_avg = sets[set_index].avg
              
                sets[set_index] = multivariable_pivot_set(keys, new_avg)

     
     # at the end, do a final insert.
     insert_data(sets, data, keys, save_key)
     return sets









