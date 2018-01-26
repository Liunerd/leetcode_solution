class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pos;
        vector<int> ret(2, 0);
        for(int i = 0; i < nums.size(); ++i){
            int left = target - nums[i];
            if(pos.find(left) != pos.end()){
                ret[0] = pos[left];
                ret[1] = i;
                break;
            }else pos[nums[i]] = i;
        }
        return ret;
    }
};