import base64

s = "Hallo"
b = bytearray()
b.extend(map(ord, s))
c = base64.b64encode(b)
c = base64.b64decode(c)
print(str(c))
