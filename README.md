<h2> Multivariable Clustering </h2>

<p> This functions allows you to train a clustering AI to cluster dictionaries based on multiple variables you can choose. </p>

<h3> the main parameters are: </h3>

<ul>
 <li> data: a list of dictionaries. </li>
 <li> save_key: a string used to save the names inside the sets. for readability </li>
 <li>keys: a list of strings containing the dictionary entries. see example</li>
 <li>iteractions: how many time you want to repeat the process (the more, the more accurate)</li>
 <li>num_sets: how many sets you want. </li>
</ul>


<h2> Use example </h2>


```
animali = [
{"name": "cat", "weight": 48, "age": 3, "length": 155, "class": "feline"},
{"name": "dog", "weight": 60, "age": 8, "length": 150, "class": "canid"},
{"name": "tiger", "weight": 170, "age": 4, "length": 270, "class": "feline"}]


keys = ["weight", "age", "length"]
save_key = "name"
c_class = "class"


sets = multivariable_clustering(animali, save_key, keys, 100, 5)

insert_data(sets, {"name": "New Fish", "weight": 0, "age": 99, "length": 99}, keys, save_key);

```

<h2> Average Classifier </h2>

<p> This is a classifier class that lets you train an AI to a dictionary dataset, and then will return the most probable class of a new dictionary element. </p>

<h3> the main parameters are: </h3>

<ul>
 <li> data: a list of dictionaries. </li>
 <li>keys: a list of strings containing the dictionary entries. see example</li>
 <li>c_class: the dictionary entry used as the class name </li>
</ul>

```
# example keys used
keys = ["length", "age", "weight"]
c_class = "class"


classifier = avg_classifier(keys, c_class)
classifier.train_avg_classifier(animali)
presumed_class = classifier.avg_classify({"name": "New Cat", "weight": 10, "age": 6, "length": 150})
```