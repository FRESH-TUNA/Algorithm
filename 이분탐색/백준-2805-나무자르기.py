N, M = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0

# 높이의 최소가 0이상 1000000000 이하 이기 때문이다.
left, right = 0, 1000000000

# left, right가 같은 경우에도 해야 한다.
# 이진탐색의 경우 그렇게 하잖아
while left <= right:
    mid = left + (right-left)//2

    # 자르는높이가 더 높으면 못짜른다.
    # 자르는 높이가 나무보다 작으면 자를수 있다.
    cutted = sum(0 if mid > tree else tree-mid for tree in trees)

    # M높이 이상이면 답을 갱신해주고
    # 더높은 답을 얻어보기 위해 left를 더 오른쪽으로 댕긴다.
    if cutted >= M:
        answer = max(answer, mid)
        left = mid+1
    else:
        right = mid-1

# 무조건 짜를수 있는 case만 나오기때문에 그냥 반환한다.
print(answer)

