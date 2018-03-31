import os
import sys

import xattr

attrname = "user.backup"

def backupstatus(filename):
    attrs = xattr.xattr(filename)
    if attrname in attrs:
        value = attrs[attrname].decode("utf8")
        #print("Found value for {}: {}".format(filename, value))
        if value == "":
            return True
        if value.upper() in ["0", "FALSE", "NO"]:
            return False
        return True
    else:
        return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        start = sys.argv[1]
    else:
        start = os.environ["HOME"]
    for dir, subdirs, files in os.walk(start):
        print(dir)
        for f in files:
            name = os.path.join(dir, f)
            if backupstatus(name):
                print(name)
        idx = 0
        while idx < len(subdirs):
            d = os.path.join(dir, subdirs[idx])
            if backupstatus(d):
                idx += 1
            else:
                del subdirs[idx]
