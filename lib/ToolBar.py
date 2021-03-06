## $Id: ToolBar.py 28 2004-12-06 10:47:21Z mightor $
## This file is part of PyQLogger.
## 
## Copyright (c) 2004 Eli Yukelzon a.k.a Reflog         
##
## Modified by Xander Soldaat to include support for
## adding URLs and Image tags
##
## PyQLogger is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
## 
## PyQLogger is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with PyQLogger; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
""" This module contains all functions to be called from 
the toolbar. The mapping is done thru Button->Func method
"""

tbBold_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x74\x49\x44\x41\x54\x18\x95\xed\x93\x41\x0e\x80" \
    "\x20\x0c\x04\x57\x5f\xda\xa7\xed\x4f\xeb\x45\x4c" \
    "\x85\xa6\x58\xd1\x83\x86\x49\xb8\x94\x30\x59\x5a" \
    "\x00\x26\x6f\xb3\x04\x7b\x3a\xe2\x58\xa3\x03\x24" \
    "\x4f\x05\x92\xa8\x6b\x89\x00\x0d\x5a\x16\x49\xbd" \
    "\x50\x07\x10\x27\x1e\xe2\xae\xf8\x48\xe8\xb4\x06" \
    "\x40\x3c\xbc\x46\x62\xb1\x42\x11\x69\x3c\x29\x71" \
    "\x91\x89\x48\xd7\x91\x6e\xc5\x9e\xce\xca\xdc\x1b" \
    "\x3d\x32\xbc\xff\xbf\x8a\xee\x8f\x32\xc3\xcc\xbd" \
    "\x0a\xaf\x77\x35\x9e\x74\xf2\x71\x36\x4c\x03\x2e" \
    "\x2a\x65\x3b\x90\xc2\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
tbItalic_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x81\x49\x44\x41\x54\x18\x95\xed\x93\xc1\x0d\xc3" \
    "\x30\x0c\x03\x2f\x9d\x88\x23\x79\x04\x8f\xe2\x11" \
    "\x38\x92\x37\x52\x3e\x4d\xd0\x14\x4e\x8d\x24\x2d" \
    "\xea\x47\x0e\x10\x04\xeb\x41\x09\x26\x08\x37\x43" \
    "\x20\x29\x80\xb5\x96\xf7\xb3\x37\x99\x8e\x2c\xb0" \
    "\x1d\xa5\x14\x00\x72\xce\xeb\x3c\xa5\x74\x48\xa7" \
    "\x45\x48\x0a\xdb\x61\x7b\xf7\x5a\x80\xc7\xd9\x0d" \
    "\xbd\x2b\x4f\x0b\xf7\x18\x42\x38\x24\x51\x6b\xbd" \
    "\x6c\x54\x4b\xb8\x6b\xda\xc2\xff\xbf\x42\xd2\x4f" \
    "\x84\x03\xb6\xa1\xb8\x4a\xbc\xd7\xa7\x18\xbf\xd2" \
    "\x75\x78\xcf\xac\x6f\xc4\xf8\x66\x50\x66\x92\x09" \
    "\x2f\xfd\x65\xac\xd0\x68\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
tbUnder_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x6f\x49\x44\x41\x54\x18\x95\xed\x94\x3b\x0e\xc0" \
    "\x30\x08\x43\x4d\x4f\xca\xd1\xb8\x29\x9d\xa8\xa2" \
    "\x8a\xef\xd0\xa9\x3c\x29\x52\x12\x47\x06\x06\x07" \
    "\x58\xbe\x86\x82\x7b\x2d\xde\x7b\x3a\x85\x87\x13" \
    "\x11\x51\x66\xb6\xfd\x73\xcf\xcc\x74\xea\x9e\xd6" \
    "\x41\x01\xa8\x88\x44\x13\x84\xda\xd5\xad\x30\x65" \
    "\x8d\xd7\x78\x6e\x4c\x00\x60\x41\x79\xa1\x48\x02" \
    "\xd6\x45\x9d\x85\x24\x38\xfd\x8a\x9e\x49\x16\xe1" \
    "\xca\x38\xec\xa8\xf2\x28\x3b\xce\xc6\x35\x26\x9f" \
    "\xcf\x0f\xb9\x01\x92\x16\x2b\xcc\x1b\x67\x3d\x54" \
    "\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
