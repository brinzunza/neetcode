
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subset;
        dfs(nums, subset, 0, result);
        return result;
    }

private:
    void dfs(vector<int>& nums, vector<int>& subset, int index, vector<vector<int>>& result) {
        if (index == nums.size()) {
            result.push_back(subset);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (find(subset.begin(), subset.end(), nums[i]) != subset.end()) {
                continue;
            }
            subset.push_back(nums[i]);
            dfs(nums, subset, index + 1, result);
            subset.pop_back();
        }
    }
};
