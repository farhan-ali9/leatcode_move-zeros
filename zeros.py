#first solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i,num in enumerate(nums):
            if num==0:
                nums.remove(0)
                nums.append(0)
#second solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for j,num in enumerate(nums):
            if num!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
