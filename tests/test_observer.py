import unittest

from observer.displays import BarMeter, LoudnessLabel, NumberReadout
from observer.volume import VolumeKnob


class ObserverTests(unittest.TestCase):

    def setUp(self):
        self.knob = VolumeKnob(25)
        self.number = NumberReadout(self.knob)
        self.bar = BarMeter(self.knob)
        self.words = LoudnessLabel(self.knob)

    def test_displays_sign_up_and_show_starting_level(self):
        self.assertEqual(self.knob.observers, [self.number, self.bar, self.words])
        self.assertEqual(self.number.showing, "number | VOL  25")
        self.assertEqual(self.words.showing, "label  | quiet")

    def test_change_from_one_display_reaches_the_others(self):
        self.number.set_state(60)
        self.assertEqual(self.knob.get_state(), 60)
        self.assertEqual(self.bar.state, 60)
        self.assertEqual(self.bar.showing, "bar    | [############........]")
        self.assertEqual(self.words.showing, "label  | normal")

    def test_update_pulls_from_the_subject(self):
        self.knob._level = 95
        self.words.update()
        self.assertEqual(self.words.state, 95)

    def test_detached_display_stops_updating(self):
        self.words.detach()
        self.number.set_state(80)
        self.assertEqual(self.words.state, 25)
        self.assertEqual(self.bar.state, 80)


if __name__ == "__main__":
    unittest.main()
