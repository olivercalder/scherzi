'''
Meant to extract score images from subdirectories of https://archives.nyphil.org/index.php/artifact/a2bb4cea-cecf-4ab1-8daf-5ba23fc1a23a-0.1
'''

import os
import sys

if len(sys.argv) == 1:
    print('Usage: python3 {} <URL> <pg_count> <name>'.format(sys.argv[0]))
    quit()

else:
    url = sys.argv[1]

    pgs = sys.argv[2]
    if '-' in pgs:
        start, end = pgs.split('-')
        start = int(start)
        end = int(end) 
    else:
        start = 1
        end = int(pgs)

    name = sys.argv[3]

    if not os.path.exists(name):
        os.mkdir(name)

    chunks = url.split('001')

    for i in range(start, end + 1):
        os.system('wget -t 1 -O {0}/{1:03}.jpg "{2}{1:03}{3}"'.format(name, i, chunks[0], chunks[1]))
