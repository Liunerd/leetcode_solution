#define val(c) (c - 'A')
#define pos(s) (val(s[0])*7+ val(s[1]))
class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        bool alw[49][7];
        for(int i = 0; i < 49; ++i) for(int j = 0; j < 7; ++j) alw[i][j] = false;
        for(int i = 0; i < allowed.size(); ++i) alw[pos(allowed[i])][val(allowed[i][2])] = true;
        vector<int> lv1, lv2;
        for(int i = 0; i < bottom.size(); ++i) lv1.push_back(val(bottom[i]));
        return helper(lv1, lv2, 0, alw);
    }
private:
    bool helper(vector<int>& lv1, vector<int>& lv2, int p, bool alw[49][7]){
        if(lv1.size() == 1) return true;
        if(p == lv1.size() - 1){
            vector<int> next;
            return helper(lv2, next, 0, alw);
        }
        for(int i = 0; i < 7; ++i) if(alw[lv1[p]*7+lv1[p+1]][i]){
            lv2.push_back(i);
            if(helper(lv1, lv2, p+1, alw)) return true;
            lv2.pop_back();
        }
        return false;
    }
};