tbLeft_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x34\x49\x44\x41\x54\x18\x95\x63\x60\x18\x05\xb4" \
    "\x06\x8c\x58\xc4\xfe\x53\xd1\x2c\xea\x03\x6a\xb8" \
    "\x98\x3e\x2e\xc5\x67\x1b\xb1\x2e\xa6\xaf\x4b\xf1" \
    "\xd9\x3a\x9a\x2a\xa8\x0b\x86\x7f\x18\x0f\x4c\xda" \
    "\x1d\x05\xf4\x05\x00\xcd\x32\x07\x08\x01\xd0\xc9" \
    "\x8e\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
tbCenter_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x3a\x49\x44\x41\x54\x18\x95\x63\x60\x18\x05\xb4" \
    "\x06\x8c\x58\xc4\xfe\x53\xd1\x2c\xea\x03\x5c\xb6" \
    "\x90\xea\x6a\xfa\xb8\x96\x90\x4d\xc4\xba\x9a\x7e" \
    "\xae\xc5\x65\xdb\x68\xaa\xa0\x2e\x18\x3e\x61\x0c" \
    "\x03\x84\x5c\x4f\xdf\x34\x3c\x0a\xe8\x03\x00\xb1" \
    "\x2e\x07\x08\x76\x79\xa7\x27\x00\x00\x00\x00\x49" \
    "\x45\x4e\x44\xae\x42\x60\x82"
tbRight_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x37\x49\x44\x41\x54\x18\x95\x63\x60\x18\x05\xb4" \
    "\x06\x8c\x58\xc4\xfe\x53\xd1\x2c\xea\x03\x7c\xb6" \
    "\x90\xea\xf2\x81\x77\x31\x0c\x10\xeb\xf2\x81\x73" \
    "\xf1\x68\xaa\xa0\x2e\x18\x5e\x61\x8c\x0d\xe0\xf3" \
    "\x0d\x7d\x5c\x3c\x0a\x68\x0f\x00\x91\x32\x07\x08" \
    "\xa7\xc2\xb4\x2b\x00\x00\x00\x00\x49\x45\x4e\x44" \
    "\xae\x42\x60\x82"
tbBr_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x74\x49\x44\x41\x54\x18\x95\xed\xd2\xb1\x0d\xc0" \
    "\x20\x0c\x44\xd1\x73\x94\x41\x32\x82\x47\x62\x14" \
    "\x8f\xc0\x08\x1e\x89\x8d\x2e\x05\x5d\xe2\x34\x86" \
    "\x22\x42\xfc\x12\x89\x67\x84\x0c\xec\x76\xcf\x24" \
    "\x7b\x51\x55\xf9\x3c\x6b\xad\xa5\xbd\x17\x4e\x92" \
    "\xd1\x90\x63\xca\x84\xa0\xe5\x60\x7b\xfd\xdd\x04" \
    "\xd8\xe8\x7e\x65\xdd\x2f\xb8\xa3\xa5\x94\xf4\xfa" \
    "\x9c\x11\x0a\x18\x6a\xd5\x70\x57\x93\x70\x47\xc9" \
    "\xb4\xf7\x09\x0b\x60\x14\x11\xa8\xea\x30\x1e\x64" \
    "\x74\xf7\xf1\x67\xaf\x86\xff\xac\x1b\xad\xf7\x2d" \
    "\x19\xfe\xa2\x32\x68\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
tbFontPlus_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x7b\x49\x44\x41\x54\x18\x95\xed\x92\xc1\x0d\xc4" \
    "\x20\x0c\x04\xc7\xa7\x2b\x2c\xa5\x6d\x69\xee\x8c" \
    "\x7c\x40\x22\x27\x1b\x38\xbe\x61\x24\x3f\x40\x68" \
    "\x19\x1b\xe0\xf0\x3a\x4a\xad\x94\xcf\x66\x28\x00" \
    "\x92\xd2\xf0\x30\xd8\xa1\x78\x6c\x34\xb4\x9c\x06" \
    "\x0f\x30\x49\x4b\x07\xbf\xfd\xc2\x7f\x8c\xda\xfa" \
    "\x02\x6b\x7b\x92\x8c\x05\xf3\x25\xe3\xd1\x2c\x33" \
    "\x1e\xc6\xcd\xcc\xab\x91\x2f\xb6\x3d\x0d\x8e\xa8" \
    "\xad\xff\x4d\x38\x8a\x0b\x6c\x60\xdb\x7f\xb7\x9d" \
    "\x3b\x53\x4a\x5f\xd9\xfc\xa7\xa3\x08\xb0\x9d\xc7" \
    "\x3c\x1c\xe0\x06\x0c\x1e\x27\x0f\x59\xb1\xf8\xd5" \
    "\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
