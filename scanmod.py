# -*- coding: utf-8 -*-
import os
import hashlib


def search_vdb(vdb, fmd5):
    for t in vdb:
        if t[0] == fmd5:    # MD5 hash
            return True, t[1]   # name
    return False, ''


def scan_md5(vdb, vsize, fname):
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


def scan_str(fp, offset, mal_str):
    size = len(mal_str)

    fp.seek(offset)
    buf = fp.read(size)

    if buf.decode() == mal_str:
        return True
    else:
        return False


def scan_virus(vdb, vsize, sdb, fname):
    ret, vname = scan_md5(vdb, vsize, fname)
    if ret:
        return ret, vname

    fp = open(fname, 'rb')
    for t in sdb:
        if scan_str(fp, t[0], t[1]):
            ret = True
            vname = t[2]
            break
    fp.close()

    return ret, vname
