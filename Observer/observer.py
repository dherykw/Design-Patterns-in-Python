class Subject:
    def register_observer(self, observer):
        raise NotImplementedError('you must implement this method')

    def remove_observer(self, observer):
        raise NotImplementedError('you must implement this method')

    def notify_observer(self):
        raise NotImplementedError('you must implement this method')


class Observer:
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError('you must implement this method')

