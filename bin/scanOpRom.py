#!/usr/bin/env python

__author__      = 'Paul Komurka'
__description__ = 'https://github.com/pawlex/pcbios.optionrom'

import sys, os

help_text = """
    Useful for scanning BIOS roms for indications of option roms
    usage: %s <filename>
"""

STRIDE = 0x800      # 2KiB
ORMINSZ = STRIDE
ROMSTART = 256 * 2**10 

def oprom_scan(filename):
    image = None
    size = None
    with open(filename, "rb") as file:
        image = file.read()
        size = len(image)
        if(size < STRIDE):
            print("%s too small (%d bytes)" % (filename, size))
        #
    #
    for i in range(0, len(image), STRIDE):
        byte0 = ord( image[i] )
        byte1 = ord( image[i + 1] )
        byte3 = ord( image[i + 2] )
        if( (byte0,byte1) == (0x55,0xAA) ):
            print("0x%08x" % i),
            print(" <- Option Rom Signature Found"),
            print(" Size 0x%x (%d bytes)" % (byte3, byte3 * 512))
        else:
            if(i <= (size - ROMSTART)):
                continue
            # Determine if the next STRIDE is all repeating bytes.
            # Useful if you're looking for a location to place your oprom.
            if( image[i:i+ORMINSZ] == bytearray([image[i]]*ORMINSZ) ):
                print("0x%08x:[0x%05x] DATA=[0x%02x]*%d" % (i,(i&0xFFFFF),byte0,ORMINSZ))
            #
        #
    #
#

def main():
    if(len(sys.argv) < 2):
        print(help_text % sys.argv[0])
        return
    #
    oprom_scan(filename=sys.argv[1])
#

if __name__ == "__main__":
    main()
#


