#!/bin/bash

#
## EFI BIOS Image
#
#BIOS='/usr/share/ovmf/OVMF.fd'

#
## Non EFI BIOS Image
#
BIOS='/usr/share/seabios/bios.bin'
#OPTROM='/home/pawl/vm/ide_386.bin'
OPTROM='/home/pawl/vm/optrom'
FLOPPY='/media/felix/images/98bootclean.img'

qemu-system-i386 \
	-bios ${BIOS} \
	-m 32 \
	-k en-us \
    -enable-kvm \
    -cpu host \
	-rtc base=localtime \
    -option-rom ${OPTROM} \
    -fda ${FLOPPY}

#
