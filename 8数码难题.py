import math
import copy

class 标准节点:
	def __init__(self):
		self.本节点 = ''
		self.最小g值 = -1
		self.h值 = -1
		self.g值对应的父节点 = ''
		self.子节点 = []
	def toString(self):
		return '本节点:' + self.本节点 + ',最小g值:' + str(self.最小g值) + ',h值:' + str(
			self.h值) + ',此g值对应的父节点:' + self.g值对应的父节点 + ',子节点:' + str(self.子节点)

def 返回所有点坐标(所有点):  # 所有点是一个str类型,含有平方数个元素。返回字典如{'1':[0,0]}
	点列表 = list(所有点)  # 转化为列表
	阶 = math.sqrt(len(点列表))  # 获得数码阶数
	坐标 = {}
	for i in range(len(点列表)):
		坐标.update([(点列表[i], [int(i / 阶), int(i % 阶)])])  # 写入字典
	return 坐标

def 返回所有后继节点(所有点, 空点):  # 得到后继节点的列表
	点列表 = list(所有点)  # 转化为列表
	点列表c = copy.deepcopy(点列表)  # 深拷贝
	阶 = math.sqrt(len(点列表))  # 获得数码阶数
	所有坐标 = 返回所有点坐标(所有点)
	后继节点 = []
	if 所有坐标[空点][0] > 0:  # 判断空点上面是否有点,有则对换
		x = 点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])]
		点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])] = 点列表c[int((所有坐标[空点][0] - 1) * 阶 + 所有坐标[空点][1])]
		点列表c[int((所有坐标[空点][0] - 1) * 阶 + 所有坐标[空点][1])] = x
		后继节点.append(''.join(点列表c))
		点列表c = copy.deepcopy(点列表)  # 深拷贝
	if 所有坐标[空点][0] < 阶 - 1:  # 判断空点下面是否有点,有则对换
		x = 点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])]
		点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])] = 点列表c[int((所有坐标[空点][0] + 1) * 阶 + 所有坐标[空点][1])]
		点列表c[int((所有坐标[空点][0] + 1) * 阶 + 所有坐标[空点][1])] = x
		后继节点.append(''.join(点列表c))
		点列表c = copy.deepcopy(点列表)  # 深拷贝
	if 所有坐标[空点][1] > 0:  # 判断空点左面是否有点,有则对换
		x = 点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])]
		点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])] = 点列表c[int((所有坐标[空点][0]) * 阶 + 所有坐标[空点][1] - 1)]
		点列表c[int((所有坐标[空点][0]) * 阶 + 所有坐标[空点][1] - 1)] = x
		后继节点.append(''.join(点列表c))
		点列表c = copy.deepcopy(点列表)  # 深拷贝
	if 所有坐标[空点][1] < 阶 - 1:  # 判断空点右面是否有点,有则对换
		x = 点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])]
		点列表c[int(所有坐标[空点][0] * 阶 + 所有坐标[空点][1])] = 点列表c[int((所有坐标[空点][0]) * 阶 + 所有坐标[空点][1] + 1)]
		点列表c[int((所有坐标[空点][0]) * 阶 + 所有坐标[空点][1] + 1)] = x
		后继节点.append(''.join(点列表c))
	return 后继节点

def 得到后继节点并化为标准节点(父节点, 目标所有点, 空点,估价函数):  # 父节点类型为标准节点
	后继节点 = 返回所有后继节点(父节点.本节点, 空点)
	标准后继节点 = []
	父节点.子节点 = []
	for i in range(len(后继节点)):
		节点 = 标准节点()
		节点.本节点 = 后继节点[i]
		节点.最小g值 = 父节点.最小g值 + 1
		节点.h值 = 估价函数(节点.本节点, 目标所有点, 空点)
		节点.g值对应的父节点 = 父节点.本节点
		标准后继节点.append(节点)
		父节点.子节点.append(节点.本节点)  # 后继节点添加到父节点
	return 标准后继节点

def 修改子孙g值(标准表, SUC):  # 以SUC的g值为标准。SUC必须属于标准表
	for i in 标准表[SUC.本节点].子节点:
		if SUC.本节点!=标准表[i].g值对应的父节点:
			# if i in open表:raise
			continue  #如果子节点的父节点不再是原来的父节点则不需要变
		else:
			标准表[i].最小g值=SUC.最小g值+1
		if len(标准表[i].子节点)>0:
			修改子孙g值(标准表, 标准表[i])  #如果子节点下还有子节点则深度递归,必须先序遍历

def 节点检测(初始,目标,空点):
	if 空点==' ' or len(空点)!=1:
		print('空点不能为空格且必须等于一个字符!')
		return False
	if 初始.count(空点)!=1:
		print('空点在初始节点中出现了%d次!'%初始.count(空点))
		return False
	if math.sqrt(len(初始))!=int(math.sqrt(len(初始))):
		print('初始节点不是平方数!%d'%len(初始))
		return False
	if math.sqrt(len(目标))!=math.sqrt(len(初始)):
		print('初始节点和目标节点数不同!%d'%len(目标))
		return False
	初始点列表=list(初始)
	目标点列表=list(目标)
	# 求初始节点和目标节点的相对逆序数
	逆序数=0
	阶数=math.sqrt(len(目标))
	for i in range(len(初始点列表)):
		if 初始点列表[i]==空点:continue
		for j in range(目标点列表.index(初始点列表[i])+1):
			if 目标点列表[j]==空点:continue
			if 初始点列表.index(目标点列表[j])>i:
				逆序数+=1
	#奇数阶的逆序数不会改变
	if 阶数%2==1 and 逆序数%2==1:
		print('初始节点无法到达目标节点!')
		return False
	#偶数阶的逆序数要和空点行数的逆序数保持一致
	if 阶数%2==0 and 逆序数%2!=abs(int(初始点列表.index(空点)/阶数)-int(目标点列表.index(空点)/math.sqrt(len(目标))))%2:
		print('初始节点无法到达目标节点!')
		return False

