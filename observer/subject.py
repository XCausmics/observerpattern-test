from abc import ABC, abstractmethod


class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    @property
    def observers(self):
        return list(self._observers)

    def notify(self, changed_by=None):
        for obs in list(self._observers):
            if obs is changed_by:
                continue
            obs.update()

    @abstractmethod
    def get_state(self):
        ...

    @abstractmethod
    def set_state(self, value, changed_by=None):
        ...
