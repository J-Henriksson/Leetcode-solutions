from Data_structures.list_node import ListNode
from typing import List

class MergeKLists():
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        for i in range(len(lists) - 1):
            lists[i + 1] = self.merge_two_lists(lists[i], lists[i + 1])
        return lists[len(lists)]


    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1.val > list2.val:
            current_root = list2
            left = list1
            right = list2.next
        else: 
            current_root = list1
            left = list1.next
            right = list2
        current = current_root

        while True:
            if left == None:
                current.next = right
                return current_root
            if right == None:
                current.next = left
                return current_root

            if left.val > right.val:
                current.next = right
                right = right.next
            else: 
                current.next = left
                left = left.next
            current = current.next

if __name__ == "__main__":
    merger = MergeKLists()
    node = ListNode()
    list1 = node.make_linked_list_from_int(1237)
    list2 = node.make_linked_list_from_int(1289)
    list3 = merger.merge_two_lists(list1, list2)   
    node.print_linked_list(list3)