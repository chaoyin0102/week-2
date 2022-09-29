# coding=utf-8
# --------------- 要求1 --------------- 
print("------要求1------")
def calculate(min, max, step):
    sum=0
    for n in range(min,max+1,step):
        sum=sum+n
    print(sum)
calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)


# --------------- 要求2 ---------------
print("------要求2------") 
def avg(data):
    sum=0 # 用來加總薪水
    person=0 #用來計算符合條件的人數
    for i in data["employees"]:
        if i["manager"]==False:
            sum=sum+i["salary"]
            person+=1
    avg=sum/person
    print(avg)

avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
})

# --------------- 要求3 --------------- 
print("------要求3------")
def func(a):
    def func2(b,c):
        print (a+(b*c))
    return func2
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15


# --------------- 要求4 --------------- 
print("------要求4------")
def maxProduct(nums):
    max=nums[0]*nums[1]
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]*nums[j]>max:
                max=nums[i]*nums[j]
    return max
print(maxProduct([5, 20, 2, 6])) # 得到 120
print(maxProduct([10, -20, 0, 3])) # 得到 30
print(maxProduct([10, -20, 0, -3])) # 得到 60
print(maxProduct([-1, 2])) # 得到 -2
print(maxProduct([-1, 0, 2])) # 得到 0
print(maxProduct([5,-1, -2, 0])) # 得到 2
print(maxProduct([-5, -2])) # 得到 10


# --------------- 要求5 ---------------
print("------要求5------")
def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                result=[i,j]
    return result
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9