class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for key, temp in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and temp > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = key - last
            stack.append(key)

        return result
