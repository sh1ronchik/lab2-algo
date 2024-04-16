class Rectangle:
    
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        Initializes a Rectangle instance with the given coordinates.

        :param x1: The x-coordinate of the top-left corner.
        :param y1: The y-coordinate of the top-left corner.
        :param x2: The x-coordinate of the bottom-right corner.
        :param y2: The y-coordinate of the bottom-right corner.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def contains(self, x: float, y: float) -> bool:
        """
        Checks if the given point is within the rectangle.

        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        :return: True if the point is within the rectangle, False otherwise.
        """
        return self.x1 <= x < self.x2 and self.y1 <= y < self.y2