class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for op in operations:

            if op not in ["+", "C", "D"]:
                ans.append(int(op))

            elif op == "+":
                ans.append(ans[-1] + ans[-2])

            elif op == "D":
                ans.append(ans[-1] * 2)

            else:   # "C"
                ans.pop()

        return sum(ans)