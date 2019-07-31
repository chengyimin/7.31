#基础的while循环
# i = 0
# while i<10:
#     i=i+1
#     print(i)

# 退出循环
# i = 0
# while i < 10:
#     i = i + 1
#     print(i)
#     if i == 5:
#         break
#     else:
#         continue

#任务1：高斯求和
# i = 0
# sum=0
# while i<100:
#     i=i+1
#     sum=sum+i
# print(sum)

#任务2：求1-100内奇数和
# i=1
# sum=1
# while i<99:
#     i=i+2
#     sum=sum+i
# print(sum)

# i=1
# n=101
# while n>0:
#     n=n-2
#     i=i+n
# print(i)

#while遍历hello world！
# s = "hello world!"
# s_len = len(s)
# i=0
# while i < s_len:
#     print(s[i])
#     i=i+1

#for循环遍历hello wrold！
# s = "hello cym！"
# for i in s:
#     print(i)

#for循环遍历列表
# l = [1,2,3,"hello world",32,False,True]
# for i in l:
#     print(i)

#for循环遍历元组
# l = (1,2,3,"hello world",32,False,True)
# for i in l:
#     print(i)

#for循环遍历字典
# l = {"name":"chengyimin","age":21}
# for key in l:
#     print(key,l[key])

#for循环遍历集合
# for i in set([1,2,3,"hello wrold",32,False]):
#     print(i)

#计算0-99中所有整数的和
# sum=0
# for i in range(0,101):
#     sum=sum+i
# print(sum)

#计算0-99中所有奇数的和
# sum=0
# for i in range(1,101,2):
#     sum=sum+i
# print(sum)

#for和range 结合使用
# l1=[1,2,3,4,5,6,7,8,9]
# for i in range(0,len(l1)):
#     print(l1[i])

# 计算0-100中所有整数的和
# i,sum=0,0
# for i in range(0,101):
#     sum=sum+i
# print(sum)

# 计算1-100中所有整数的积
# i,s=1,1
# for i in range(1,101):
#     s=s*i
# print(s)

#定义函数
# def print_result(result):
#     print("result:",result)
#     return len(result)

# l=print_result("你好")
# print(l)