tbFontMinus_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x6a\x49\x44\x41\x54\x18\x95\xed\x92\x51\x0a\x80" \
    "\x20\x10\x44\x67\xa3\x83\x79\xb4\x39\x5a\x37\xab" \
    "\x1f\x0b\xb4\x46\xd6\xb5\x3f\x7d\x20\x28\xc8\x63" \
    "\x76\x14\x58\x4c\xc7\x99\x97\x64\x0b\x4a\x01\x00" \
    "\x24\xa5\xbc\x57\xdc\x4c\x39\x22\x36\x92\xae\x8b" \
    "\x7b\x79\x3c\x44\xa2\x64\xf7\x8e\xa4\xc1\x91\xdc" \
    "\x95\xb8\xd5\xa5\xa2\x4a\x9c\x2c\x22\x71\x88\x9f" \
    "\x51\x87\x89\x48\xea\x89\x3e\x1d\x91\x7f\x5c\xa0" \
    "\xaa\x7b\x55\xe1\xe0\xb7\x77\x58\xcc\xc6\x05\x5a" \
    "\xd6\x19\x57\x89\x3d\xad\x1e\x00\x00\x00\x00\x49" \
    "\x45\x4e\x44\xae\x42\x60\x82"
tbUl_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x35\x49\x44\x41\x54\x18\x95\x63\x60\x18\x05\xb4" \
    "\x06\x8c\x98\x42\xf5\xff\x11\xec\x46\x2c\xf2\xc4" \
    "\x01\x16\x22\xd5\xfd\x27\xac\x04\xd5\x91\xc4\x1a" \
    "\x4c\xb6\xcb\x87\x0e\x18\x8d\xbc\x21\x0c\x46\x23" \
    "\x6f\x14\x0c\x07\x00\x00\x24\xbf\x09\x1f\x74\x26" \
    "\x50\x73\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42" \
    "\x60\x82"
tbOl_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x69\x49\x44\x41\x54\x18\x95\xed\x92\x41\x0a\x80" \
    "\x30\x0c\x04\x37\xe2\xbf\x83\x2f\x5f\x8f\x1a\x52" \
    "\x65\x49\xa8\x5e\x3a\x50\x0a\x6d\x99\x2c\x49\x81" \
    "\xc5\x4f\x38\xbb\x86\x5d\x94\x2a\x85\x4c\x78\xd3" \
    "\x4f\x3c\xa8\x72\x97\x1e\x4a\x8a\x77\x31\xc9\x76" \
    "\x4a\x00\x30\xb3\x18\xe6\x12\x3b\xab\xad\x18\x86" \
    "\xcb\x87\x41\x4e\x61\x29\xe2\x7e\xe2\x2d\x5f\x3b" \
    "\xe3\x5e\x63\xda\xf0\xa6\x7d\xb7\x07\x52\x1b\xa4" \
    "\xe1\x55\xe5\x5d\xea\xff\x78\xf1\x2d\x27\x9a\x4a" \
    "\x4a\x47\xde\x0f\x8e\x11\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
tbHr_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x33\x49\x44\x41\x54\x18\x95\xed\xcc\x31\x0a\x00" \
    "\x20\x10\x03\xc1\xcb\xcf\xf7\xe7\xb1\x13\xaf\x10" \
    "\x8b\xab\x84\x4c\x17\x08\x5b\x15\x11\x57\x3a\x07" \
    "\xe0\x49\x0c\xd8\xbd\x16\xb6\x3d\x0a\x4b\xd2\xfb" \
    "\x15\x11\x1f\x5a\x01\x15\x08\x03\x7d\xe0\xfc\x0c" \
    "\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
