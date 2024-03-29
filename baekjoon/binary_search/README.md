
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
while문(start <= end)으로 주로 구현한다. (재귀함수로도 구현 가능) <br><br>
또한 mid 값을 이용해 start와 end값을 조정하여 탐색을 계속 수행한다. <br><br>
이 때 어떤 원소를 리스트에서 '탐색'을 해야하는 경우는, mid를 ((start + end) // 2) **인덱스**로 사용하고, <br><br>
값을 '결정'을 해야하는 경우는 mid 값을 직접 이용해 start, end값을 조정한다. <br><br>

```
💡 찾고자 하는 값(target)이 중간값(mid)의 왼쪽에 있다면, end = mid - 1, 오른쪽에 있다면 start = mid + 1로 재조정될 수 있도록 한다.
```

### 🔍 Strategy : Parametric Search


어떤 조건을 만족하는 값들 중에 최대, 최소를 찾는 **'최적화 문제'** 를, 이진탐색을 이용하여,
어떻게 **'결정문제(Decision : 예-아니오)'** 로 풀어나갈 수 있을까 ? <br><br>
문제가 요구하는 값이 어떤 조건을 만족하면서도 최댓값/최솟값을 구해야하고, 답의 범위가 연속적이고 이산적이라면 의심해보자. <br><br>

```
💡 '연속적이다'는 문제를 해결할 때 sort() 메소드로 구현할 수 있으며, '이산적이다'는 문제가 정수로 주어진다는 뜻을 염두에 두자. 
```
<br><br>
예를 들어, 성원이는 바게뜨를 정말 좋아한다. 바게뜨는 길이가 길수록 비싸지기 때문에 <br><br>
성원이는 길이가 **20cm 이상의 바게뜨들 중에 최솟값**을 사려고 한다 
<br><br>
최솟값을 구하려고 할 때, '20cm 보다 긴 길이는 모두 조건을 만족하면서, (최댓값의 문제의 경우 그 값보다 작은 값은 모두 조건을 만족)<br><br>
더 큰 값들을 이분탐색'하면서 답을 구해보는 방식이라는 것이다.




<br><br>


|          순번          |        정답 여부         |        문제 번호 / 이름         |         난이도          |
| :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1789" target="_blank">1789 / 수들의 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2417" target="_blank">2417 / 정수 제곱근</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10815" target="_blank">10815 / 숫자 카드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |
| 03 |    | <a href="https://www.acmicpc.net/problem/10816" target="_blank">10816 / 숫자 카드2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1920" target="_blank">1920 / 수 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | 
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2805" target="_blank">2805 / 나무 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1654" target="_blank">1654 / 랜선 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | 
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2512" target="_blank">2512 / 예산</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 08 |    | <a href="https://www.acmicpc.net/problem/7795" target="_blank">7795 / 먹을 것인가 먹힐 것인가</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1072" target="_blank">1072 / 게임</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |
| 10 |    | <a href="https://www.acmicpc.net/problem/1072" target="_blank">3079 / 입국심사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |



<!--



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



시간복잡도, 빅오표기법 구현
    
    -->
