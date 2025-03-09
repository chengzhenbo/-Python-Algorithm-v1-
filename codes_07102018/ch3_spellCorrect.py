#coding=utf-8
#!/usr/bin/python

import re, collections

#读入文件
def read_file(filename):
    try:
        fp = open(filename)
        text = fp.read()
    except IOError:
        print ("Error opening or reading input file: ",filename)
        sys.exit()
    return text

#分割文件为单词，并将字母都转换为小写
def words(text):
    return re.findall('[a-z]+', text.lower())

# 该函数计算输入文本每个单词出现的次数
def train(features):
    # 生成了一个默认value=1的带key的数据字典
    model = collections.defaultdict(lambda: 1) 
    for f in features:
        model[f] += 1
    return model

# big文本中每一个单词及其出现的次数
NWORDS = train(words(read_file('big.txt')))

alphabet = 'abcdefghijklmnopqrstxyz'
# 变换输入单词形式，得到那种是最可能的错误
def edist1(word):
    n = len(word)
    return set([word[0:i]+word[i+1: ] for i in range(n)] +                      #删除
               [word[0:i]+word[i+1]+word[i]+word[i+2: ] for i in range(n-1)] +  #错位
               [word[0:i]+c+word[i+1: ] for i in range(n) for c in alphabet] +  #变换
               [word[0:i]+c+word[i: ] for i in range(n+1) for c in alphabet])   #添加
# 在edist1的基础上进一步变换,要去是出现在字典内的词
def known_edist2(word):
    return set(e2 for e1 in edist1(word) for e2 in edist1(e1) if e2 in NWORDS)
# big.txt中已知的单词集合
def known(words):
	wordintxt = set([])
	for w in words:
		if w in NWORDS:
			wordintxt.add(w)
	return wordintxt
    # return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edist1(word)) or known_edist2(word) or [word]
    return max(candidates, key=lambda w:NWORDS[w])


print (correct("acacss"))
# ####test######
# tests1 = { 'access': 'acess', 'accessing': 'accesing', 'accommodation':
#     'accomodation acommodation acomodation', 'account': 'acount'}

# tests2 = {'forbidden': 'forbiden', 'decisions': 'deciscions descisions',
#     'supposedly': 'supposidly', 'embellishing': 'embelishing'}

# def spelltest(tests, bias=None, verbose=False):
#     import time
#     n, bad, unknown, start = 0, 0, 0, time.clock()
#     if bias:
#         for target in tests: NWORDS[target] += bias
#     for target,wrongs in tests.items():
#         for wrong in wrongs.split():
#             n += 1
#             w = correct(wrong)
#             if w!=target:
#                 bad += 1
#                 unknown += (target not in NWORDS)
#                 if verbose:
#                     print '%r => %r (%d); expected %r (%d)' % (
#                         wrong, w, NWORDS[w], target, NWORDS[target])
#     return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), 
#                 unknown=unknown, secs=int(time.clock()-start) )

# print spelltest(tests1)
# print spelltest(tests2) ## only do this after everything is debugged