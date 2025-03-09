def collect_contributions(n): #n为需要筹集的款数
  if (n <= 100):
    return 100 #需要此人捐出100元
  else:
    #寻找10个朋友
    friends = find_friend() 
    sum = 0
    for(i=0; i<length(friends); i++):
      #从这10个朋友中分别募集n/10元
      sum += collect_contributions(n/10)
    return sum #返回从10个朋友募集到的资金