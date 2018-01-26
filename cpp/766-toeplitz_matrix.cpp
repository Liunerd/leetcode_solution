#define min2(a, b) (a < b ? a : b)
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        if(matrix.size() == 0 || matrix[0].size() == 0) return false;
        int m = matrix.size(), n = matrix[0].size(), v = matrix[0][0];
        for(int i = 1; i < min2(m, n); ++i) if(matrix[i][i] != v) return false;
        return true;
    }
};