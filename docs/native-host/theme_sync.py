#!/usr/bin/env python3
import sys
import struct
import json
import time
import os

PATH = os.path.expanduser('~/.cache/wal/colors.json')

def send(obj):
    out = json.dumps(obj).encode()
    sys.stdout.buffer.write(struct.pack('=I', len(out)) + out)
    sys.stdout.buffer.flush()

last = None
while True:
    try:
        m = os.path.getmtime(PATH)
        if m != last:
            last = m
            with open(PATH) as fp:
                colors = json.load(fp)
            send({
                "bg": colors['special']['background'],
                "fg": colors['special']['foreground'],
            })
    except Exception:
        pass
    time.sleep(0.2)
