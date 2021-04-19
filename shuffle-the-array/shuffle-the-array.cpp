class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ret;
        for (size_t i = 0; i < nums.size() / 2; ++i) {
            ret.push_back(nums[i]);
            ret.push_back(nums[i+n]);
        }
        return ret;
    }
};