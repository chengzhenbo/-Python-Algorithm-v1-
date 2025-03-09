#coding=utf-8
import math
import string
import sys

def read_file(filename):
    try:
        fp = open(filename)
        L = fp.readlines()
    except IOError:
        print ("Error opening or reading input file: ",filename)
        sys.exit()
    return L

def get_words_from_line_list(L):
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list = word_list + words_in_line
    return word_list

def get_words_from_string(line):
    word_list = []         
    character_list = []     
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list)>0:
            word = "".join(character_list)
            word = str.lower(word)
            word_list.append(word)
            character_list = []
    if len(character_list)>0:
        word = "".join(character_list)
        word = str.lower(word)
        word_list.append(word)
    return word_list

def count_frequency(word_list):
    L = []
    for new_word in word_list:
        for entry in L:
            if new_word == entry[0]:
                entry[1] = entry[1] + 1
                break
        else:
            L.append([new_word,1])
    return L

def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    sorted_freq_mapping = sorted(freq_mapping)

    print ("File",filename,":",)
    print (len(line_list),"lines,",)
    print (len(word_list),"words,",)
    print (len(sorted_freq_mapping),"distinct words")

    return sorted_freq_mapping

def inner_product(L1,L2):
    sum = 0.0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum += count1*count2
    return sum

def vector_angle(L1,L2):
    numerator = inner_product(L1,L2)
    denominator = math.sqrt(inner_product(L1,L1)*inner_product(L2,L2))
    return math.acos(numerator/denominator)

def main():
    filename_1 = "t1.verne.txt"
    filename_2 = "t2.bobsey.txt"
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
    print ("The distance between the documents is: %0.6f (radians)"%distance)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
    # main()
    # L=count_frequency(['to', 'be', 'or','not', 'to', 'be'])
    # print (L)
    # print(get_words_from_string('a cat a 12'))
