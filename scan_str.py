# -*- coding: utf-8 -*-


def scan_str(fp, offset, mal_str):
    size = len(mal_str)

    fp.seek(offset)
    buf = fp.read(size)

    if buf == mal_str:
        return True
    else:
        return False


fp = open('samples/dummy.txt', 'rb')
print(scan_str(fp, 0, b'Dum'))
fp.close()
