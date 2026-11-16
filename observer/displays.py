from observer.observer import Observer


class Display(Observer):

    label = "?"

    def __init__(self, knob):
        self.screen = []
        super().__init__(knob)
        self.redraw()

    @property
    def showing(self):
        return self.screen[-1]

    def redraw(self):
        self.screen.append(f"{self.label:<7}| {self.render(self.state)}")

    def render(self, level):
        raise NotImplementedError


class NumberReadout(Display):
    label = "number"

    def render(self, level):
        return f"VOL {level:3d}"


class BarMeter(Display):
    label = "bar"
    width = 20

    def render(self, level):
        filled = round(level * self.width / 100)
        return "[" + "#" * filled + "." * (self.width - filled) + "]"


class LoudnessLabel(Display):
    label = "label"

    def render(self, level):
        if level == 0:
            return "muted"
        if level < 30:
            return "quiet"
        if level < 70:
            return "normal"
        if level < 90:
            return "loud"
        return "neighbours are complaining"
