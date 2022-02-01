# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap, ans = [0], 0
        self.heapify(heap, nums)
        while k: ans, k = self.heappop(heap), k-1
        return ans

    def heapify(self, heap, datas):
        for data in datas: self.heappush(heap, data)
           
    def heappush(self, heap, data):
        heap.append(data)
        idx = len(heap)-1
        
        while idx > 0:
            parent_idx = idx // 2
            
            if parent_idx == 0 or (
                heap[idx] <= heap[parent_idx]): break
            self.swap(heap, idx, parent_idx)
            idx = parent_idx
    
    def heappop(self, heap):
        if len(heap) == 2: return heap.pop()
        ans, heap[1] = heap[1], heap.pop()
        idx = 1
        
        while idx < len(heap):
            l_idx, r_idx = 2*idx, 2*idx+1
            max_child_idx = idx
            
            if l_idx < len(heap) and heap[l_idx] > heap[max_child_idx]:
                max_child_idx = l_idx
            if r_idx < len(heap) and heap[r_idx] > heap[max_child_idx]:
                max_child_idx = r_idx
                
            if max_child_idx == idx: break
            else: 
                self.swap(heap, idx, max_child_idx)
                idx = max_child_idx
        return ans

    def swap(self, datas, i, j):
        datas[i], datas[j] = datas[j], datas[i] 
