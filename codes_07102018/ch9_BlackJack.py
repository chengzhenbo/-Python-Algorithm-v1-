#coding=utf-8
def black_jack_iterative(cards):
	global n 
	n = len(cards)
	bj_table = {}
	bj_table[n] = 0
	for i in range(n-1, -1, -1):
		bj_table[i] = black_jack(i, bj_table)
	return bj_table
		
def black_jack(i,bj_table):
	if n-i < 4:return 0 #没有足够的扑克
	options = []
	for p in range(0, n-i-3):
		# 玩家尝试抓各种数量的牌
		player_cards = get_player_cards(cards, i, p)
		player = sum(player_cards)
		if player > 21:
			options.append(-1+bj_table[i+4+p])
			break
		# 庄家按照固定的策略抓牌
		for d in range(0, n-i-p-3):
			dealer_cards = get_dealer_cards(cards, i, p, d)
			dealer = sum(dealer_cards)
			if dealer >=17: break
		if dealer > 21: dealer = 0
		options.append(cmp(player, dealer)+bj_table[i+4+p+d])
	return max(options)
	
# 玩家第i位开始抓p张牌
def get_player_cards(cards, i, p):
	player_cards = []
	player_cards.append(cards[i])
	player_cards.append(cards[i+2])
	for k in range(0, p):
		player_cards.append(cards[i+4+k])
	return player_cards
# 庄家第i位开始抓p张牌
def get_dealer_cards(cards, i, p, d):
	dealer_cards = []
	dealer_cards.append(cards[i+1])
	dealer_cards.append(cards[i+3])
	for k in range(0, d):
		dealer_cards.append(cards[i+4+p+k])
	return dealer_cards

# 随机产生n张扑克
def generate_cards(num):
	import random
	hand = [random.randint(1,11) for i in range(num)]
	random.shuffle(hand)
	random.shuffle(hand)
	return hand

def cmp(a, b):
	return (a > b) - (a < b)
	
if __name__ == '__main__':
	cards = generate_cards(50)
	print("input cards = ",cards)
	print (black_jack_iterative(cards))