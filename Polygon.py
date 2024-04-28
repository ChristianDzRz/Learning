from abc import ABCMeta, abstractmethod
import math

class Polygon(metaclass = ABCMeta):
    """Class reprensenting poligons"""

    def __init__(self, vertices_coordinates):
        self._vertices_coordinates = vertices_coordinates

    @abstractmethod
    def perimeter(self):
        """Calculate the poligon perimeter"""
        perimeter = 0
        for v in range(len(self._vertices_coordinates)):
            if v == len(self._vertices_coordinates)-1:
                coord_1 = self._vertices_coordinates[v]
                coord_2 = self._vertices_coordinates[0]
            else:
                coord_1 = self._vertices_coordinates[v]
                coord_2 = self._vertices_coordinates[v+1]
            perimeter += self._calculate_vertices_distance(coord_1, coord_2)
        return perimeter

    
    abstractmethod
    def area(self):
        """"Calculate the Area of the poligon"""

    @staticmethod
    def _calculate_vertices_distance(v2, v1):
        distance = math.sqrt((v2[0]-v1[0])**2 + (v2[1]-v1[1])**2)
        return distance

class Triangle(Polygon):
    
    def __init__(self, vertices):
        super().__init__(vertices)

    def perimeter(self):
        return super().perimeter()
    
    def area(self):
        (x1, y1), (x2, y2), (x3, y3) = self._vertices_coordinates
        return (abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

        

class Quadrilateral(Polygon):

    def __init__(self, vertices):
        super().__init__(vertices)
    
    def perimeter(self):
        return super().perimeter()
    
    def area(self):
        dimensions = set()
        for v in range(len(self._vertices_coordinates)-1):
            coord_1 = self._vertices_coordinates[v]
            coord_2 = self._vertices_coordinates[v+1]
            dimensions.add(self._calculate_vertices_distance(coord_1, coord_2))
        return sum(list(dimensions)) if len(dimensions)>1 else dimensions.pop()**2

    

class Pentagon(Polygon):

    def __init__(self, vertices):
        super.__init__(vertices)

    def perimeter(self):
        return super().perimeter()

class Hexagon(Polygon):

    def __init__(self, vertices):
        super.__init__(vertices)

    def perimeter(self):
        return super().perimeter()


class Octagon(Polygon):

    def __init__(self, vertices):
        super.__init__(vertices)

    def perimeter(self):
        return super().perimeter()


if __name__ == "__main__":

    triangle = Triangle([[0,0],[3,0],[1.5,1.5]])
    print(triangle.perimeter())
    print(triangle.area())
    rectangle = Quadrilateral([[0,0],[0,2],[2,2],[2,0]])
    print(rectangle.perimeter())
    print(rectangle.area())

