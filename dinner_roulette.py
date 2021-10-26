from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
import random 

food_choices = ['chicken parm','american chop suey','chicken fajitas','lemon pepper chicken','sheperds pie','beef stew','stuffed peppers']

dinner_sides = ['roasted potatoes', 'tater tots', 'green beans', 'cauliflower rice', 'corn', 'mixed vegetables']

for i in range(5):
    main_courses=random.choice(food_choices)

num_to_select = 2
list_of_random_items = random.sample(dinner_sides, num_to_select)
first_random_item = list_of_random_items[0]
second_random_item = list_of_random_items[1]
dinners=main_courses + first_random_item + second_random_item

def window():
    app = QApplication(sys.argv)  ## todo creates an instance of QApplication
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)  ##  todo x, y, width, height
    win.setWindowTitle("Dinner Roulette!")

    label = QtWidgets.QLabel(win)
    label.setText(dinners)
    label.move(125, 125)

    win.show()  ## todo shows applications gui
    sys.exit(app.exec_())  ## todo runs your applications event loop/main loop

window()
