import math
import pickle

def count():
    f1 = open("file.txt","r")

    alp = 'abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789'
    count = {}

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

    count_word = {}

    for i in t:
        if len(i) != 0:
            if i not in count_word:
                count_word[i] = 0
            count_word[i] += 1

    count_word = dict(reversed(sorted(count_word.items(), key=lambda item: item[1])))

    n = 0
    for i in count_word:
        n += count_word[i]
        #print(i, count_word[i])

    if n <= 1:
        m = 0

    else:
        m = 1 * math.log2(n) // 1


    c = 0
    count_final = {}

    # print(m, n)

    for i in count_word:
        c += 1
        if c <= m:
            count_final[i] = count_word[i]
        
        if c > m:
            for j in i:
                if j not in count:
                    count[j] = 0
                count[j] += count_word[i]


    a_file = open("m_words.pkl", "wb")
    pickle.dump(count_final, a_file)
    a_file.close()

    # print(count_final)

    a_file = open("m-n_letters.pkl", "wb")
    pickle.dump(count, a_file)
    a_file.close()

    # print(count)

count()
