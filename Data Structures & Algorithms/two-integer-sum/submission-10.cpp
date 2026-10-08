class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> remainders;

        for(int i = 0; i < nums.size(); i++){
            int remainder = target - nums[i];
            if(remainders.count(nums[i])){
                return {remainders[nums[i]], i};
            }
            remainders[remainder] = i;
        }

        return {};
    }
};