tbUrl_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x02" \
    "\x44\x49\x44\x41\x54\x18\x95\xdd\x94\x4b\x4f\x13" \
    "\x51\x18\x86\x9f\x43\x07\xad\x5d\x98\x31\x46\x11" \
    "\x2f\xd1\xb8\xd1\xba\xd0\x85\x37\x5c\x52\x4c\xaa" \
    "\x52\x8c\xc4\x08\x68\xc1\x92\xb0\xc1\xf0\x07\x80" \
    "\x1f\xa0\x86\xb0\x71\xe1\x8e\x4b\x13\x21\xe1\x16" \
    "\x31\x86\x50\x9a\xe8\xd2\xc8\x46\x60\x09\x51\xa6" \
    "\x25\x51\x7a\x01\xa2\x26\x32\x56\xd2\xf6\x73\x61" \
    "\xaa\x8c\x30\xa5\xb0\x70\xe1\x9b\x4c\x72\x32\x73" \
    "\xce\x93\x37\xdf\xfb\xce\x51\xc9\x44\x9c\x03\x07" \
    "\x4b\x04\x60\x29\x99\x50\xb9\xf5\x76\xa4\x94\x42" \
    "\xe4\xd7\xb1\xa5\x64\x42\x01\x14\x6d\x17\x52\xa8" \
    "\xfe\x1d\x58\x29\xb5\x61\xd3\xfa\x77\xb9\xb5\x52" \
    "\x6a\xd3\xbd\x39\x69\x3b\x71\xb3\x7e\xa6\x76\xda" \
    "\xd1\x28\xb6\x82\xee\x18\x5c\x88\xfe\x13\xf0\x66" \
    "\x2d\xd8\xae\x36\xb4\x42\x44\x2c\x55\x12\x11\x16" \
    "\xa2\x11\x1e\x34\x37\x03\x10\x8d\x18\x05\x81\x2d" \
    "\x8e\x73\xbf\xb3\x88\xfc\x7e\x00\x7a\x83\x41\x3c" \
    "\x9e\x72\x3c\x9e\x72\x7a\x83\xc1\x0d\x90\xcd\x5a" \
    "\x52\x50\x8f\xaf\x56\x54\xf0\xac\xaf\x0f\x80\x86" \
    "\xfa\xfa\x82\x1c\x6b\xf0\xe7\xe2\xf8\x5b\xad\x6d" \
    "\xed\x52\xe5\xab\x44\xd7\x75\xa6\xa6\xa6\x00\xb8" \
    "\x5b\x57\x47\x78\x22\xc4\xa7\xc5\x18\x55\xbe\x4a" \
    "\xdb\x00\xf2\x3a\x3e\x54\x52\xc2\x78\x68\x82\xe2" \
    "\x62\x8d\x44\x22\x09\xc0\xf0\xc8\x08\xa6\x69\xb2" \
    "\xba\xba\x4a\x95\xaf\xd2\xf6\xac\x4a\x26\xe2\xb6" \
    "\x1f\x57\x56\x56\x44\xd7\x75\x1c\x0e\x87\xaa\xa9" \
    "\xa9\x15\x80\xa1\xa1\x41\xb5\xb6\xb6\x26\xf3\xf3" \
    "\xf3\xb8\xdd\x6e\x5b\xc7\x96\xf0\x7a\xba\x4c\x31" \
    "\x8c\xb4\x74\x76\x2c\x48\x20\xd0\x22\xe1\xd0\x1e" \
    "\xe6\x66\xb3\x8c\x8f\xa5\xc4\x30\x32\x18\x46\x86" \
    "\xf1\xb1\x94\x7c\x78\xaf\x98\x7e\x77\x9c\x40\xa0" \
    "\x45\x3a\x3b\x16\xc4\x30\xd2\xd2\xd3\x65\x5a\x12" \
    "\xb4\x8c\x22\x1e\xcb\x32\xd0\x9f\xc2\x34\x85\x68" \
    "\x24\x43\x34\x92\x25\x1a\xf9\x61\x71\x32\x33\x9d" \
    "\x66\x66\x3a\x0d\x40\x34\x92\xe1\xd8\x61\x61\xa0" \
    "\x3f\x95\xdf\x71\x63\x93\x93\xb3\xe7\x34\x6e\xdf" \
    "\xd9\xc7\x89\x93\xbb\x98\x9d\x7b\x89\xf7\x86\xc9" \
    "\xc5\x4b\x1a\x0e\x07\x1c\x39\x5a\x44\x43\xa3\x13" \
    "\x5d\xff\x8a\xbe\x3f\xc4\x29\xf7\x6e\x7c\x37\x75" \
    "\xce\x5f\xd0\xf0\xdf\x77\xda\x83\x35\x4d\x71\xda" \
    "\xad\xe1\x3e\xb3\x97\x2b\x97\x6b\xf9\xf6\xfd\x39" \
    "\xf7\xfc\x3e\xde\xbc\x1d\xc5\xe9\x5c\xe6\xcb\xe7" \
    "\x24\xdd\xdd\xc3\x3c\x79\x5a\xcd\xab\xd7\x83\x34" \
    "\x35\xf9\x91\xac\x0b\xef\x75\xa7\x5a\xfc\x98\xb5" \
    "\x80\xf3\x86\x17\x8b\xc5\x64\x72\x72\x92\x89\x70" \
    "\x98\xd1\xd1\x17\x00\x54\x57\xdf\xe2\x9a\xd7\x4b" \
    "\x59\x59\x19\xa5\xa5\xa5\xb6\xe1\xe5\x05\xe7\x64" \
    "\x9a\xa6\xb4\xb6\xb5\x03\xf0\xf8\xd1\x43\x5c\x2e" \
    "\xd7\x96\x17\xc8\x4f\x44\x10\xe9\x77\x45\x2b\x07" \
    "\xdb\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
