class City:
    """
    Класс, представляющий город.
    """

    def __init__(self, name: str, country: str, population: int, area: int) -> None:
        """
        Инициализирует новый объект города.

        Args:
            name: Название города.
            country: Страна, в которой находится город.
            population: Население города.
            area: Площадь города.
        """

        self.name = name
        self.country = country
        self.population = population
        self.area = area

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта города.

        Returns:
            Строка, представляющая город.
        """

        return f"Город: {self.name}, Страна: {self.country}, Население: {self.population}, Площадь: {self.area}"


# Пример использования
name = input("Введите название города: ")
country = input("Введите страну, в которой находится город: ")
population = int(input("Введите население города: "))
area = int(input("Введите площадь города: "))

city = City(name, country, population, area)  # Здесь используется новый синтаксис

print(city)
