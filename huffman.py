import pickle

def huffman():
    a_file = open("m_words.pkl", "rb")
    words = pickle.load(a_file)
    # print(words)

    a_file.close()

    a_file = open("m-n_letters.pkl", "rb")
    letters = pickle.load(a_file)
    # print(letters)

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
    
    # utility function to print huffman
    # codes for all symbols in the newly
    # created Huffman tree
    
    huffman = {}
    
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
            # print(f"{node.symbol} -> {newVal}")
            huffman[node.symbol] = newVal
    
    # list containing unused nodes
    nodes = []
    
    # converting characters and frequencies
    # into huffman tree nodes
    count = 0

    for i in words:
        count += words[i]

    for i in letters:
        count += letters[i]

    for i in words:
        nodes.append(node(words[i]/count, i))

    for i in letters:
        nodes.append(node(letters[i]/count, i))

    if len(nodes) == 1:
        nodes[0].huff = '0'
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)
    
        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]
    
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
    
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    
    # Huffman Tree is ready!
    printNodes(nodes[0])

    a_file = open("huffman.pkl", "wb")
    pickle.dump(huffman, a_file)
    a_file.close()

    c = 0
    c1 = 0

    for i in words:
        c += (words[i] * len(i))
        c1 += (len(huffman[i]) * words[i])

    for i in letters:
        c += letters[i]
        c1 += (len(huffman[i]) * letters[i])

    # print(c, c1//8)