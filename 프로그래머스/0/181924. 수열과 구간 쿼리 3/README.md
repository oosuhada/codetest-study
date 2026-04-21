# [level 0] 수열과 구간 쿼리 3 - 181924 

[문제 링크](https://programmers.co.kr/) 

### 성능 요약

메모리: 9.34 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 04월 07일 18:31:20

### 문제 설명

<p>정수 배열 <code>arr</code>와 2차원 정수 배열 <code>queries</code>이 주어집니다. <code>queries</code>의 원소는 각각 하나의 <code>query</code>를 나타내며, <code>[i, j]</code> 꼴입니다.</p>

<p>각 <code>query</code>마다 순서대로 <code>arr[i]</code>의 값과 <code>arr[j]</code>의 값을 서로 바꿉니다.</p>

<p>위 규칙에 따라 <code>queries</code>를 처리한 이후의 <code>arr</code>를 return 하는 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>arr</code>의 길이 ≤ 1,000

<ul>
<li>0 ≤ <code>arr</code>의 원소 ≤ 1,000,000</li>
</ul></li>
<li>1 ≤ <code>queries</code>의 길이 ≤ 1,000

<ul>
<li>0 ≤ <code>i</code> &lt; <code>j</code> &lt; <code>arr</code>의 길이</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>queries</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[0, 1, 2, 3, 4]</td>
<td>[[0, 3],[1, 2],[1, 4]]</td>
<td>[3, 4, 1, 0, 2]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>각 쿼리에 따라 <code>arr</code>가 다음과 같이 변합니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>arr</th>
</tr>
</thead>
        <tbody><tr>
<td>[0, 1, 2, 3, 4]</td>
</tr>
<tr>
<td>[3, 1, 2, 0, 4]</td>
</tr>
<tr>
<td>[3, 2, 1, 0, 4]</td>
</tr>
<tr>
<td>[3, 4, 1, 0, 2]</td>
</tr>
</tbody>
      </table>
<ul>
<li>따라서 [3, 4, 1, 0, 2]를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

## 🗒️ 풀이 노트

### ❌ 오답 기록

> 틀렸던 코드와 이유를 기록해두세요.

```python
# 오답 코드
```

### ✅ 정답 풀이

> 최종 정답 코드와 핵심 아이디어를 메모하세요.

```python
# 정답 코드
```

### 💡 새로 배운 개념

> 이 문제를 통해 새로 알게 된 함수, 문법, 패턴을 정리하세요.

-

### 🔁 헷갈렸던 부분

> 헷갈렸거나 실수하기 쉬운 부분을 기록하세요.

-

### 📌 다음에 기억할 것

> 다음에 비슷한 문제를 풀 때 떠올려야 할 핵심 포인트를 적어두세요.

-
