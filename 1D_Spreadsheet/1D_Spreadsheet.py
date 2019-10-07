# Accounting is hard 2...
[['MULT', '$61', '$95'], ['ADD', '$26', '$80'], ['ADD', '$6', '$0'], ['ADD', '$98', '$39'], ['ADD', '$72', '$14'], ['SUB', '$12', '$32'], ['MULT', '$73', '$86'], ['ADD', '$80', '$12'], ['MULT', '$86', '$60'], ['SUB', '$39', '$59'], ['SUB', '$64', '$83'], ['SUB', '$98', '$91'], ['SUB', '$59', '$80'], ['MULT', '$65', '$73'], ['ADD', '$25', '$3'], ['ADD', '$93', '$10'], ['SUB', '$93', '$72'], ['MULT', '$43', '$23'], ['MULT', '$43', '$51'], ['MULT', '$71', '$0'], ['SUB', '$60', '$3'], ['ADD', '$77', '$46'], ['SUB', '$23', '$40'], ['MULT', '$99', '$6'], ['MULT', '$44', '$39'], ['VALUE', '$28', '_'], ['VALUE', '$43', '_'], ['ADD', '$92', '$46'], ['ADD', '$49', '$86'], ['SUB', '$82', '$41'], ['ADD', '$12', '$89'], ['ADD', '$91', '$86'], ['SUB', '$60', '$9'], ['MULT', '$51', '$3'], ['SUB', '$12', '$94'], ['ADD', '$12', '$28'], ['ADD', '$66', '$69'], ['SUB', '$53', '$1'], ['ADD', '$98', '$53'], ['ADD', '$98', '$98'], ['ADD', '$42', '$59'], ['SUB', '$64', '$0'], ['SUB', '$98', '$6'], ['MULT', '609', '-14'], ['ADD', '$60', '$55'], ['SUB', '$59', '-245'], ['MULT', '$64', '$1'], ['MULT', '$99', '$98'], ['ADD', '$46', '$97'], ['SUB', '$86', '$43'], ['MULT', '$28', '$18'], ['MULT', '$64', '$40'], ['SUB', '$70', '$32'], ['MULT', '$91', '$80'], ['ADD', '$83', '$6'], ['ADD', '$97', '$76'], ['MULT', '$23', '$45'], ['SUB', '$53', '$22'], ['MULT', '$6', '$10'], ['ADD', '$39', '$98'], ['MULT', '$17', '$26'], ['MULT', '$93', '$59'], ['SUB', '$70', '$99'], ['SUB', '$64', '$43'], ['SUB', '$9', '$9'], ['MULT', '$91', '$53'], ['MULT', '$26', '$80'], ['ADD', '$9', '$43'], ['SUB', '$72', '$13'], ['ADD', '$64', '$82'], ['ADD', '$80', '$45'], ['SUB', '$12', '$61'], ['ADD', '$53', '$73'], ['SUB', '$43', '$98'], ['MULT', '$47', '$86'], ['SUB', '$56', '$99'], ['SUB', '$53', '$51'], ['ADD', '681', '$43'], ['ADD', '$70', '$18'], ['MULT', '$12', '$51'], ['MULT', '$6', '$45'], ['SUB', '$99', '$40'], ['VALUE', '$45', '_'], ['SUB', '$59', '$98'], ['SUB', '$6', '$59'], ['MULT', '$55', '$51'], ['SUB', '$39', '$39'], ['SUB', '$26', '$73'], ['ADD', '$84', '$92'], ['ADD', '$97', '$50'], ['SUB', '$75', '$66'], ['ADD', '$86', '$43'], ['MULT', '295', '$60'], ['MULT', '$31', '$17'], ['SUB', '$9', '$11'], ['SUB', '$87', '$65'], ['MULT', '$64', '$55'], ['MULT', '$49', '$23'], ['MULT', '-6', '380'], ['VALUE', '$53', '_']]

