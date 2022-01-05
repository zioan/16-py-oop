# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()


# https://pypi.org/
# python -m pip install -U prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Column Title", ['First item', 'Another', 'Thirdentry'])
table.add_column("Second column Title", [
                 'First item 2', 'Another 2', 'Third entry 2'])

table.align = 'l'

print(table)
