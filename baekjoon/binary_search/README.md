
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
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2512" target="_blank">2512 / 예산</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |






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






Category 1: Basic / Simple model
Category 2: Model from learning dataset
Category 3: Convolutional Neural Network with real-world image dataset
Category 4: NLP Text Classification with real-world text dataset
Category 5: Sequence Model with real-world numeric dataset

coursera : https://www.coursera.org/professional-certificates/tensorflow-in-practice?action=enroll

https://www.coursera.org/specializations/deep-learning?

1. Tensorflow Basics
Core Skills

Building, compiling, training, evaluating models for binary and muilti- classification
Identifying and mitigating overfitting
Plotting loss and accuracy
Matching input and output shapes
Using early stopping callbacks
Using datasets from tensorflow datasets


https://iyousys.tistory.com/44 텐서플로우 자격증
https://blog.naver.com/hobbang143/221477487359 머신러닝
https://rekt77.tistory.com/102 텐서란 무엇인가
https://iyousys.tistory.com/29 텐서플로우 첫 모델(화씨, 섭씨)
1. 텐서란 무엇인가
수학적인 개념, 데이터의 배열 배열의 차원이 높아질수록, Rank가 높아짐,
바보(1,0,0,0)
정성원을 (0,1,0,0)
안균승을 (0,0,1,0)
이재열을 (0,0,0,1)

정성원 바보 안균승 바보 이재열 바보
[[[0,1,0,0],[1,0,0,0]],[[0,0,1,0],[1,0,0,0]],[[0,0,0,1],[1,0,0,0]]]

문장은 3개
각 문장은 2개의 단어로 구성
단어는 4개

(3,2,4) 3차원 텐서


https://katie0809.github.io/2020/06/16/tf-study2/


① 생략(선형 문제라 다 똑같음, 수치만 다름)
② mnist https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/tutorials/mnist/beginners/
③ CNN
④ sarcasm https://katie0809.github.io/2020/06/22/tf-study4/
⑤ Time Series(강의 문제X)




x.ndim

추가적으로
 
1) 나는 텐서플로우에 익숙하다 → 코세라 강의 추천
2) 나는 텐서플로우를 잘 모르거나 기출 문제로 공부하고 싶다 → 인프런/런어데이 강의 추천

접근 : 인공지능을 이해하고, 텐서플로우로 구현, 과적합을 해결함으로서 좋은 모델을 만들기

2512번. 국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.



n = int(input())
local_list = list(map(int, input().split()))
nation_budget = int(input())

start = 0
end = max(local_list)

    
while start <= end:
    
    mid = (start + end) // 2
    tmp = 0
    
    for local in local_list:
        if local < mid:
            tmp += local
        else:
            tmp += mid
    
    if tmp < nation_budget:
        start = mid + 1
    
    else:
        end = mid - 1 
        
print(end)    

    
    -->
