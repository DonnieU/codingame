# There is a rectangle of given width w and height h,

# On the width side, you are given a list of measurements.
# On the height side, you are given another list of measurements.

# Draw perpendicular lines from the measurements to partition the rectangle into smaller rectangles.

# In all sub-rectangles (include the combinations of smaller rectangles), how many of them are squares?


# Example

# w = 10
# h = 5
# measurements on x-axis: 2, 5
# measurements on y-axis: 3

#    ___2______5__________ 
#   |   |      |          |
#   |   |      |          |
#  3|___|______|__________|
#   |   |      |          |
#   |___|______|__________|

# Number of squares in sub-rectangles = 4 (one 2x2, one 3x3, two 5x5)

total_w, total_h, count_x, count_y = [200, 100, 20, 10]
hs = [11, 25, 26, 29, 30, 40, 44, 56, 65, 71, 87, 98, 100, 108, 130, 149, 153, 161, 173, 179, 200]
ws = [1, 11, 16, 17, 19, 37, 38, 53, 65, 69, 100]
# EXPECTED RESULT: 123

"""
# Hi-density
total_w, total_h, count_x, count_y = (10000, 9000, 123, 201)
# hs are horizontal measurements to divide up rectangle
# ws are vertical measurements to divide up rectangle
hs = [1, 14, 79, 126, 390, 506, 573, 690, 747, 778, 798, 887, 896, 907, 912, 1026, 1122, 1172, 1193, 1223, 1380, 1557, 1693, 1759, 1840, 2050, 2063, 2279, 2321, 2332, 2396, 2468, 2514, 2664, 2803, 2813, 2823, 2886, 2913, 3131, 3363, 3426, 3580, 3583, 3780, 3979, 3981, 4014, 4102, 4198, 4284, 4355, 4666, 4693, 4708, 4718, 4926, 5055, 5094, 5121, 5292, 5298, 5299, 5372, 5406, 5532, 5634, 5800, 5801, 5835, 5838, 5851, 5875, 6183, 6305, 6358, 6359, 6433, 6479, 6589, 6600, 6609, 6635, 6766, 6774, 6906, 6940, 6957, 6978, 7004, 7008, 7086, 7226, 7413, 7442, 7525, 7536, 7573, 7625, 7693, 7721, 8004, 8113, 8252, 8300, 8303, 8385, 8390, 8523, 8526, 8688, 8733, 8766, 9027, 9075, 9170, 9196, 9198, 9223, 9331, 9497, 9910, 9945, 10000]
ws = [59, 60, 63, 128, 132, 146, 183, 249, 270, 303, 380, 387, 467, 606, 643, 663, 682, 707, 728, 734, 799, 851, 1019, 1078, 1105, 1116, 1122, 1126, 1167, 1237, 1327, 1402, 1436, 1439, 1635, 1674, 1718, 1751, 1817, 1864, 1865, 1871, 1921, 1995, 2001, 2085, 2089, 2214, 2274, 2282, 2399, 2442, 2443, 2447, 2564, 2569, 2577, 2875, 2937, 2988, 2992, 3017, 3121, 3162, 3202, 3216, 3226, 3228, 3259, 3416, 3426, 3443, 3475, 3795, 3852, 3879, 3920, 3993, 4038, 4039, 4052, 4137, 4207, 4243, 4248, 4251, 4270, 4328, 4346, 4354, 4369, 4379, 4389, 4396, 4413, 4426, 4477, 4491, 4501, 4508, 4531, 4533, 4544, 4659, 4666, 4720, 4769, 4846, 4877, 4977, 5036, 5143, 5254, 5348, 5416, 5425, 5452, 5468, 5523, 5580, 5601, 5611, 5613, 5620, 5714, 5722, 5724, 5748, 5759, 5794, 5803, 5927, 5979, 6042, 6101, 6115, 6168, 6177, 6184, 6230, 6269, 6336, 6343, 6416, 6428, 6709, 6756, 6786, 6813, 6895, 6919, 6945, 6971, 7099, 7114, 7142, 7179, 7241, 7267, 7381, 7401, 7412, 7416, 7422, 7427, 7456, 7514, 7519, 7533, 7555, 7577, 7597, 7735, 7739, 7745, 7777, 7780, 7859, 7913, 7917, 7948, 7984, 7999, 8000, 8035, 8051, 8071, 8143, 8155, 8228, 8392, 8480, 8490, 8575, 8653, 8677, 8731, 8754, 8830, 8867, 8887, 9000]
"""
squares = 0

