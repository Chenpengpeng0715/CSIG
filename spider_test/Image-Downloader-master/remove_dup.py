# /usr/bin/env python
# -*- coding:utf-8 -*-
import os
import hashlib
 
 
def md5sum(filename):
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        fb = f.read(8096)
        if not fb:
            break
        md5.update(fb)
    f.close()
    return (md5.hexdigest())
 
def delfile():
    all_md5 = {}
    filedir = os.walk('D:/Image-Downloader-master/download_images')
    
                
                
    for i in filedir:
        for tlie in i[2]:
            tlie = os.path.join(i[0], tlie)
            if md5sum(tlie) in all_md5.values():
                os.remove(tlie)
            else:
                all_md5[tlie] = md5sum(tlie)
 
if __name__ == '__main__':
    delfile()
