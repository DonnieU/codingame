# message = 'CC'
message = "Chuck Norris' keyboard has 2 keys: 0 and white space."
bits = []
for char in message:
    curr_bits = [bin(ord(char))[2:] for b in char]
    bits.append(curr_bits[0].zfill(7))
    # curr_bits = list(curr_bits[0])
    # print(curr_bits)
    # bits.append(curr_bits)
bits = ''.join(bits)
# print("{} {}".format(bits, len(bits)))

res = []
i = 0
curr = int(bits[i])
# print(curr & 1)
# print("before while: {}  {}".format(i, curr))

while i < len(bits):
    if curr & 1:
        res.append('0 ')
        while (i < len(bits)) and (curr & 1):
            res.append('0')
            i += 1
            if i < len(bits):
                curr = int(bits[i])
            # print("In curr & 1: {}  {}".format(i, curr))
            # print(res)
        res.append(' ')
    else:
        res.append('00 ')
        while (i < len(bits)) and (not (curr & 1)):
            res.append('0')
            i += 1
            # print(i)
            if i < len(bits):
                curr = int(bits[i])
            # print("In else: {}  {}".format(i, curr))
        res.append(' ')

    # print(res)
res.pop()
# print(res)
print(''.join(res))