# Check for same h's and w's which make squares...
# for h in hs:
#     for w in ws:
#         if h == w: squares = squares + 1
squares = len([w for w in ws if w in hs])
# squares = len(list(w for w in ws for h in hs if h==w))

"""
Start at end of (hs) list 
start at end of (hs) list - 1 (h_2)
Find diff between h and h-1 (h_diff)
start at end of (ws) list
if h_diff == ws[w], must be a square
start at end of (ws) list - 1(w_2)
find diff between w and w-1 (w_2_diff)
if h_diff = w_2_diff, must be a square 
"""
# for h in range(len(hs)-1, 0, -1):
#     for h_2 in range(h-1, -1, -1):
#         h_diff = hs[h] - hs[h_2]
        
#         for w in range(len(ws)-1, -1, -1):
#         # # print("w,h: {},{}".format(ws[w],hs[h]))
#             if h_diff == ws[w]: squares = squares + 1
#         #     if h_diff == (ws[w] - ws[w-1]): squares = squares + 1
#             for w_2 in range(w-1, -1, -1):
#                 w_2_diff = ws[w] - ws[w_2]
#                 if h_diff == w_2_diff: squares = squares + 1

""" This works but still slow... """
# for h in range(len(hs)-1,0,-1):
#     for h_2 in range(h-1,-1,-1):
#         squares = squares + len([w for w in range(len(ws)-1,-1,-1) for w_2 in range(w-1,-1,-1) if (hs[h]-hs[h_2])==(ws[w]-ws[w_2])])

# print(list(map(operator.sub, t[1:], t[:-1])))
# print([j-i for i,j in zip(hs[:-1], hs[1:])])
h_diff = [j-i for i,j in zip(hs[:-1], hs[1:])]
h_diff2 = [abs(h-h_2) for h in hs for h_2 in hs]
w_diff = [j-1 for i,j in zip(ws[:-1], ws[1:])]
w_diff2 = [abs(w-w_2) for w in ws for w_2 in ws]

# squares = squares + len([h for h in h_diff if h in ws])
squares = squares + len([h for h in h_diff2 if h in ws])
# squares = squares + len([h for h in h_diff if h in w_diff])
squares = squares + len([h for h in h_diff2 if h in w_diff2])

# print([h for h in range(len(hs-1,0,-1)) for h_2 in range(h-1,-1,-1) for w in range(len(ws)-1,-1,-1) for w_2 in range(w-1,-1,-1) if (hs[h]-hs[h_2])==(ws[w]-ws[w-1]) if (hs[h]-hs[h_2])==(ws[w]-ws[w_2])])
# squares = squares + len([w_2 for w_2 in range(w-1,-1,-1)])
# print(squares)

""" Same as above but starting on (ws) list """
# for w in range(len(ws)-1, 0, -1):
#     for w_2 in range(w-1, -1, -1):
#         w_diff = ws[w] - ws[w_2]
        
#         for h in range(len(hs)-1, -1, -1):
#         # # print("w,h: {},{}".format(ws[w],hs[h]))
#             if w_diff == hs[h]: squares = squares + 1

        #     if h_diff == (ws[w] - ws[w-1]): squares = squares + 1
        
            ### The below section works also if the above compliment
            ### section is commented out. (for w_2 in range...)
            # for h_2 in range(h-1, -1, -1):
            #     h_2_diff = hs[h] - hs[h_2]
            #     if w_diff == h_2_diff: squares = squares + 1

# squares = squares + len([w for w in range(len(ws)-1,0,-1) for w_2 in range(w-1,-1,-1) for h in range(len(hs)-1,-1,-1) if (ws[w]-ws[w_2]) == hs[h]])
# squares = squares + len([w for w in w_diff if w in hs])
# squares = squares + len([w for w in w_diff if w in h_diff])

# print(len([h-h_2 for h in hs for h_2 in hs]))
print(squares)