tbImg_image = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x03" \
    "\x0a\x49\x44\x41\x54\x18\x95\xed\x93\x4d\x4c\x63" \
    "\x55\x14\xc7\x7f\xb7\xef\xb3\x5f\x03\x1d\x28\xa2" \
    "\xce\x8c\xc4\x30\x2c\x30\x71\x63\x82\x93\x68\xba" \
    "\x60\x36\x03\x6c\x0d\x79\x0b\x49\x30\x26\xce\x02" \
    "\x97\x26\x8d\x31\x9a\xb8\x30\xa1\x0a\x1b\xa3\x08" \
    "\x6c\x58\xc8\x24\xac\x5c\xb2\xd1\x14\x42\x33\x13" \
    "\x85\x1a\x94\x08\x52\x1d\x60\xd2\x8a\x33\xb6\x05" \
    "\xa6\xe3\x7b\xed\xb4\xaf\xf4\xba\x60\xac\x61\xa4" \
    "\x8c\xc9\x44\x57\xfe\x37\x37\xb9\xe7\x9e\xdf\x39" \
    "\xf7\xde\xff\x81\x7f\x49\xe2\xe1\x8d\x68\x34\x2a" \
    "\x1f\x17\x1a\x8b\xc5\x84\x7a\x52\x60\x74\x74\xf4" \
    "\x71\xd9\xf2\x44\x30\xc0\xb9\xcb\xaf\xa1\xe8\x5e" \
    "\x50\x54\x90\x35\x3c\x9a\x89\xf0\x78\x8e\x9d\x09" \
    "\xf9\x0d\x34\xd5\x83\x5b\xad\x71\xe0\x94\x01\xd8" \
    "\xfe\xe2\x43\x62\xb1\x18\x0d\xc1\x8a\x37\x88\xd1" \
    "\xfc\x04\xaa\x37\x78\x62\xbc\xb3\xbd\x89\xf3\xad" \
    "\x7e\x02\x86\x86\x5d\x76\xc9\xe4\x1d\x6e\xde\x29" \
    "\xd4\xe3\x0d\xc1\x9a\x6e\x60\x04\x9b\x31\x82\x2d" \
    "\x47\x85\x3c\x47\xdf\x71\x58\x93\x3c\xdd\xd6\xc2" \
    "\x0b\xcf\xb6\xf2\xfc\x85\xb3\xb4\x37\x79\xb9\x53" \
    "\x28\xb1\x96\xde\xc7\xf9\x7a\xf5\xd1\x60\x55\x51" \
    "\xd1\x35\x03\x6f\xa0\x19\x00\xb3\x56\xa2\x29\x14" \
    "\x42\x57\x15\x14\x01\x21\xbf\xc9\x93\xcd\x3e\x5e" \
    "\xec\x0c\xf3\xcd\xcd\x1c\x99\xbd\x22\x7e\xaf\x51" \
    "\xcf\xf7\x00\x7f\xba\xe0\x98\x1b\x74\xc3\x44\x15" \
    "\x1e\x0e\x7f\xcf\x93\x78\xef\x0a\x07\xbf\xed\x92" \
    "\xdd\x2b\x50\xad\x09\xdc\x43\x41\xc9\x95\xe4\xed" \
    "\x0a\x2b\xdb\x7b\xe4\xed\x0a\x25\x57\x72\x28\x3d" \
    "\xc7\xc0\xe2\x01\x54\x48\x29\xeb\xf0\x90\xdf\x24" \
    "\xa0\xc3\x8d\x8f\x5e\x25\x1e\x8f\x93\xfc\xec\x4d" \
    "\x9c\xcc\x26\xfb\xfb\xf7\x48\xff\xbc\x41\x26\xef" \
    "\xb0\x79\xdb\x66\xf5\x56\x81\xcd\xdb\x36\xbb\x07" \
    "\x65\xee\x95\x6a\xc7\xc0\x47\xed\x4a\x29\x85\x10" \
    "\x75\x5f\xeb\x9a\x4a\x7c\xec\x75\x86\x87\x87\x49" \
    "\xa5\x52\x4c\x4c\x4c\xf0\xed\x4c\x14\x51\xb9\xcb" \
    "\x8d\x8f\xdf\xe0\xfb\xe4\x32\xeb\xe9\x02\x6b\xbf" \
    "\xd8\xfc\xf8\x6b\x91\x5b\x7b\x15\x74\x4d\x7b\xf4" \
    "\x1b\x7f\xf5\xe9\x5b\xf4\xf6\xf6\xd2\xd1\xd1\xc1" \
    "\xf2\xf2\x32\x8a\xa2\xd0\xd7\xd7\xc7\x4f\x1b\x1b" \
    "\xbc\xc3\x3a\x4b\x9f\x7c\xc0\xd0\xfb\x9f\x53\x69" \
    "\x7d\x86\x60\x28\x4c\xc0\xd0\x39\x70\xfd\xd8\xb6" \
    "\x7d\x3a\x18\xa0\xbf\xbf\x9f\xf9\xf9\x79\x8a\xc5" \
    "\x22\x9a\xa6\x91\x48\x24\x18\x1a\x1a\x22\x12\x89" \
    "\x30\x32\x32\xc2\xdd\x74\x9a\x2f\x57\x56\x78\xf7" \
    "\xda\x0a\x63\x33\x17\x91\x52\x92\xc9\x7c\x77\x3a" \
    "\xb8\xbb\xbb\x9b\xa5\xa5\x25\xe2\xf1\x38\x00\x03" \
    "\x03\x03\x58\x96\x45\x38\x1c\x66\x7c\x7c\x9c\xc5" \
    "\xc5\x45\xba\xba\xba\x70\x5d\x97\xb1\x99\x8b\xb4" \
    "\xbd\xa4\xe3\xda\x92\x44\x22\x71\x3a\xb8\xf2\xf2" \
    "\x36\x6b\xce\x16\x3d\x3d\x3d\x54\xab\x55\x84\x10" \
    "\x38\x8e\x43\x32\x99\x64\x6b\x6b\x0b\xd7\x75\xc9" \
    "\x9e\x5b\x27\x74\xc9\xe4\xd2\xfd\x57\xe0\xfa\x51" \
    "\xde\xd5\x6b\x57\xb1\x2c\xab\x31\xf8\xa9\xe0\x05" \
    "\xcc\x4e\x85\xdd\xf3\x3f\x70\x3f\x57\x23\x35\x97" \
    "\xa2\x5c\x2e\x13\xba\x5c\xe5\xcc\x15\x93\xe7\xc2" \
    "\x3e\xf4\x80\x8a\x76\x56\xc2\x75\x98\x9d\x9d\x05" \
    "\x20\x12\x89\x90\xcd\x66\x1b\x83\x5b\x7c\xed\xec" \
    "\x06\x56\xf1\x07\x14\x8c\x36\xc1\x99\xb7\x15\xc0" \
    "\x47\xc5\xae\xa2\x07\x54\xa4\xe9\xa2\xf9\x24\xe5" \
    "\xfd\xbf\x2c\x36\x3d\x3d\xcd\xc2\xc2\x02\x73\x73" \
    "\x73\x02\x1e\x1a\x90\x68\x34\x2a\xff\x89\x8a\xc5" \
    "\xa2\xdc\xd9\xd9\x91\x53\x53\x53\x12\x90\x93\x93" \
    "\x93\xd2\xb2\xac\xfa\x1c\xa8\x3c\x18\x0c\x21\x44" \
    "\x7d\x05\x64\x2c\x16\x6b\x74\x99\xbf\x69\x70\x70" \
    "\x90\x5c\x2e\x57\xef\xf4\x7f\xfd\x37\xfa\x03\xef" \
    "\xd9\x5d\xff\x88\xeb\xc7\x39\x00\x00\x00\x00\x49" \
    "\x45\x4e\x44\xae\x42\x60\x82"



