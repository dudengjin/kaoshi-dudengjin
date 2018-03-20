import random
import pygame

# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 960, 539)
# 敌机的定时器事件常量
CREATE_ENEMT_EVENT = pygame.USEREVENT
# 定义一个子弹的常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class Du_Deng_Jin_GameSprite(pygame.sprite.Sprite):
	'''精灵基类'''
	def __init__(self,image_name,speed = 1):
		# 调用父类的初始化方法
		super().__init__()
		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed

	def update(self):
		# 默认在垂直方向移动
		self.rect.x -= self.speed



class Du_Deng_Jin_Background(GameSprite):
	'''背景精灵组'''
	
	def __init__(self,is_alt = False):
		super().__init__("/home/share/deng.jpg")
		if is_alt:
			self.rect.left = -self.rect.width
	
	def update(self):
		# 调用父类方法
		# super().update()
		# 判断是否移除屏幕,如果移除屏幕,将图片移动到上方
		if self.rect.x <= SCREEN_RECT.width:
			self.rect.left = -self.rect.width


class Du_Deng_Jin_Enemy(GameSprite):
	'''敌机精灵类'''
	def __init__(self):
		# 调用父类的方法,创建敌机精灵,并且指定敌机的图像
		super().__init__("/home/dudengjin/a飞机大战.py/images/enemy3.png")
		# 设置敌机的随机初始速度
		self.speed = random.randint(1, 3)
		# 设置敌机的随机初始位置
		self.rect.bottom = 0
		self.rect.x = SCREEN_RECT.width + self.rect.width
		max_ = SCREEN_RECT.height - self.rect.height
		self.rect.y = random.randint(0, max_)

	def update(self):
		# 调用父类的方法,让敌机在垂直方向运动
		super().update()
		# 判断是否飞出屏幕,如果是,需要将敌机从精灵组删除
		if self.rect.y <= 0:
			self.kill()
	'''
	def __del__(self):
		print("敌机挂掉啦%s"%self.rect)
	'''

class Du_Deng_Jin_Hero(GameSprite):
	'''英雄精灵'''
	def __init__(self):
		super().__init__("/home/dudengjin/a飞机大战.py/images/me3.png")
		# 给英雄设置一个初始位置
		self.rect.centery = SCREEN_RECT.centery
		self.rect.left = SCREEN_RECT.y - 20
		self.move = True
		# 创建一个子弹精灵
		self.bullets_group = pygame.sprite.Group()

		
		# 英雄移动 方法1：
		'''
		self.up = False
		self.down = False
		self.left = False
		self.right = False
		'''

	def update(self):
		'''
		if self.up == True:
			self.rect.y -= 5
		elif self.down == True:
			self.rect.y += 5
		elif self.left == True:
			self.rect.x -= 5
		elif self.right == True:
			self.rect.x += 5

		self.rect.x += self.speed
 	 	
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom
		elif self.rect.left <= 0:
			self.rect.left = 0
		elif self.rect.right >= SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		'''

		# 英雄移动 方法2：
		
		
		# 飞机水平移动
		if not self.move:
			self.rect.x += self.speed
		else:
			self.rect.y += self.speed
		# 不能飞出上方
		if self.rect.y <= 0:
			self.rect.y = 0
		# 不能飞出左边
		if self.rect.x <= 0:
			self.rect.x = 0	
		# 不能飞出下边
		if self.rect.bottom >= SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
		# 不能飞出右边
		if self.rect.x >= SCREEN_RECT.width:
			self.rect.x = SCREEN_RECT.width
		
		
	def fire(self):
		print("发射子弹")

		for i in [1,2,3]:
			# 创建子弹
			bullet = Bullet()		
			# 设置子弹的位置
			bullet.rect.left = self.rect.right + 20*i
			bullet.rect.centery = self.rect.centery
			# 将子弹添加到精灵组
			self.bullets_group.add(bullet)


class Du_Deng_Jin_Bullet(GameSprite):
	'''子弹精灵类'''
	def __init__(self):
		# 调用父类方法
		super().__init__("images/bullet1.png")

	def update(self):
		# super().update()
		self.rect.x += 10
		# 判断子弹是否超出屏幕,如果是,我们要让子弹从精灵组删除
		if self.rect.left < SCREEN_RECT.width:
			self.kill()



