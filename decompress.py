import pickle
import copy

def decimalToBinary(n):
    result = bin(n).replace("0b", "")
    while len(result) < 8:
        result = '0' + result

    return result

f1 = open('../code/compressed_file.txt',"r")

a_file = open("huffman.pkl", "rb")
huffman = pickle.load(a_file)
a_file.close()

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (character)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''

def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
        huffman[node.symbol] = newVal

head = node(-1, '')
s = ''

for i in huffman:
    temp = head

    for j in huffman[i]:
        if j == '0':
            if temp.left == None:
                temp.left = node(-1, '')
            temp = temp.left
        else:
            if temp.right == None:
                temp.right = node(-1, '')
            temp = temp.right

        temp.symbol = ''
        temp.freq = -1

    temp.symbol = i
    temp.freq = 1
    temp.huff = huffman[i]

#printNodes(head)

s = ''

byte_string = ''

for x in f1:
    for i in x:
        s += i

i = len(s) - 1

while s[i] == '0' or s[i] == '1':
    i -= 1

while i >= 0:
    byte_string = decimalToBinary(ord(s[i])) + byte_string
    i -= 1

result = ''
i = 0

p = copy.deepcopy(head)

while i < len(byte_string):
    if p == None:
        p = head

    if byte_string[i] == '0':
        p = p.left
    
    if byte_string[i] == '1':
        p = p.right

    #print(byte_string[i], end = '')
        
    if p != None and p.freq == 1:
        result += p.symbol
        p = head
        #print(" ", end='')

    i += 1

f2 = open("decompressed_file1.txt", "w")
f2.write(result)
f2.close()

#decompress