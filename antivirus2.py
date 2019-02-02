import sys
import os
import hashlib

VirusDB = [
    '68:44d88612fea8a8f36de82e1278abb02f:EICAR Test',
    '65:77bff0b143e4840ae73d4582a8914a43:Dummy Test'
]

vdb = []
vsize = []


def make_virus_db():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')
        t.append(v[1])
        t.append(v[2])
        vdb.append(t)

        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)


def search_vdb(fmd5):
    for t in vdb:
        if t[0] == fmd5:
            return True, t[1]
    return False, ''


if __name__ == '__main__':
    make_virus_db()

    if len(sys.argv) != 2:
        print('Usage: antivirus.py [file]')
        exit(0)

    fname = sys.argv[1]

    size = os.path.getsize(fname)
    if vsize.count(size):   # faster
        fp = open(fname, 'rb')
        fb = fp.read()
        fp.close()

        m = hashlib.md5()
        m.update(fb)
        fmd5 = m.hexdigest()

        ret, vname = search_vdb(fmd5)
        if ret:
            print('%s : %s' % (fname, vname))
            os.remove(fname)
        else:
            print('%s : ok' % fname)
    else:
        print('%s : ok' % fname)

