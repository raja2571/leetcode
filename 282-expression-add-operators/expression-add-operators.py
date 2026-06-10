class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        ans = []

        def dfs(index, expr, value, prev):

            if index == len(num):
                if value == target:
                    ans.append(expr)
                return

            for i in range(index, len(num)):

                # prevent leading zeros
                if i > index and num[index] == "0":
                    break

                cur_str = num[index:i+1]
                cur_num = int(cur_str)

                # first number
                if index == 0:
                    dfs(i + 1,
                        cur_str,
                        cur_num,
                        cur_num)

                else:

                    dfs(i + 1,
                        expr + "+" + cur_str,
                        value + cur_num,
                        cur_num)

                    dfs(i + 1,
                        expr + "-" + cur_str,
                        value - cur_num,
                        -cur_num)

                    dfs(i + 1,
                        expr + "*" + cur_str,
                        value - prev + prev * cur_num,
                        prev * cur_num)

        dfs(0, "", 0, 0)
        return ans