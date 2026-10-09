
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;

        if (!root){
            return levels;
        } 

        queue<TreeNode*> level;
        level.push(root);

        queue<TreeNode*> nextLevel;

        while (!level.empty()) {
            vector<int> newLevel;

            while (!level.empty()) {
                TreeNode* curr = level.front();
                level.pop();

                newLevel.push_back(curr->val);

                if (curr->left) {
                    nextLevel.push(curr->left);
                }

                if (curr->right) {
                    nextLevel.push(curr->right);
                }
            }

            levels.push_back(newLevel);

            level = move(nextLevel);
            nextLevel = queue<TreeNode*>();
        }

        return levels;
    }
};
