# A part of pdfrw (https://github.com/pmaupin/pdfrw)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

'''
Currently, this sad little file only knows how to decompress
using the flate (zlib) algorithm.  Maybe more later, but it's
not a priority for me...
'''

import sys
from .objects import PdfName
from .uncompress import streamobjects
from .py23_diffs import zlib


def compress(mylist):
    flate = PdfName.FlateDecode
    for obj in streamobjects(mylist):
        ftype = obj.Filter
        if ftype is not None:
            continue
        if sys.version_info >= (3, 0):
            oldstr = obj.stream.encode('latin1')
        else:
            oldstr = obj.stream
        newstr = zlib.compress(oldstr)
        if len(newstr) < len(oldstr) + 30:
            if sys.version_info >= (3, 0):
                obj.stream = newstr.decode('latin1')
            else:
                obj.stream = newstr
            obj.Filter = flate
            obj.DecodeParms = None
