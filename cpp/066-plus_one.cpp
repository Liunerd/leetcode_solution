class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        vector<int> ret;
        int carry = 0;
        int len = digits.size();
        ++digits[len-1];
        carry = digits[len-1]/10;
        digits[len-1] = digits[len-1]%10;
        for(int i = len-2; i >= 0; --i){
            digits[i] += carry;
            carry = digits[i]/10;
            digits[i] = digits[i]%10;
        }
        if(carry){
            ret.push_back(carry);
        }
        for(int i = 0; i < len; ++i){
            ret.push_back(digits[i]);
        }
        return ret;
    }
};