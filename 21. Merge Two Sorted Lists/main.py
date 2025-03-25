from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = None

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ans.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ans.next = ListNode(list2.val)
                list2 = list2.next
            ans = ans.next
            if head == None:
                head = ans

        while list1 != None:
            ans.next = list1
            list1 = list1.next
            ans = ans.next
            if head == None:
                head = ans

        while list2 != None:
            ans.next = list2
            list2 = list2.next
            ans = ans.next
            if head == None:
                head = ans

        return head

# Helper function to build a linked list from a list of values.
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for num in values[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Helper function to convert a linked list back into a Python list.
def linked_list_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def main():
    s = Solution()
    # Test case 1: both lists non-empty.
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    merged = s.mergeTwoLists(list1, list2)
    print("Test case 1 result:", linked_list_to_list(merged))
    
    # Test case 2: one empty list, one non-empty.
    list1 = None
    list2 = build_linked_list([0])
    merged = s.mergeTwoLists(list1, list2)
    print("Test case 2 result:", linked_list_to_list(merged))
    
    # Test case 3: both lists empty.
    list1 = None
    list2 = None
    merged = s.mergeTwoLists(list1, list2)
    print("Test case 3 result:", linked_list_to_list(merged))
    
    # Test case 4: lists with one element each.
    list1 = build_linked_list([2])
    list2 = build_linked_list([1])
    merged = s.mergeTwoLists(list1, list2)
    print("Test case 4 result:", linked_list_to_list(merged))

if __name__ == '__main__':
    main()