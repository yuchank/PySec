import sys
import os
import hashlib

VirusDB = []    # malware pattern
vdb = []
vsize = []


def load_virus_db():
    with open('./virus.db') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            VirusDB.append(line)


def make_virus_db():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')
        t.append(v[1])  # MD5 hash
        t.append(v[2])  # name
        vdb.append(t)

        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)


def search_vdb(fmd5):
    for t in vdb:
        if t[0] == fmd5:    # MD5 hash
            return True, t[1]
    return False, ''


if __name__ == '__main__':
    load_virus_db()
    make_virus_db()

    if len(sys.argv) != 2:
        print('Usage: antivirus.py [file]')
        exit(0)

    fname = sys.argv[1]

    size = os.path.getsize(fname)
    if vsize.count(size):   # faster
        with open(fname, 'rb') as fp:
            fb = fp.read()

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