def 主框架(估价函数,是否输出空点=False):
	global 初始节点,目标节点
	初始节点 = 初始节点.replace(' ', '')
	目标节点 = 目标节点.replace(' ','')
	if 节点检测(初始节点, 目标节点,空点)==False:
		return False  #节点不对
	第几步 = 1
	S = 标准节点()
	S.本节点 = 初始节点
	S.最小g值 = 0
	S.h值 = 估价函数(S.本节点, 目标节点, 空点)
	open表.update([(S.本节点, S)])
	while True:
		if len(open表) == 0:
			print('失败')
			break
		# 选取OPEN表中f值最小的节点BESTNODE放入CLOSED表
		最小f值 = -1
		for i in open表:
			if 最小f值 > open表[i].最小g值 + open表[i].h值 or 最小f值 < 0:
				最小f值 = open表[i].最小g值 + open表[i].h值
				最小f值节点 = open表[i].本节点
		close表.update([(最小f值节点, open表[最小f值节点])])
		del open表[最小f值节点]
		BESTNODE = close表[最小f值节点]

		# BESTNODE为目标节点吗？
		if BESTNODE.本节点 == 目标节点:
			print('\r\n成功得到路径:')
			路径 = []
			过程节点 = 目标节点
			while S.本节点 != 过程节点:
				路径.append(过程节点)
				过程节点 = close表[过程节点].g值对应的父节点
				# print(过程节点)
			路径.append(S.本节点)
			#输出过程
			for i in range(len(路径)):
				print('第' + str(i) + '步:')
				输出为阵列(路径[-i - 1], 空点, 是否输出空点)
				print()
			break

		# 扩展BESTNODE ，产生后继节点SUCCESSOR
		SUCCESSOR = 得到后继节点并化为标准节点(BESTNODE, 目标节点, 空点,估价函数)  # SUCCESSOR在其中添加到BESTNODE的后继节点表

		print('BESTNODE-' + str(第几步) + '--' + BESTNODE.toString());
		第几步 += 1
		for i in range(len(SUCCESSOR)):
			print(SUCCESSOR[i].toString())
		print()

		for SUC in SUCCESSOR:
			# SUC ∈ OPEN？
			if SUC.本节点 in open表:
				if SUC.最小g值 < open表[SUC.本节点].最小g值:
					open表[SUC.本节点].g值对应的父节点 = BESTNODE.本节点
					open表[SUC.本节点].最小g值 = SUC.最小g值
			# SUC ∈ CLOSED？
			elif SUC.本节点 in close表:
				if SUC.最小g值 < close表[SUC.本节点].最小g值:  # 每步权值一样且h值公平的话,这里不会为真
					# print('*************************' + close表[SUC.本节点].toString());raise
					close表[SUC.本节点].g值对应的父节点 = BESTNODE.本节点
					close表[SUC.本节点].最小g值 = SUC.最小g值
					修改子孙g值(dict(open表, **close表), close表[SUC.本节点])  # 还有子孙的g值,open表中的不会有子孙
			# 把SUCCESSOR放入OPEN表
			else:
				open表.update([(SUC.本节点, SUC)])
				# print(SUC.toString())

def 输出为阵列(所有点, 空点,是否输出空点):
	点列表 = list(所有点)  # 转化为列表
	阶 = math.sqrt(len(点列表))  # 获得数码阶数
	for i in range(int(阶)):
		for j in range(int(阶)):
			if 是否输出空点:  #输出空点
				print('\t' + 点列表[int(i * 阶 + j)], end='')
			else:  #不输出空点
				if 点列表[int(i * 阶 + j)] != 空点:
					print('\t' + 点列表[int(i * 阶 + j)], end='')
				else:
					print('\t', end='')
		print()

class h函数:
	@staticmethod
	def 迪杰斯特拉算法(*args):
		return 0
	def 曼哈顿距离(所有点1, 所有点2, 空点):  # 保证所有点1和所有点2中的点种类及个数是一样的
		所有坐标1 = 返回所有点坐标(所有点1)
		所有坐标2 = 返回所有点坐标(所有点2)
		距离 = 0
		for i in 所有坐标1:
			if i == 空点: continue
			距离 += pow(abs(所有坐标1[i][0] - 所有坐标2[i][0]) + abs(所有坐标1[i][1] - 所有坐标2[i][1]),1)
		return 距离
	def 平方欧式距离(所有点1, 所有点2, 空点):  # 如果h(x)>h*(s)就不是Astar算法,这种搜索快,但找到的不一定是最优解
		所有坐标1 = 返回所有点坐标(所有点1)
		所有坐标2 = 返回所有点坐标(所有点2)
		距离 = 0
		for i in 所有坐标1:
			if i == 空点: continue
			距离 += abs(pow(所有坐标1[i][0] - 所有坐标2[i][0],2)) + abs(pow(所有坐标1[i][1] - 所有坐标2[i][1],2))
		return 距离

open表 = {}
close表 = {}
初始节点 = '283164705'
目标节点 = '123804765'
空点 = '0'
主框架(h函数.曼哈顿距离)