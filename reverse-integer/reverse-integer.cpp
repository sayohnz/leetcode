class Solution {
public:
    int reverse(int x) {
        bool negative = x < 0 ? true : false;
        x = abs(x);
        int64_t ret = 0;
        while (x > 0) {
            if (ret*10 + x%10 > INT_MAX) return 0;
            ret = ret*10 + x % 10;
            x = x / 10;
        }
        return (int) (negative? -ret : ret);
    }
};