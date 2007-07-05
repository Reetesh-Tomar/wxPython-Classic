"""
A simple script to encode all the images the XRCed needs into a Python module
"""

import sys, os, glob
from wx.tools import img2py

def main():
    output = 'bitmaps.py'

    # get the list of BMP files
    files = glob.glob('bitmaps/*.bmp')
    files.sort()

    # Truncate the inages module
    open(output, 'w')

    # call img2py on each file
    for file in files:

        # extract the basename to be used as the image name
        name = os.path.splitext(os.path.basename(file))[0]

        # encode it
        if file == files[0]:
            cmd = "-u -n %s %s %s" % (name, file, output)
        else:
            cmd = "-a -u -n %s %s %s" % (name, file, output)
        img2py.main(cmd.split())


if __name__ == "__main__":
    main()

