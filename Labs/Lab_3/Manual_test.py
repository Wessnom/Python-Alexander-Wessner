from Geometric_shape import Circle, Rectangle

cirkel1 = Circle(x=0, y=0, radius=1)  # enhetscirkel
cirkel2 = Circle(x=1, y=1, radius=1)
rektangel = Rectangle(x=0, y=0, side1=1, side2=1)

print(cirkel1 == cirkel2)  # True
print(cirkel2 == rektangel)  # False
print(cirkel1.is_inside(0.5, 0.5))  # True
cirkel1.transpose(5, 5)
print(cirkel1.is_inside(0.5, 0.5))  # False
# cirkel1.transpose("TRE", 5)  # ger ValueError med kommentar: "Translation values must be numbers."
