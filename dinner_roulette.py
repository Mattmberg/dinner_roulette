import random

food_choices = ['Chicken Parm', 'American Chop Suey ', 'Chicken Fajitas', 'Lemon Pepper Chicken', 'Sheperds Pie',
                'Beef Stew', 'Stuffed Peppers', 'Cereal', 'Alfredo Pasta']

dinner_sides = ['Roasted Potatoes', 'Tater Tots', 'Green Beans', 'Cauliflower Rice', 'Corn', 'Mixed Vegetables']

for i in range(5):
    main_courses = random.choice(food_choices)

num_to_select = 2
list_of_random_items = random.sample(dinner_sides, num_to_select)
first_random_item = list_of_random_items[0]
second_random_item = list_of_random_items[1]

print(main_courses + ", " + first_random_item + ", " + second_random_item)
