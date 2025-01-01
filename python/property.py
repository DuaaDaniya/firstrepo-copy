class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

# Creating an instance
circle = Circle(5)
print(circle.area)  # Output: 78.5

# Setting a new radius
circle.radius = 10
print(circle.area)  # Output: 314.0
