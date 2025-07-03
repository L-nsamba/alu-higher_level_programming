class Rectangle:
    """Defines a rectangle with width and height."""

    number_of_instances = 0  # public class attribute

    def __init__(self, width=0, height=0):
        self.width = width  # invokes setter for validation
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If either width or height is zero, perimeter is zero.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Print the rectangle using '#' characters.

        If width or height is zero, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""

        lines = ['#' * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string that can recreate the instance with eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
