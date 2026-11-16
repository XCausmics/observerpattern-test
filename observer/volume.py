from observer.subject import Subject


class VolumeKnob(Subject):
    MIN = 0
    MAX = 100

    def __init__(self, level=25):
        super().__init__()
        self._level = self._clean(level)

    def _clean(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"volume has to be a whole number, not {value!r}")
        return max(self.MIN, min(self.MAX, value))

    def get_state(self):
        return self._level

    def set_state(self, value, changed_by=None):
        new_level = self._clean(value)
        if new_level == self._level:
            return
        self._level = new_level
        self.notify(changed_by)
