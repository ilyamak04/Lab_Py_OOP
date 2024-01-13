class Vehicle:
    """
    Базовый класс для транспортных средств.

    param: brand (str): Марка транспортного средства.
    param: model (str): Модель транспортного средства.
    """
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def start(self) -> str:
        """
        Метод для запуска транспортного средства.

        return: Возвращает строку с сообщением о запуске.
        """
        return f"{self.brand} {self.model} начал движение."

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand='{self.brand}', model='{self.model}')"


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.

    param: num_doors (int): Количество дверей.
    """
    def __init__(self, brand: str, model: str, num_doors: int):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def open_door(self) -> str:
        """
        Метод для открытия двери

        return: Возвращает строку с сообщением об открытии двери
        """
        return f"{self.brand} {self.model}: Дверь открыта."

    def __str__(self) -> str:
        return f"{super().__str__()}, Дверей: {self.num_doors}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand='{self.brand}', model='{self.model}', num_doors={self.num_doors})"


class Animal:
    """
    Базовый класс для животных

    param: species (str): Вид животного
    """

    def __init__(self, species: str):
        self._species = species

    # Вид животного должен быть неизменяемым
    @property
    def species(self):
        return self._species

    def __str__(self) -> str:
        return f"{self.species}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(species='{self.species}')"

    def random_sound(self) -> str:
        """
        Животное издаёт случайный звук

        return: Строка "Животное издаёт случайный звук"
        """
        return f"Животное издаёт случайный звук"

class Bird(Animal):
    """
    Дочерний класс для животных

    param: species (str): Вид животного
    param: type_of_bird (str): Вид птицы
    """
    def __init__(self, species: str, type_of_bird: str):
        super().__init__(species)
        self.type_of_bird = type_of_bird

    def __str__(self) -> str:
        return f"{self.species} {self.type_of_bird}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(species='{self.species}', type_of_bird='{self.type_of_bird}')"

    def random_sound(self) -> str:
        """
        Птица издаёт случайный звук

        return: Строка "Птица издаёт случайный звук"
        """
        return f"Птица издаёт случайный звук"

class Seagull(Bird):
    """
    Дочерний класс для чайки
    """

    def random_sound(self):
        """
        Чайка издаёт звук чайки

        return: Звуки чайки
        """
        return f"Ка-ка-ка"

class Figure:
    """Базовый класс для геометрических фигур

    param: color (str): Цвет геометрической фигуры.

    """

    def __init__(self, color: str):
        self._color = color

    # Делаем атрибут непубличным и через свойства устанавливаем проверку типа данных
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError("Цвет фигуры должен быть типа str")
        self._color = new_color

    def area(self) -> float:
        """Вычисление площади геометрической фигуры."""
        return 0.0

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.color} "

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color='{self.color}')"

class Circle(Figure):
    """
    Дочерний класс для круга

    param: color (str): Цвет круга.
    param: radius (int, float): Радиус круга.
    """

    def __init__(self, color: str, radius: (int, float)):
        super().__init__(color)
        self.radius = radius

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.color} {self.radius} "

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color='{self.color}', radius='{self.radius}')"

    def area(self) -> (int, float):
        """
        Вычисляем площадь круга

        return: Возвраащем площадь круга
        """
        return 3.14 * self.radius ** 2

class Rectangle(Figure):
    """
    Дочерний класс для прямоугольника

    param: color (str): Цвет круга.
    param: width (int, float): Шиирина.
    param: height (int, float): Высота.
    """
    def __init__(self, color: str, width: (int, float), height: (int, float) ):
        super().__init__(color)
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.color} {self.height} {self.width} "

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(color='{self.color}', height='{self.height}',\
         width='{self.width}')"

    def area(self) -> (int, float):
        """
        Вычисляем площадь прямоугольника

        return: Площадь прямоугольника
        """
        return self.width * self.height

    def perimetr(self) -> (int, float):
        """
        Вычисляем периметря прямоугольника

        return: Периметр прямоугольника
        """
        return  2*self.width + 2*self.height

if __name__ == "__main__":
    # Write your solution here
    pass
