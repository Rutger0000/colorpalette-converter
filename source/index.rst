.. Colorpalette converter documentation master file, created by
   sphinx-quickstart on Fri Aug 20 12:54:07 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Colorpalette converter's documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. code-block:: python
   
   import colorpaletteconverter as cv

   # Create the palette, named "MyPythonPalette"
   mypalette = cv.Palette("MyPythonPalette")

   # Add a color using a key e.g. "White" and color described by (r, g, b, a)
   mypalette.add_color((1,1,1,1), "White")
   mypalette.add_color((1,0,0,1), "Red")
   mypalette.add_color((0,1,0,1), "Green")
   mypalette.add_color((0,0,1,1), "Blue")
   mypalette.add_color((0,0,1,0.5), "Translucent blue")

   # Save it to the default location. This will make it visible in the MacOS color palette.
   mypalette.save()

   # To save it to an alternative location
   mypalette.save("mypalette.clr")

.. toctree::
   :maxdepth: 2
   :caption: Colorpalette converter

   colorpaletteconverter
