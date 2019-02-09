# -*- coding: utf-8 -*-

import sys
import zlib
import hashlib


def main():
    if len(sys.argv) != 2:
        print('Usage : kmake.py [file]')
        return

    fname = sys.argv[1]
    tname = fname

    fp = open(tname, 'rb')
    fb = fp.read()
    fp.close()

    #
    cmp = zlib.compress(fb)

    buf = bytearray()
    for c in cmp:
        buf.append(c ^ 0xff)

    buf2 = b'KAVM' + buf

    f = buf2
    for i in range(3):
        if isinstance(f, str):
            f = f.encode()
        md5 = hashlib.md5()
        md5.update(f)
        f = md5.hexdigest()

    buf2 += f.encode()

    kmd_name = fname.split('.')[0] + '.kmd'
    fp = open(kmd_name, 'wb')
    fp.write(buf2)
    fp.close()

    print('%s -> %s' % (fname, kmd_name))

    #

    # fp = open(kmd_name, 'rb')
    # buf = fp.read()
    # fp.close()
    #
    # buf2 = buf[:-32]
    # fmd5 = buf[-32:]
    #
    # f = buf2
    # for i in range(3):
    #     if isinstance(f, str):
    #         f = f.encode()
    #     md5 = hashlib.md5()
    #     md5.update(f)
    #     f = md5.hexdigest()
    #
    # if f.encode() != fmd5:
    #     raise SystemError
    #
    # buf3 = buf2[4:]
    #
    # buf4 = bytearray()
    # for c in buf3:
    #     buf4.append(c ^ 0xff)
    #
    # #
    # dcp = zlib.decompress(buf4)
    #
    # if dcp == fb:
    #     print('comp success')


if __name__ == '__main__':
    main()
