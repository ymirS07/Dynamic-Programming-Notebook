class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        """
        # initialize 备忘录 dict
        tempDict = {}
       
        # 临界条件
        if n == 0:
            return 1
        if n <= 2:
            return n
        
        # 备忘录里有，无需再次计算
        if n in tempDict:
            return tempDict[n]
        else:
            tempDict[n] = numWays(n - 1) + numWays(n - 2)
            return tempDict[n]

