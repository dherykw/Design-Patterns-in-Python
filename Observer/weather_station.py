import signal
from random import randint

from .observer import Subject
from .weather_display import EnglishCurrentConditionsDisplay, SpanishCurrentConditionsDisplay


class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observer()

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)


class WeatherStationEngineSimulator:
    def __init__(self, weather_data, timeout=2):
        self.timeout = timeout
        self.weather_data = weather_data
        self.is_on = False

    def start(self):
        print("Weather Station Engine Simulartor Started.\nPress ENTER for stopping")
        self.is_on = True
        while self.is_on:
            try:
                self.wait_stop_signal()
            except TimeOutException:
                self.get_new_sensors_values()
            except KeyboardInterrupt:
                self.is_on = False

        print("Weather Station Stopped.")

    def get_new_sensors_values(self):
        temperature, humidity, pressure = self.get_random_data()
        self.weather_data.set_measurements(temperature, humidity, pressure)

    def get_random_data(self):
        return randint(20, 25), randint(0, 10), randint(60, 70)

    def wait_stop_signal(self):
        self.set_signal_timeout()
        self.wait_interrupt()

    def set_signal_timeout(self):
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.alarm(self.timeout)

    def alarmHandler(self, signum, frame):
        raise TimeOutException

    def wait_interrupt(self):
        input('')
        print("Stopping the Weather Station Engine")
        raise KeyboardInterrupt


class TimeOutException(Exception):
    pass


if __name__ == '__main__':
    weather_data = WeatherData()
    EnglishCurrentConditionsDisplay(weather_data)
    SpanishCurrentConditionsDisplay(weather_data)
    weather_station_engine = WeatherStationEngineSimulator(weather_data)
    weather_station_engine.start()
