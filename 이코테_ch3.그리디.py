# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# <h1>그리디,탐욕법,욕심쟁이 알고리즘 - 당장 가장 좋은것 만을 선택하는 알고리즘</h1><br>
# 현재 상황에서 당장 좋은것만 고르므로 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.<br>
# 문제 출제의 범위가 넓어 그리디의 한 종류인 다익스크라를 제외하고는 단순 암기를 통해 모든 문제를 대체하긴 어렵다.<br>
# 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구하며 자주 정렬 문제와 짝을 이루어 출제된다<br>

# <h3>1.거스름돈</h3>
# 그리디 - 가장 큰 화폐 단위부터 돈을 거슬러 주는 것, 화폐의 종류가 K개일 때 복잡도 O(K), 거슬러 줘야 할 돈의 크기에는 영향없음<br>
# 정당성 - 동전 중 큰 단위가 항상 작은 단위의 배수이므로 작은 단위만으로 새로운 해가 나오지 않는다는 전제가 있어야 함

n = int(input())#거슬러주어야 할 돈
count = 0
coins = [500,100,50,10]
for coin in coins:
    count += n//coin#제일 큰 단위부터 거슬러 줌
    n %= coin#거슬러주고 남은 돈
print(count)

# <h3>2.큰수의법칙</h3>

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
sum,cnt,i = 0,1,0
for _ in range(m):
    if(cnt%(k+1)==0):sum += arr[1]
    else: sum += arr[0]
    cnt += 1
print(sum)

#책답안
n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
cnt = int(m/(k+1))*k#arr[0]이 더해지는 횟수, m을 반복되는 수열길이(k+1)로 나눈 횟수에 수열에서 arr[0]이 등장하는 횟수 k를 곱해 구한다.
cnt += m%(k+1)#나머지에 arr[0]이 등장하는 횟수
sum = 0
sum += cnt*arr[0]
sum += (m-cnt)*arr[1]
print(sum)

# <h3>3.숫자카드게임</h3>

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
min_list = []
for a in arr:
    min_list.append(min(a))
print(max(min_list))

# <h3>4.1이 될 때까지</h3>

n,k = map(int,input().split())
cnt = 0
while(True):
    if(n%k==0):
        n = n // k
    else:
        n -= 1
    cnt += 1
    if(n==1):break
print(cnt)

#책답안
n,k = map(int,input().split())
result = 0
while True:
    #n==k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target
    #n이 k보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
    if n<k: break
    result += 1
    n //= k
result += (n-1)
print(result)
