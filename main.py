import sys

from observer.displays import BarMeter, LoudnessLabel, NumberReadout
from observer.volume import VolumeKnob


def print_panel(displays):
    for d in displays:
        print("   ", d.showing)
    print()


def scripted():
    knob = VolumeKnob(25)
    number = NumberReadout(knob)
    bar = BarMeter(knob)
    words = LoudnessLabel(knob)
    panel = [number, bar, words]

    print("Stereo switched on:")
    print_panel(panel)

    print("Someone types 60 into the number readout:")
    number.set_state(60)
    print_panel(panel)

    print("Someone drags the bar meter all the way up (asks for 150):")
    bar.set_state(150)
    print_panel(panel)

    print("The label display gets unplugged, then the knob is turned to 0:")
    words.detach()
    knob.set_state(0)
    print_panel(panel)
    print("(the label is stuck on its old text - it isn't listening anymore)")


def interactive():
    knob = VolumeKnob()
    panel = {
        "n": NumberReadout(knob),
        "b": BarMeter(knob),
        "l": LoudnessLabel(knob),
    }
    print("Type <display> <level>, e.g. 'b 80' or 'n 15'. Displays: n, b, l.")
    print("Empty line or 'q' to quit.\n")
    print_panel(panel.values())

    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if line in ("", "q"):
            break
        parts = line.split()
        if len(parts) != 2 or parts[0] not in panel:
            print("huh? try something like 'n 42'")
            continue
        try:
            panel[parts[0]].set_state(int(parts[1]))
        except ValueError:
            print("that's not a number")
            continue
        print_panel(panel.values())


if __name__ == "__main__":
    if "-i" in sys.argv[1:]:
        interactive()
    else:
        scripted()
