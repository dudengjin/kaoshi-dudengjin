import random


class du_deng_jin(object):
	count = 1

	computer = random.randint(0, 99)
	user_num = input("请输入一个数字") 

	if user_num == computer:
		print("猜中,是否继续游戏")
	elif user_num >= computer:
		print("猜小")
	elif user_num <= computer:
		print("猜大")	
	
		count += 1	