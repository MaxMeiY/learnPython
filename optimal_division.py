class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        A = map(str, nums)
        if len(nums) <= 2:
            return '/'.join(A)
        return '{}/({})'.format(A[0], '/'.join(A[1:]))
        