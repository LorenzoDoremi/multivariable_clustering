<h1> Multivariable Clustering </h1>

<p> This functions allows you to train a clustering AI to cluster dictionaries based on multiple variables you can choose. </p>

<h2> the main parameters are: </h2>

<ul>
 <li> data: a list of dictionaries. </li>
 <li> save_key: a string used to save the names inside the sets. for readability </li>
 <li>keys: a list of strings containing the dictionary entries. see example</li>
 <li>iteractions: how many time you want to repeat the process (the more, the more accurate)</li>
 <li>num_sets: how many sets you want. </li>
</ul>


<h2> Use example </h2>
```
# example dataset
animali = [{"name": "gatto","weight": 4, "age": 3,"length": 55, "class": "felino"},
{"name": "leone", "weight": 160, "age": 8,"length": 250, "class": "felino"},
{"name": "tigre","weight": 170,"age": 4, "length": 270, "class": "felino"},
{"name": "ragno", "weight": 0.27, "age": 2, "length": 14, "class": "invertebrato"},
{"name": "cane", "weight": 17, "age": 10, "length": 120, "class": "canide"},
]

# example keys used
keys = ["weight", "age", "length"]
save_key = "name"
c_class = "class"


sets = multivariable_clustering(animali, save_key, keys, 100, 5)

insert_data(sets, {"name": "New Fish", "weight": 0, "age": 99, "length": 99}, keys, save_key);

```