from ToolBarManager import *
from UrlDialog_Impl import *
from ImageForm_Impl import *

def initToolbar(self,plugs):
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Bold",makeBold,None,tbBold_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Italic",makeItalic,None,tbItalic_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Underscore",makeUnderscore,None,tbUnder_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Left align",alignLeft,None,tbLeft_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Right align",alignRight,None,tbRight_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Center align",alignCenter,None,tbCenter_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"HR",insertHR,None,tbHr_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"URL",insertUrl,None,tbUrl_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Image",insertImage,None,tbImg_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"BR",insertBR,None,tbBr_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Plus",incFont,None,tbFontPlus_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"Minus",decFont,None,tbFontMinus_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"UL",makeUnorderedList,None,tbUl_image) )
    plugs.manualAdd( ToolbarPlugin.SimpleButton(self,"OL",makeOrderedList,None,tbOl_image) )

def surroundWith(self,tag,param=''):
    text = unicode(self.sourceEditor.selectedText())
    self.sourceEditor.removeSelectedText()
    line, index = self.sourceEditor.getCursorPosition()
    if param != '': 
        tagp = "%s %s" % (tag, param)
    else:
        tagp = tag
    self.sourceEditor.insertAt("<%s>%s</%s>"%(tagp,text,tag), line, index)
    

