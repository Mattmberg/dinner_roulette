import random

food_choices = ['chicken parm','american chop suey','chicken fajitas','lemon pepper chicken','sheperds pie','beef stew','stuffed peppers']

dinner_sides = ['roasted potatoes', 'tater tots', 'green beans', 'cauliflower rice', 'corn', 'mixed vegetables']

for i in range(5):
    print(random.choice(food_choices))

num_to_select = 2
list_of_random_items = random.sample(dinner_sides, num_to_select)
first_random_item = list_of_random_items[0]
second_random_item = list_of_random_items[1]
print(first_random_item + ", " + second_random_item)
