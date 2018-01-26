/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
		int carry = 0, addition = 0;
		ListNode *pre = NULL, *temp, *ret;
		while((l1 != NULL) || (l2 != NULL) || carry){
			int val1 = l1 == NULL?0:(l1->val);
			int val2 = l2 == NULL?0:(l2->val); 
			carry += val1+val2;
			temp = new ListNode(carry%10);
            carry /= 10;
			if(pre == NULL) ret = temp; else pre -> next = temp;
			pre = temp;
			l1 = l1 == NULL?NULL:l1->next;
			l2 = l2 == NULL?NULL:l2->next;
		}
		return ret;
    }
};