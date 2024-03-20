# 시간복잡도

![image](https://github.com/Choe-minsung/TIL/assets/145301343/aee2bd39-1767-4b0b-a253-acf7af5ddf1e)

### 표기법
- Big-O
1. O(1) ex.해시테이블 : 상수, n에 따라 변하지않고 항상 상수번 반복
2. O(n) ex.리스트 1번 완전탐색 : 선형 (1차), n에 따라 증가, for문 1번 사용
3. O(n²) ex.리스트 2번 완전탐색 : 제곱 (2차), n의 제곱에 따라 증가, for문 2번 사용 (=중첩 for문)
4. O(2ⁿ) ex.방향이없는 그래프(undirected-graph) n개 채색 : 지수 (n차), 매우 비효율
5. O(log n) ex.이진 탐색 : 로그, 입력이 10ⁿ 배 커져도 시간은 선형적으로 n배 커짐

### 얼마의 시간복잡도를 갖는가?
- 시간복잡도를 나타내는 T(n)에서 가장 영향력이 큰(dominant)값만을 나타냄  
ex. T(n) = 2n^2 + n + 1일 경우, O(n^2)로 표현

### Dominance 순서
O(1) < O(logn) < O(n) < O(nlogn) < O(n²) < O(cⁿ) < O(n!)
