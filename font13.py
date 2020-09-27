import codecs
import fontforge
import os.path
import string
import sys

if len(sys.argv) < 2:
    print('Usage: fontforge -script font13.py Roboto-Regular.ttf')
    sys.exit(1)

ttf = sys.argv[1]

font = fontforge.open(ttf)
font.selection.all()
font.copy()

copy = fontforge.font()
copy.selection.all()
copy.paste()

def rot13(cleartext):
    return codecs.encode(cleartext, 'rot_13')

for char in list(string.ascii_lowercase + string.ascii_uppercase):
    copy.selection.select(rot13(char))
    copy.copy()
    font.selection.select(char)
    font.paste()

font.familyname = rot13(font.familyname)
font.fullname = rot13(font.fullname)
font.fontname = rot13(font.fontname)
font.generate(rot13(os.path.splitext(ttf)[0]) + '.ttf')
font.close()
