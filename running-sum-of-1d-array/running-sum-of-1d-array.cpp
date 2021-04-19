class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> ret (nums.size());
        int acc = 0;
        for (size_t i = 0; i < nums.size(); ++i) {
            acc += nums[i];
            ret[i] = acc;
        }
        return ret;
    }
};