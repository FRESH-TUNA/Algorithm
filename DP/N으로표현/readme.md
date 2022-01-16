# 가장 큰 정사각형 찾기 (readme 예제)

## 링크
https://programmers.co.kr/learn/courses/30/lessons/42895


## 클루
N을 k번썻을때 어떤 수들이 생성돨지 점화식을 새워야 한다.

```python
data[N] = (N을 k번 이어붙인수) + (합이 k가되는 data[x]들의 쌍의 사칙연산)
```
이때 0보다 작거나 같은 수는 db에 넣을필요가 없다. 최솟값을 구하는데 필요가 없고 0으로 
나눗셈을 하는 현상을 방지할수 있다.
