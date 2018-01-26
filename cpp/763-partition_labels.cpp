#define max2(a, b) (a > b ? a : b)
class Solution {
public:
    vector<int> partitionLabels(string S) {
        int len = S.size(), i = 0, j = 0, last = -1;
        int lastof[26] = {-1};
        for(char c = 'a'; c <= 'z'; ++c){
            int k = len - 1;
            while(k >= 0 && S[k] != c) --k;
            lastof[c - 'a'] = k;
        }
        vector<int> ret;
        for(; i < len; ++i){
            j = max2(j, lastof[S[i] - 'a']);
            if(j == i){
                ret.push_back(j - last);
                last = j;
            }
        }
        return ret;
    }
};