# Deep birecursion...
cells = [['SUB', '$33', '$64'], ['ADD', '$60', '$60'], ['ADD', '$61', '$61'], ['SUB', '$76', '$80'], ['SUB', '$25', '$59'], ['ADD', '$58', '$28'], ['ADD', '$88', '$59'], ['ADD', '$32', '$32'], ['ADD', '$83', '$21'], ['ADD', '$69', '$39'], ['ADD', '$57', '$64'], ['ADD', '$26', '$26'], ['ADD', '$1', '$1'], ['SUB', '$62', '$68'], ['ADD', '$73', '$1'], ['ADD', '$50', '$27'], ['SUB', '$24', '$2'], ['ADD', '$14', '$12'], ['ADD', '$10', '$89'], ['SUB', '$67', '$35'], ['ADD', '$58', '$58'], ['ADD', '$7', '$7'], ['SUB', '$0', '$89'], ['ADD', '$20', '$20'], ['SUB', '$43', '$61'], ['SUB', '$53', '$11'], ['ADD', '$37', '$37'], ['ADD', '$82', '$47'], ['ADD', '$90', '$2'], ['ADD', '$89', '$89'], ['ADD', '$85', '$85'], ['SUB', '$91', '$47'], ['ADD', '$69', '$69'], ['SUB', '$46', '$86'], ['SUB', '$42', '$20'], ['ADD', '$12', '$12'], ['ADD', '$56', '$8'], ['ADD', '$72', '$72'], ['ADD', '$9', '$32'], ['ADD', '$30', '$77'], ['ADD', '$80', '$48'], ['ADD', '$79', '$81'], ['SUB', '$16', '$58'], ['SUB', '$44', '$56'], ['SUB', '$63', '$21'], ['ADD', '$20', '$5'], ['SUB', '$49', '$81'], ['ADD', '$54', '$54'], ['ADD', '$29', '$18'], ['SUB', '$34', '$23'], ['ADD', '$47', '$47'], ['SUB', '$74', '$32'], ['SUB', '$17', '$72'], ['SUB', '$71', '$26'], ['ADD', '$59', '$59'], ['ADD', '$15', '$68'], ['ADD', '$21', '$21'], ['ADD', '$86', '$41'], ['ADD', '$2', '$2'], ['ADD', '$11', '$11'], ['ADD', '$80', '$80'], ['ADD', '$56', '$56'], ['SUB', '$31', '$50'], ['SUB', '$51', '$7'], ['ADD', '$86', '$86'], ['ADD', '$72', '$35'], ['SUB', '$75', '$30'], ['SUB', '$70', '$12'], ['ADD', '$50', '$50'], ['ADD', '$30', '$30'], ['SUB', '$84', '$1'], ['SUB', '$52', '$37'], ['VALUE', '1', '_'], ['ADD', '$40', '$60'], ['SUB', '$66', '$69'], ['SUB', '$13', '$85'], ['SUB', '$22', '$29'], ['ADD', '$55', '$85'], ['ADD', '$37', '$65'], ['ADD', '$23', '$45'], ['ADD', '$29', '$29'], ['ADD', '$23', '$23'], ['ADD', '$54', '$6'], ['ADD', '$38', '$7'], ['SUB', '$3', '$60'], ['ADD', '$68', '$68'], ['ADD', '$81', '$81'], ['ADD', '$78', '$26'], ['ADD', '$87', '$11'], ['ADD', '$64', '$64'], ['ADD', '$61', '$36'], ['SUB', '$4', '$54']]

import sys
import math

# WORKS FOR EVERY TEST!!
dict = {}

def is_int(val, cell_number=None):
    try:
        int(val)
        dict[cell_number] = int(val)
        return True
    except:
        return False 

def do_op(cell, cell_number=None):
    op = cell[0]
    val1 = cell[1]
    val2 = cell[2]

    if op == 'VALUE':
        if is_int(val1, cell_number):
            return val1
        # else it's a reference...
        new_cell = int(val1[1:])
        if dict.get(new_cell):
            new_val1 = dict.get(new_cell)
        else:
            new_val1 = do_op(cells[new_cell], new_cell)
        return int(new_val1)

    if op == 'ADD':
        if not is_int(val1):
            # must be a reference...
            new_cell = int(val1[1:])
            # print('new_cell, cells[{}]: {}, {}'.format(test_cells[new_cell], new_cell, val1))
            if dict.get(new_cell):
                val1 = dict.get(new_cell)
            else:
                val1 = do_op(cells[new_cell], new_cell)
            # print('val1: {}'.format(val1))
        if not is_int(val2):
            # must be a reference...
            new_cell = int(val2[1:])
            if dict.get(new_cell):
                val2 = dict.get(new_cell)
            else:
                val2 = do_op(cells[new_cell], new_cell)
        # print('val1,val2: {},{}'.format(val1, val2))
        dict[cell_number] = int(val1) + int(val2)
        return dict[cell_number]

    if op == 'SUB':
        if not is_int(val1):
            # must be a reference...
            new_cell = int(val1[1:])
            # print('new_cell, cells[{}]: {}, {}'.format(test_cells[new_cell], new_cell, val1))
            if dict.get(new_cell):
                val1 = dict.get(new_cell)
            else:
                val1 = do_op(cells[new_cell], new_cell)
            # print('val1: {}'.format(val1))
        if not is_int(val2):
            # must be a reference...
            new_cell = int(val2[1:])
            if dict.get(new_cell):
                val2 = dict.get(new_cell)
            else:
                val2 = do_op(cells[new_cell], new_cell)
        # print('val1,val2: {},{}'.format(val1, val2))
        dict[cell_number] = int(val1) - int(val2)
        return dict[cell_number]

    if op == 'MULT':
        if not is_int(val1):
            # must be a reference...
            new_cell = int(val1[1:])
            # print('new_cell, cells[{}]: {}, {}'.format(test_cells[new_cell], new_cell, val1))
            val1 = do_op(cells[new_cell], new_cell)
            # print('val1: {}'.format(val1))
        if not is_int(val2):
            # must be a reference...
            new_cell = int(val2[1:])
            val2 = do_op(cells[new_cell], new_cell)
        # print('val1,val2: {},{}'.format(val1, val2))
        # return int(val1) * int(val2)
        dict[cell_number] = int(val1) * int(val2)
        return dict[cell_number]

for i in range(len(cells)):
    print(do_op(cells[i], i))