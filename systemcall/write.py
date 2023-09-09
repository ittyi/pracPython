import os

os.write(1, b'h')
tmp = "Hello, World!"
print(tmp)
print(len(tmp))

for i in range(len(tmp)):
    # print(i)
    # print(type(i))
    # print("i.encode('UTF-8')", tmp[i].encode('UTF-8'))
    os.write(1, tmp[i].encode('UTF-8'))

