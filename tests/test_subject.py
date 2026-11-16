import unittest

from observer.observer import Observer
from observer.volume import VolumeKnob


class CountingObserver(Observer):
    def __init__(self, subject):
        self.pokes = 0
        super().__init__(subject)

    def update(self):
        self.pokes += 1
        super().update()

    def redraw(self):
        pass


class SubjectTests(unittest.TestCase):

    def setUp(self):
        self.knob = VolumeKnob(25)

    def test_get_and_set_state(self):
        self.assertEqual(self.knob.get_state(), 25)
        self.knob.set_state(80)
        self.assertEqual(self.knob.get_state(), 80)

    def test_attach_and_detach(self):
        a = CountingObserver(self.knob)
        b = CountingObserver(self.knob)
        self.assertEqual(self.knob.observers, [a, b])
        self.knob.detach(a)
        self.assertEqual(self.knob.observers, [b])

    def test_set_state_notifies_every_observer(self):
        a = CountingObserver(self.knob)
        b = CountingObserver(self.knob)
        self.knob.set_state(70)
        self.assertEqual((a.pokes, b.pokes), (1, 1))

    def test_observer_that_made_the_change_is_skipped(self):
        me = CountingObserver(self.knob)
        you = CountingObserver(self.knob)
        self.knob.set_state(70, changed_by=me)
        self.assertEqual((me.pokes, you.pokes), (0, 1))


if __name__ == "__main__":
    unittest.main()
