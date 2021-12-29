def solution(brown, yellow):
    nums, col = brown + yellow, (brown + yellow) // 3  
    while col >= nums // col:
        # brown 과 yellow로 테두리를 구한다
        if col * (nums // col) == nums and (col + nums // col) * 2 - 4 == brown: return [col, nums // col] 
        col -= 1
