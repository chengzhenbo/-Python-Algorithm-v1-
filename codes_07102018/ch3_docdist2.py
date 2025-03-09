#coding=utf-8
def get_words_from_line_list(L):
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list.extend(words_in_line)
    return word_list

def inner_product(L1,L2):
    sum = 0.0
    i = 0
    j = 0
    while i<len(L1) and j<len(L2):
        if L1[i][0] == L2[j][0]:
            # 两个都有的单词才计算内积
            sum += L1[i][1] * L2[j][1]
            i += 1
            j += 1
        elif L1[i][0] < L2[j][0]:
            # 单词 L1[i][0] 在 L1 不在 L2
            i += 1
        else:
            # 单词 L2[j][0] 在 L2 但不在 L1
            j += 1
    return sum

def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if D.has_key(new_word):
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D.items()