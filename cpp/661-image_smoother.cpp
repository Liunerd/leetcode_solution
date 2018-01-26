class Solution {
public:
    vector<vector<int> > imageSmoother(vector<vector<int>>& M) {
    	vector<vector<int> > ret;
    	copyMatrix(M, ret);
    	if(ret.size() == 0 || ret[0].size() == 0) return ret;
    	int m = ret.size(), n = ret[0].size();
    	for(int i = 0; i < m; ++i) for(int j = 0; j < n; ++j){
    		int count = 1, sum = M[i][j];
    		if(i > 0){ ++count; sum += M[i-1][j]; } // up
    		if(i < m-1){ ++count; sum += M[i+1][j]; } // down
    		if(j > 0){ ++count; sum += M[i][j-1]; } // left
    		if(j < n-1){ ++count; sum += M[i][j+1]; } // right
    		if(i > 0 && j > 0){ ++count; sum += M[i-1][j-1]; } // up-left
    		if(i > 0 && j < n-1){ ++count; sum += M[i-1][j+1]; } // up-right
    		if(i < m-1 && j > 0){ ++count; sum += M[i+1][j-1]; } // down-left
    		if(i < m-1 && j < n-1){ ++count; sum += M[i+1][j+1]; } // down-right
    		ret[i][j] = sum/count;
    	}
    	return ret;
    }
private:
	inline void copyMatrix(vector<vector<int> >& from, vector<vector<int> >& to){
		if(from.size() == 0 || from[0].size() == 0) return;
		for(int i = 0; i < from.size(); ++i){
			vector<int> row(from[i].begin(), from[i].end());
			to.push_back(row);
		}
	}
};