def makeBold(): surroundWith(qApp.mainWidget(),'b')
    
def makeItalic(): surroundWith(qApp.mainWidget(),'i')

def makeUnderscore(): surroundWith(qApp.mainWidget(),'u')
    
def alignLeft(): surroundWith(qApp.mainWidget(),'div','align="left"')

def alignCenter():surroundWith(qApp.mainWidget(),'div','align="center"')

def alignRight():surroundWith(qApp.mainWidget(),'div','align="right"')

def insertHR():
    self = qApp.mainWidget()
    line, index = self.sourceEditor.getCursorPosition()
    self.sourceEditor.insertAt("<HR>\n", line, index)
    self.sourceEditor.setCursorPosition(line+1,0)

def insertUrl():
    self = qApp.mainWidget()
    text = unicode(self.sourceEditor.selectedText())
    urldialog = UrlDialog_Impl(self)
    urldialog.initValues(text)
    res = urldialog.exec_loop()
    urltag = urldialog.urltag()
    if urltag:
        self.sourceEditor.removeSelectedText()
        line, index = self.sourceEditor.getCursorPosition()
        self.sourceEditor.insertAt(urltag, line, index)
        self.sourceEditor.setCursorPosition(line,index+len(urltag))

def insertImage():
    self = qApp.mainWidget()
    imagedialog = ImageForm_Impl(self)
    res = imagedialog.exec_loop()
    if res:
        imagetag = imagedialog.imagetag()
        if imagetag:
            line, index = self.sourceEditor.getCursorPosition()
            self.sourceEditor.insertAt(imagetag, line, index)
            self.sourceEditor.setCursorPosition(line,index+len(imagetag))


def insertBR():
    self = qApp.mainWidget()
    line, index = self.sourceEditor.getCursorPosition()
    self.sourceEditor.insertAt("<BR>\n", line, index)
    self.sourceEditor.setCursorPosition(line+1,0)
    
def incFont():surroundWith(qApp.mainWidget(),'font','size="+1"')

def decFont():surroundWith(qApp.mainWidget(),'font','size="-1"')

def makeUnorderedList():
    self = qApp.mainWidget()
    text = unicode(self.sourceEditor.selectedText())
    self.sourceEditor.removeSelectedText()
    lines = ["<li>%s</li>"%(line) for line in text.split("\n")]
    newtext = "<ul>\n%s\n</ul>" % ( "\n".join(lines) )
    line, index = self.sourceEditor.getCursorPosition()
    self.sourceEditor.insertAt(newtext, line, index)
    

def makeOrderedList():
    self = qApp.mainWidget()
    text = unicode(self.sourceEditor.selectedText())
    self.sourceEditor.removeSelectedText()
    lines = ["<li>%s</li>"%(line) for line in text.split("\n")]
    newtext = "<ol>\n%s\n</ol>" % ( "\n".join(lines) )
    line, index = self.sourceEditor.getCursorPosition()
    self.sourceEditor.insertAt(newtext, line, index)
