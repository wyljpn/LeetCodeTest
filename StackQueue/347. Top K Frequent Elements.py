import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 要统计元素出现频率
        # nums[i]:对应出现的次数
        map_ = dict()

        for num in nums:
            map_[num] = map_.get(num, 0) + 1

        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = []

        # 用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))

            # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        result = [0] * k

        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]

        return result