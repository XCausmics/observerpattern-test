# Observer Pattern – Volume Knob

My take on the Observer pattern in Python.

The idea: there's one volume knob on a stereo (the **subject**) and three
different displays hooked up to (the **observers**):

| display         | what it shows                      |
|-----------------|------------------------------------|
| `NumberReadout` | `VOL  60`                          |
| `BarMeter`      | `[############........]`           |
| `LoudnessLabel` | `muted` / `quiet` / `normal` / ... |

Any display can change the volume. When that happens, the knob tells all the
*other* displays, they each call `get_state()` to grab the new level, and
redraw. The knob has no idea what the displays look like, so adding a fourth
one is just a matter of writing the class and pointing it at the knob.

The volume is a whole number from 0 to 100. Going past either end just
stops there, like a real knob would.

## What you need

Just Python 3.8 or newer; the tests use the built-in
`unittest` module.

If it isn't there:

```bash
sudo apt update
sudo apt install -y python3
```

## Running it

Nothing to compile. Run these from the top folder of the repo.

Scripted demo:

```bash
python3 main.py
```

Play with it yourself (type things like `b 80` or `n 15`, `q` to quit):

```bash
python3 main.py -i
```

Run the tests:

```bash
python3 -m unittest discover -s tests -t . -v
```

Or just one of the two test classes:

```bash
python3 -m unittest tests.test_subject -v
python3 -m unittest tests.test_observer -v
```
