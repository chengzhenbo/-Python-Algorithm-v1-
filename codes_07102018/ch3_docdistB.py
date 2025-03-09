#coding=utf-8
import math
import string

def get_counts(sorted_data):
	counts = []
	for word in sorted_data:
		is_new_word = True
		for entry in counts:
			if word == entry[0]:
				entry[1] += 1
				is_new_word = False
		if is_new_word:
			counts.append([word, 1])
	return counts

def get_inner_product(L1, L2):
    sum = 0.0
    i = 0
    j = 0
    while i<len(L1) and j<len(L2):
        if L1[i][0] == L2[j][0]:
            sum += L1[i][1] * L2[j][1]
            i += 1
            j += 1
        elif L1[i][0] < L2[j][0]:
            i += 1
        else:
            j += 1
    return sum

def get_pairs(words):
	raise NotImplementedError()

translation_table = \
    string.maketrans(string.punctuation+string.uppercase," "*len(string.punctuation)+string.lowercase)

def docdist(path1, path2, use_pairs):
	sorted_data1 = get_sorted_data(path1, use_pairs)
	sorted_data2 = get_sorted_data(path2, use_pairs)
	counts1 = get_counts(sorted_data1)
	counts2 = get_counts(sorted_data2)
	inner_product = get_inner_product(counts1, counts2)
	norm1 = get_inner_product(counts1, counts1)
	norm2 = get_inner_product(counts2, counts2)
	numerator = inner_product
	demominator = math.sqrt(norm1*norm2)
	return math.acos(numerator/demominator)

def get_sorted_data(path, use_pairs):
	text = open(path).read()
	normalized_text = text.translate(translation_table)
	words = normalized_text.split()
	sorted_data = sorted(get_pairs(words) if use_pairs else words)
	return sorted_data

def main(path1="t1.verne.txt", path2="t2.bobsey.txt", use_pairs=""):
	theta = docdist(path1, path2, use_pairs)
	print("angle between document vector is %.3f radians. \n" % theta)

if __name__ == '__main__':
    import cProfile
    cProfile.run("main()")