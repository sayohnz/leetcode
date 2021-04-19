class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ret(candies.size());
        int highest = *max_element(candies.begin(), candies.end());
        for (size_t i = 0; i < candies.size(); ++i)
            ret[i] = candies[i] + extraCandies >= highest;
        return ret;
    }
};