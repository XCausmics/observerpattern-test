from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, subject):
        self.subject = subject
        self.state = subject.get_state()
        subject.attach(self)

    def update(self):
        self.state = self.subject.get_state()
        self.redraw()

    def set_state(self, value):
        self.subject.set_state(value, changed_by=self)
        self.state = self.subject.get_state()
        self.redraw()

    def detach(self):
        self.subject.detach(self)

    @abstractmethod
    def redraw(self):
        ...
