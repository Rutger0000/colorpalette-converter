import objc
from Cocoa import NSColorList, NSColor, NSURL

class Palette:
    """Object to generate color palettes to use in MacOS."""

    def __init__(self, name: str):
        self.name = name
        self.colors = NSColorList.alloc().initWithName_(self.name)

    def add_color(self, color: tuple, key: str):
        """Adds a color to the color palette with a certain key.
        
        Parameters
        ----------
        color : tuple 
            this should be a tuple with 4 elements (r, g, b, a)
        key : str 
            the name of the color
        
        """
        color = NSColor.colorWithRed_green_blue_alpha_(*tuple(color))
        self.colors.setColor_forKey_(color, key)
        
    def save(self, path: str = None):
        """Saves the color palette
        
        Parameters
        ----------
        path: str
            The color palette will be saved to the specified path. If no path is specified the 
            color palette will be saved to the default ~/Library/Colors directory.
            https://developer.apple.com/documentation/appkit/nscolorlist/2269695-writetourl?language=objc
        """
        if path is None:
            return self.colors.writeToURL_error_(objc.nil, objc.nil)
        else:
            url = NSURL.alloc().initFileURLWithPath_(path)
            return self.colors.writeToURL_error_(url, objc.nil)

