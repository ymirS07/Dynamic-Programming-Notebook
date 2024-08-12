public class Solution {
    public int numWays(int n) {
        if (n<= 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int a = 1;
        int b = 2;
        int temp = 0;
        for (int i = 3; i <= n; i++) {
            temp = (a + b)% 1000000007;
            a = b;
            b = temp;
        }
        return temp;
    }
    }
