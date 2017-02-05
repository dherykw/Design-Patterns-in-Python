from .observer import Observer, Subject


class DisplayElement:
    def display(self):
        raise NotImplementedError('you must implement this method')


class BaseConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: Subject):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        raise NotImplementedError('you must implement this method')


class EnglishCurrentConditionsDisplay(BaseConditionsDisplay):
    def display(self):
        print("Current conditions → temperature: {} | humidity: {} | pressure: {}"
              .format(self.temperature, self.humidity, self.pressure))


class SpanishCurrentConditionsDisplay(BaseConditionsDisplay):
    def display(self):
        print("Condiciones Actuales → temperatura: {}  | humedad: {} | presión: {}"
              .format(self.temperature, self.humidity, self.pressure))
