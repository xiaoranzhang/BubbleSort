#冒泡排序算法
# 逆序排列

# 排序函数
def bubble(bubble_list):
	list_length=len(bubble_list)   #获得数组长度(个数)
	for bubble_list in range(list_length,0,-1):
		for j in range(list_length-1):                 # 遍历

			if bubble_list[j]>bubble_list[j+1]:    # 如果J>J+1
				TMP=bubble_list[j]                 # 临时存放j的数值
				bubble_list[j]=bubble_list[j+1]    # j与j+1交换位置
				bubble_list[j+1]=TMP               # 读取临时存放的J数值

	print bubble_list

# 程序入口
bubble_list=[3,4,1,2,5,8,0]
bubble(bubble_list)        # 传参，调用函数