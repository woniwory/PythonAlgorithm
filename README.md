
PythonAlgorithm
===




## 🔍 Input 

### input()
기본적으로 input 함수는 str형식으로 입력을 받는 파이썬 내장함수이며, 따라서 정수로 입력을 받아야할 때는 int()를 사용해야한다. <br><br>

또한 '한 줄에 여러 개의 정수를 입력받아야 할 상황'이 굉장히 많기 때문에, map() 함수를 응용하여 입력을 받아올 수 있다 <br><br>

이를 리스트에 한꺼번에 저장하고 싶다면 list()함수로 감싸주면 된다. <br><br>



``` 
💡 list(map(int,input().split()))은 띄어쓰기로 구분된 문자열 요소들을 입력받아(input().split()), <br>
정수로 바꾸어준 다음(map()), 리스트에 모두 저장하겠다는 의미이다.(list())
```






### sys.stdin.readline()

얼마 되지 않는 줄들을 입력받는 문제와는 달리, 반복문으로 여러 개의 테스트케이스를 받아서 문제를 해결해야할 때는 <br><br>

sys 모듈에 있는 sys.stdin.readline()를 사용해야 시간초과를 피할 수 있다. <br><br>

``` 
💡 여러 개의 테스트 케이스를 입력받을 땐 꼭 input().split() 대신 sys.stdin.readline()을 사용하여 시간초과를 피하자.
```



