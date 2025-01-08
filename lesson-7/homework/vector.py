import math
class Vector:
    def __init__(self, *args):
        self.components = list(args)
        self.dimension = len(self.components)
    def __repr__(self):
        return f"Vector({' ,'.join(map(str, self.components))})"
    def __str__(self):
        return f"({' ,'.join(map(str, self.components))})"
    def __add__(self, other):
        self._check_dimension(other)
        addition = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*addition)
    def __sub__(self, other):
        self._check_dimension(other)
        subtraction = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*subtraction) 
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("You can only multiple vector with float number")
        multipled = [a * scalar for a in self.components]
        return Vector(*multipled)
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    def dot(self, other):
        self._check_dimension(other)
        return sum(a * b for a, b in zip(self.components, other.components))
    def length(self):
        return math.sqrt(sum(a**2 for a in self.components))
    def normalize(self):

        normalized = [a/self.length() for a in self.components]
        return Vector(*normalized)
    def _check_dimension(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Variable must be a vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must be the same dimension")
    
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f"Vector{v1}")
    v3 = v1 + v2
    print(f"Vector{v3}")
    v4 = v2 - v1
    print(f"Vector{v4}")
    dot_product = v1.dot(v2)
    print(dot_product)
    v5 = 3 * v1
    print(f"Vector{v5}")
    v6 = 2 * v2
    print(f"Vector{v6}")
    print(v1.length())
    v_unit = v1.normalize()
    print(v_unit)
