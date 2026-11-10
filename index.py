from registry import ShapeRegistry
from shapes import Circle, Rectangle

registry = ShapeRegistry()

registry.register("small_circle", Circle(radius=5))
registry.register("big_rectangle", Rectangle(width=15, height=25))

small_red_circle = registry.create("small_circle")
small_red_circle.move(10, 20)
small_red_circle.set_color("red")

big_blue_rectangle = registry.create("big_rectangle")
big_blue_rectangle.move(30, 40)
big_blue_rectangle.set_color("blue")

print("Small Red Circle:")
print(small_red_circle)

print("Big Blue Rectangle:")
print(big_blue_rectangle)