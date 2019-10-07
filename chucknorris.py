# message = "Chuck Norris' keyboard has 2 keys: 0 and white space."

# bits = []
# for char in message:
#     curr_bits = [bin(ord(char))[2:] for b in char]
#     bits.append(curr_bits[0].zfill(7))
#     # curr_bits = list(curr_bits[0])
#     # print(curr_bits)
#     # bits.append(curr_bits)
# bits = ''.join(bits)
# print(bits)
# res_encoded = []
# res_count = []
# tmp = []

# def do_encoding(bit, length):
#   if (int(bit) & 1):
#     one = '0'
#     res_encoded.append(one)
#   else:
#     zero = '00'
#     res_encoded.append(zero)
#   res_count.append('{}'.format(''.zfill(length)))
  
# prev = bits[0]
# tmp.append(prev)

# for i in range(1, len(bits)):
#   curr = bits[i]

#   # print(bits[i])
#   # print("{}, {}, {}".format(prev, curr, tmp))
#   if i == (len(bits)-1): # last bit check
#     if curr == prev:
#       tmp.append(prev)
#       tmp.append(curr)
#       do_encoding(prev, len(tmp)-1)
#       tmp = []
#     else:
#       do_encoding(prev, 1)
#       do_encoding(curr, 1)
#       tmp = []
#   elif curr != prev:
#     do_encoding(prev, len(tmp))
#     # print(tmp)
#     tmp = []
     
#   prev = curr
#   tmp.append(prev)

# # print(res_encoded)
# # print(res_count)
# tmp = []
# tmp.append(res_encoded[0])
# tmp.append(' ')
# tmp.append(res_count[0])
# for i in range(1, len(res_encoded)):
#   tmp.append(' ')
#   tmp.append(res_encoded[i])
#   tmp.append(' ')
#   tmp.append(res_count[i])
# print(''.join(tmp))


### Works! ###
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