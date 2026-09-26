
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            key = num
            if key not in freq:
                freq[key] = 1
            if key in freq:
                freq[key] +=1
        arr = []
        for num, count in freq.items():
            arr.append([count,num])
        
        arr.sort()

        print(arr)
        re = []
        for i in range(1,k+1):
            re.append(arr[-i][1])
        # print(re)
        return re
 