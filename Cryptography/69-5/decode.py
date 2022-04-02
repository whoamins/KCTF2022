import base64

f = open('input_data.txt', 'rb')

code = f.readline()

for i in range(20):
    if i == 0:
        decoded = base64.b64decode(code)

    decoded = base64.b64decode(decoded)

print(decoded)
f.close()
