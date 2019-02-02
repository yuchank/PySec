import sys
import os
import hashlib

VirusDB = [
    '44d88612fea8a8f36de82e1278abb02f:EICAR Test',
    '77bff0b143e4840ae73d4582a8914a43:Dummy Test'
]

vdb = []


def make_virus_db():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')
        t.append(v[0])
        t.append(v[1])
        vdb.append(t)


def search_vdb(fmd5):
    for t in vdb:
        if t[0] == fmd5:
            return True, t[1]
    return False, ''


if __name__ == '__main__':
    make_virus_db()
    if len(sys.argv) != 2:
        print('Usage: antivirus.py [file]')

fp = open('./samples/eicar.txt', 'rb')
fb = fp.read()
fp.close()

# if fb[0:3] == b'X5O':
#     print('Virus')
#     os.remove('./samples/2eicar.txt')
# else:
#     print('No Virus')

m = hashlib.md5()
# m.update('hello'.encode('utf-8'))
m.update(fb)
fmd5 = m.hexdigest()
print(fmd5)

if fmd5 == '44d88612fea8a8f36de82e1278abb02f':
    print('Virus')
    os.remove('./samples/eicar.txt')
else:
    print('No Virus')
