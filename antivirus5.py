import sys
import hashlib
import zlib
import io
import scanmod
import curemod

VirusDB = []    # malware pattern
vdb = []
vsize = []


def decode_kmd(fname):
    try:
        fp = open(fname, 'rb')
        buf = fp.read()
        fp.close()

        buf2 = buf[:-32]
        fmd5 = buf[-32:]

        f = buf2
        for i in range(3):
            if isinstance(f, str):
                f = f.encode()
            md5 = hashlib.md5()
            md5.update(f)
            f = md5.hexdigest()

        if f.encode() != fmd5:
            raise SystemError

        buf3 = buf2[4:]

        buf4 = bytearray()
        for c in buf3:
            buf4.append(c ^ 0xff)

        dcp = zlib.decompress(buf4)
        return dcp
    except SystemError:
        pass

    return None


def load_virus_db():
    buf = decode_kmd('virus.kmd')
    fp = io.StringIO(buf.decode())

    while True:
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        VirusDB.append(line)
    fp.close()


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


if __name__ == '__main__':
    load_virus_db()
    make_virus_db()

    if len(sys.argv) != 2:
        print('Usage: antivirus.py [file]')
        exit(0)

    fname = sys.argv[1]

    ret, vname = scanmod.scan_md5(vdb, vsize, fname)
    if ret:
        print('%s : %s' % (fname, vname))
        curemod.cure_delete(fname)
    else:
        print('%s : ok' % fname)
