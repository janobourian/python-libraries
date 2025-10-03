import math
import numpy as np
from abc import ABC, abstractmethod

class Vector(ABC):
    @abstractmethod
    def magnitude(self) -> float:
        pass

    @abstractmethod
    def unit_vector(self):
        pass
    
    @abstractmethod
    def inner_product(self, other) -> float:
        pass
    
    @abstractmethod
    def angle_between(self, other) -> float:
        pass
    
    @abstractmethod
    def proyection_onto(self, other):
        pass

    @abstractmethod
    def __mul__(self, scalar: float | int):
        pass
    
    def radians_to_degrees(self, radians: float) -> float:
        return radians * (180.0 / math.pi)


class Vector3D(Vector):
    def __init__(self, x: float | int, y: float | int, z: float | int) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    def __mul__(self, scalar: float | int):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def unit_vector(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Zero vector has no direction")
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)
    
    def inner_product(self, other: 'Vector3D') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def angle_between(self, other: 'Vector3D') -> float:
        dot_product = self.inner_product(other)
        magnitudes_product = self.magnitude() * other.magnitude()
        if magnitudes_product == 0:
            raise ValueError("Zero vector has no direction")
        cos_angle = dot_product / magnitudes_product
        return math.acos(cos_angle)
    
    def proyection_onto(self, other: 'Vector3D'):
        other_unit = other.unit_vector()
        scalar_projection = self.inner_product(other_unit)
        return other_unit * scalar_projection

class Vector2D(Vector):
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __mul__(self, scalar: float | int):
        return Vector2D(self.x * scalar, self.y * scalar)

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def unit_vector(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Zero vector has no direction")
        return Vector2D(self.x / mag, self.y / mag)

    def inner_product(self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y
    
    def angle_between(self, other: 'Vector2D') -> float:
        dot_product = self.inner_product(other)
        magnitudes_product = self.magnitude() * other.magnitude()
        if magnitudes_product == 0:
            raise ValueError("Zero vector has no direction")
        cos_angle = dot_product / magnitudes_product
        return math.acos(cos_angle)

    def proyection_onto(self, other: 'Vector2D'):
        other_unit = other.unit_vector()
        scalar_projection = self.inner_product(other_unit)
        return other_unit * scalar_projection


current_vector = Vector2D(5, 6)
longitude = current_vector.magnitude()
print(f"Longitude: {longitude}")

vector_value = Vector2D(1, 2)
inner_value = vector_value.inner_product(Vector2D(2,1))
print(f"Inner product: {inner_value}")

new_vector = Vector2D(3, 4)
unit_vector = new_vector.unit_vector()
print(f"Unit vector: {unit_vector}")

other_vector = Vector2D(6, 7)
current_magnitude = other_vector.magnitude()
print(f"Current magnitude: {current_magnitude**2}")

first_angle_vector = Vector2D(5, 2)
second_angle_vector = Vector2D(-3, 6)
angle_between = first_angle_vector.angle_between(second_angle_vector)
print(f"Angle between: {first_angle_vector.radians_to_degrees(angle_between)} degrees")

vector_3d = Vector3D(2, 3, 4)
scaled_vector = vector_3d * 2
print(f"Scaled Vector3D: {scaled_vector}")

projection_vector = Vector2D(-2, 8)
projected = projection_vector.proyection_onto(Vector2D(-1, 3))
print(f"Projection onto: {projected}")