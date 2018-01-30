class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows < 2) return s;
        string ret = "";
        int len = s.size(), loop = numRows*2-2;
        for(int i = 0; i < len; i += loop) ret.append(1, s[i]);
        for(int line = 1; line < numRows-1; ++line) for(int i = line; i < len; i += loop){
        	ret.append(1, s[i]);
        	int gap = numRows-line+numRows-line-2;
        	if(i + gap < len) ret.append(1, s[i+gap]);
        }
        for(int i = numRows-1; i < len; i += loop) ret.append(1, s[i]);
        return ret;
    }
};