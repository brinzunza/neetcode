class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {

        vector<int> result(cost.size() + 1, 0);
        result[0] = 0;
        result[1] = 0;

        for (int i = 2; i < cost.size() + 1; i++){
            result[i] = min(result[i - 1] + cost[i - 1], result[i - 2] + cost[i - 2]);
        }

        return result.back();
    }
};
