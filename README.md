## Usage

```python
import colorpalettegenerator as cg

# Create the palette, named "MyPythonPalette"
mypalette = cg.Palette("MyPythonPalette")

# Add a color using a key e.g. "White" and color described by (r, g, b, a)
mypalette.add_color((1,1,1,1), "White")
mypalette.add_color((1,0,0,1), "Red")
mypalette.add_color((0,1,0,1), "Green")
mypalette.add_color((0,0,1,1), "Blue")
mypalette.add_color((0,0,1,0.5), "Translucent blue")

# Save it to the default location. This will make it visible in the MacOS color palette.
mypalette.save()
```