


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        check=False
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    ans.append(i)
                    ans.append(j)
                    check=True
                    break
            if(check):
                break
        return ans
