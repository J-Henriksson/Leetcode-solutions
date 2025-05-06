#
class ClimbStairs():
    #Runtime: Beats 100% Memory: Beats 30.30%
    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        step_1, step_2 = 1, 2
        for x in range(n - 3):
            step_1, step_2 = step_2, step_1 + step_2
        return step_1 + step_2
