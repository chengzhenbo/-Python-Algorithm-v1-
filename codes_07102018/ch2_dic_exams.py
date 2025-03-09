>>> tel = {'jack': 4098, 'sape': 4139}        #构造字典
>>> tel['guido'] = 4127                       #添加新的键值对
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']                               #根据键得到对应的值
4098
>>> del tel['sape']                           #删除一个键值对
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> list(tel.keys())                          #列出所有的键
['irv', 'guido', 'jack']
>>> sorted(tel.keys())                        #按键进行排序
['guido', 'irv', 'jack']
>>> 'guido' in tel                            #某个键是否在字典中
True
>>> 'jack' not in tel
False