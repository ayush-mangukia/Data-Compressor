import pickle

def compressor():
    f1 = open("file.txt","r")

    a_file = open("huffman.pkl", "rb")
    huffman = pickle.load(a_file)
    a_file.close()

    a_file = open("m_words.pkl", "rb")
    words = pickle.load(a_file)
    a_file.close()

    a_file = open("m-n_letters.pkl", "rb")
    letters = pickle.load(a_file)
    a_file.close()

    alp = 'abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789'
    temp = ''

    t = []

    for x in f1:
        for i in x:
            if i in alp:
                temp += i
            else:
                if len(temp) > 0:
                    t.append(temp)
                t.append(i)
                temp = ''

    # print(len(t))

    byte_string = ''

    for i in t:
        if i in words:
            byte_string += huffman[i]
        else:
            for j in i:
                byte_string += huffman[j]

    result = ''
    i = 0
    while i+8 <= len(byte_string):
        result += chr(int(byte_string[i:i+8],2))
        i += 8
    else:
        result += byte_string[i:]

    f2 = open("compressed_file.txt", "w")
    f2.write(result)
    f2.close()