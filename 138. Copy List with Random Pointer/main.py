from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        pairs, tmp, index = [], head, 0

        while tmp != None:
            pairs.append((index, tmp.val, tmp.random))
            tmp = tmp.next
        
        tmp = head
        ans = Node(0)
        ans_head = ans

        #initializare lista copy
        while tmp != None:
            ans.next = Node(tmp.val)
            tmp = tmp.next
            ans = ans.next

        index = 0
        tmp = head
        while tmp != None:
            if tmp.random == None:
                index += 1
                tmp = tmp.next
                continue

            tmp2 = ans_head.next
            tmp3 = ans_head.next

            for _ in range(index):
                tmp2 = tmp2.next
                #s a ajuns la nodul curent
            
            for _ in range(tmp.random):
                tmp3 = tmp3.next
                #s a ajuns la nodul tinta
            
            tmp2.random = tmp3
            index += 1
            tmp = tmp.next

        return ans_head.next

def main():
    sol = Solution()

    # Test case 1: Empty list
    head = None
    copied_list = sol.copyRandomList(head)
    print(f"Test case 1 result: {copied_list}")  # Expected: None

    # Test case 2: Single node with no random pointer
    node1 = Node(1)
    head = node1
    copied_list = sol.copyRandomList(head)
    print(f"Test case 2 result: {copied_list.val}")  # Expected: 1
    print(f"Test case 2 random pointer: {copied_list.random}")  # Expected: None

    # Test case 3: Two nodes with random pointers pointing to each other
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node1.random = node2
    node2.random = node1
    head = node1
    copied_list = sol.copyRandomList(head)
    print(f"Test case 3 result: {copied_list.val}, {copied_list.next.val}")  # Expected: 1, 2
    print(f"Test case 3 random pointers: {copied_list.random.val}, {copied_list.next.random.val}")  # Expected: 2, 1

    # Test case 4: Three nodes with random pointers forming a cycle
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node1.random = node3
    node2.random = node1
    node3.random = node2
    head = node1
    copied_list = sol.copyRandomList(head)
    print(f"Test case 4 result: {copied_list.val}, {copied_list.next.val}, {copied_list.next.next.val}")  # Expected: 1, 2, 3
    print(f"Test case 4 random pointers: {copied_list.random.val}, {copied_list.next.random.val}, {copied_list.next.next.random.val}")  # Expected: 3, 1, 2

    # Test case 5: Single node with a random pointer pointing to itself
    node1 = Node(1)
    node1.random = node1
    head = node1
    copied_list = sol.copyRandomList(head)
    print(f"Test case 5 result: {copied_list.val}")  # Expected: 1
    print(f"Test case 5 random pointer: {copied_list.random.val}")  # Expected: 1

if __name__ == '__main__':
    main()