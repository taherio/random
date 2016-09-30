import re
print '"'+"0x" + ",0x".join(re.findall("..", open("raw_stageless_test", "rb").read().encode("hex")))+'"'
