class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        vector<int> subset;
        dfs(nums, 0, target, 0, result, subset);
        return result;
    }

private:
    void dfs(vector<int>& nums, int currentSum, int target, int start, vector<vector<int>>& result, vector<int>& subset) {
        if (currentSum == target) {
            result.push_back(subset);
            return;
        }

        for (int i = start; i < nums.size(); i++) {
            int newSum = currentSum + nums[i];
            if (newSum <= target) {
                subset.push_back(nums[i]);
                dfs(nums, newSum, target, i, result, subset);
                subset.pop_back();
            }
        }
    }
};