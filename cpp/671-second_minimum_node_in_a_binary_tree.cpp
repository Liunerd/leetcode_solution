/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        vector<int> ret(2, -1);
        helper(root, ret);
        return ret[1];
    }
private:
	void helper(TreeNode* root, vector<int>& ret){
		if(root == NULL) return;
		int v = root -> val;
		if(ret[0] == -1) ret[0] = v;
		else if(ret[0] > v){
			ret[1] = ret[0];
			ret[0] = v;
		}else if(ret[0] < v && (ret[1] == -1 || ret[1] > v)) ret[1] = v;
		helper(root -> left, ret);
		helper(root -> right, ret);
	}
};