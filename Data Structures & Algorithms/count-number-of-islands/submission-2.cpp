
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int result = 0;
        int m = grid.size();
        int n = grid[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (grid[i][j] == '1') {
                    deque<pair<int, int>> q;
                    q.push_back({i, j});

                    grid[i][j] = '2';

                    while (!q.empty()) {
                        auto [row, col] = q.back();
                        q.pop_back();

                        if (row - 1 >= 0 && grid[row - 1][col] == '1') {
                            grid[row - 1][col] = '2';
                            q.push_back({row - 1, col});
                        }

                        if (row + 1 < m && grid[row + 1][col] == '1') {
                            grid[row + 1][col] = '2';
                            q.push_back({row + 1, col});
                        }

                        if (col - 1 >= 0 && grid[row][col - 1] == '1') {
                            grid[row][col - 1] = '2';
                            q.push_back({row, col - 1});
                        }

                        if (col + 1 < n && grid[row][col + 1] == '1') {
                            grid[row][col + 1] = '2';
                            q.push_back({row, col + 1});
                        }
                    }

                    result++;
                }
            }
        }

        return result;
    }
};
