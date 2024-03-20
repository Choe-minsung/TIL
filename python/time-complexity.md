# 시간복잡도

![image](https://github.com/Choe-minsung/TIL/assets/145301343/aee2bd39-1767-4b0b-a253-acf7af5ddf1e)

### 표기법
- Big-O
1. O(1) : 상수, n에 따라 변하지않고 항상 상수번 반복
2. O(n) : 1차, n에 따라 증가, for문 1번 사용
3. O(n²) : 2차, n의 제곱에 따라 증가, for문 2번 사용 (=중첩 for문)

### 얼마의 시간복잡도를 갖는가?
- 시간복잡도를 나타내는 T(n)에서 가장 영향력이 큰(dominant)값만을 나타냄  
ex. T(n) = 2n^2 + n + 1일 경우, O(n^2)로 표현
