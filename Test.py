# 문제 풀이
def solution(x, n):
    answer = [] # 1. 빈 배열을 만든다.
    for i in range(1,n+1): # 2. i를 1부터 n까지 반복한다.
        answer.append(x*i) # 3. answer에 x*i를 추가한다.
    return answer # 4. 반복문이 종료되고 answer를 반환한다.

# 문제 테스트
if __name__ == "__main__":
    x = 2
    n = 5
    result = solution(x, n)
    print(result) # [2, 4, 6, 8, 10] 출력