class Point:

    def __init__(self, x, y):
        """
        Initializes a Point instance with the given x and y coordinates.

        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Returns a string representation of the Point instance.

        :return: A string in the format "(x, y)" representing the point.
        """
        return f"({self.x}, {self.y})"