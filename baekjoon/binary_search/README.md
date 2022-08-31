
이진 탐색(Binary Search)
===

``` 
💡 '정렬된 리스트'에서, 찾고자 하는 값(target)이 중간값(mid)의 왼쪽에 있을까 ? 오른쪽에 있을까 ?
```


### 🔍 Outline
1부터 10까지 숫자에서 2를 찾을 때를 예로 들어본다면,  먼저 중간값인 5를 기준으로 대소 비교를 하는 접근이다<br><br>
2가 5보다 작다면 5의 왼쪽, 2가 5보다 크다면 5의 오른쪽에 있을 것이다. <br><br>
_( 그렇기 때문에 꼭 1부터 10까지의 리스트는 정렬되어 있어야 한다 😃 )_<br><br>
2는 5보다 작은 숫자가 맞다 ! 그렇다면, 1부터 5까지 숫자에서의 중간값인 3을 기준으로 대소 비교를 하는 방식이라는 것 <br><br>





### 🔍 Implementation
재귀함수, while문 (start < end)


### 🔍 Strategy : Parametric Search


어떤 조건을 만족하는 값들 중에 최대, 최소를 찾는 **'최적화 문제'** 를, 이진탐색을 이용하여,

어떻게 **'결정문제(Decision : 예-아니오)'** 로 풀어나갈 수 있을까 ?


<br>

|          순번          |        정답 여부         |        문제 번호 / 이름         |         난이도          |
| :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1789" target="_blank">1789 / 수들의 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2417" target="_blank">2417 / 정수 제곱근</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10815" target="_blank">10815 / 숫자 카드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | 
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2805" target="_blank">2805 / 나무 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1654" target="_blank">1654 / 랜선 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | 





<!--

1654번. 집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.

이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.


n, k = map(int, input().split())
lan_list = []

for _ in range(n):
    lan_list.append(int(input()))
    
start = 0
end = max(lan_list)
answer = 0

    
while start <= end:
    
    mid = (start + end) // 2
    tmp = 0
 
    for lan in lan_list:
        tmp += lan // mid  
    
    if tmp >= k:
        start = mid + 1
    
    else:
        end = mid - 1 
        
print(end)    

    
    -->
