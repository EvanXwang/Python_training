
'''
兩數之和

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''

def twoSum( nums, target):
    dic = dict()
    for index,value in enumerate(nums):
        sub = target - value
        if sub in dic:
            return [dic[sub],index]
        else:
            dic[value] = index

nums = [2,7,11,15]
target = 17
answer = twoSum(nums,target)
print (answer)
