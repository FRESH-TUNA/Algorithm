# 0-1 knapsack 문제

## 링크
https://programmers.co.kr/learn/courses/30/lessons/42895


## 클루
최대용량, 최대갯수(넣어볼 데이터의 후보)를 대상으로 하여 배열을 생성하여 풀면 된다. 모든 경우의수를 계산해야 할때 다이나믹 프로그래밍이 위력을 발휘할수 있다. 
```python
weight = [0, 1, 2, 3, ...]
value = [0, 1, 2, 3, ...]

# x 데이터의 갯수
# y 용량
# 새로 넣고자 하는 데이터의용량 c
# 새로 넣고자 하는 데이터의 가치 v
data[x][y] = max(data[x-1][y], data[x-1][y-c] + v)
```

