#coding=utf-8
import copy
guyprefers = {
 'm1':  ['w1', 'w2', 'w3'],
 'm2':  ['w1', 'w3', 'w2'],
 'm3':  ['w1', 'w3', 'w2']}
galprefers = {
 'w1':  ['m2', 'm1', 'm3'],
 'w2':  ['m1', 'm2', 'm3'],
 'w3':  ['m3', 'm1', 'm2']}
guys = sorted(guyprefers.keys())
gals = sorted(galprefers.keys())

def matchmaker():
    # 单身男生列表
    guysfree = guys[:]
    # 字典数据结构的配对关系
    engaged  = {}
    # 男生对女生的喜好
    guyprefers2 = copy.deepcopy(guyprefers)
    # 女生对男生的喜好
    galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        guy = guysfree.pop(0)
        # 得到男生guy的偏好列表
        guyslist = guyprefers2[guy]
        # 该男生当前最喜欢的女生
        gal = guyslist.pop(0)
        # 女生gal是否有对象
        fiance = engaged.get(gal)
        # 女生还未配对
        if not fiance:
            # 将男生guy和女生gal配对
            engaged[gal] = guy
            print("  %s and %s" % (guy, gal))
        else:
            # 女生对男生喜好列表
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # 女生更偏好当前的追求者
                engaged[gal] = guy
                print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers2[fiance]:
                    # 前男友进入单身列表
                    guysfree.append(fiance)
            else:
                # 女生更偏好现男友
                if guyslist:
                    # 当前追求者从新寻找下个对象
                    guysfree.append(guy)
    return engaged
 
def check(engaged):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = galprefers[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = guyprefers[he]
        helikesbetter = helikes[:helikes.index(she)]
        for guy in shelikesbetter:
            guysgirl = inverseengaged[guy]
            guylikes = guyprefers[guy]
            if guylikes.index(guysgirl) > guylikes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, guy, he, guysgirl))
                return False
        for gal in helikesbetter:
            girlsguy = engaged[gal]
            gallikes = galprefers[gal]
            if gallikes.index(girlsguy) > gallikes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, gal, she, girlsguy))
                return False
    return True 
print('\nEngagements:')
engaged = matchmaker()
 
print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')
 
print('\n\nSwapping two fiances to introduce an error')
engaged[gals[0]], engaged[gals[1]] = engaged[gals[1]], engaged[gals[0]]
for gal in gals[:2]:
    print('  %s is now engaged to %s' % (gal, engaged[gal]))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')