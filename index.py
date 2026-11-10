from shapes import Circle, Rectangle
from registry import ShapeRegistry


registry = ShapeRegistry()

registry.register("circle", Circle())
registry.register("rectangle", Rectangle())


small_red_circle = registry.create("circle")
big_blue_rectangle = registry.create("rectangle")
big_yellow_circle = registry.create("circle")
small_green_rectangle = registry.create("rectangle")
 
small_red_circle.configure(x=10, y=20, color="red", radius=5)
big_blue_rectangle.configure(x=30, y=40, color="blue", width=15, height=25)
big_yellow_circle.configure(x=50, y=60, color="yellow", radius=10)
small_green_rectangle.configure(x=70, y=80, color="green", width=20, height=30)

print(small_red_circle)
print(big_blue_rectangle)
print(big_yellow_circle)
print(small_green_rectangle)
print(small_red_circle)
print(small_green_rectangle)

