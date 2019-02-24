# -*- coding: utf-8 -*-
import os
import hashlib


def search_vdb(vdb, fmd5):
    for t in vdb:
        if t[0] == fmd5:    # MD5 hash
            return True, t[1]
    return False, ''


def scanmd5(vdb, vsize, fname):
    ret = False     # find malware
    vname = ''

    size = os.path.getsize(fname)
    if vsize.count(size):
        fp = open(fname, 'rb')  # binary mode
        buf = fp.read()
        fp.close()

        m = hashlib.md5()
        m.update(buf)
        fmd5 = m.hexdigest()

        ret, vname = search_vdb(vdb, fmd5)

    return ret, vname
