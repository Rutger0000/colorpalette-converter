import colorpaletteconverter as cg

def test_colorpaletteconverter(tmp_path):
    # Create palette
    palette = cg.Palette("MyPalette")

    # Add colors in (r, g, b, a)
    palette.add_color((1,0,0,1), "Red")
    palette.add_color((0,1,0,1), "Green")

    # Path to save the file
    path = tmp_path / "out.clr"
    print(str(path))
    # Save the palette
    assert palette.save(str(path)) == (True, None)

