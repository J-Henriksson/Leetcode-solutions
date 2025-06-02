from Data_structures.list_node import ListNode
from typing import List

class MergeKLists():
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        for i in range(len(lists) - 1):
            lists[i + 1] = self.merge_two_lists(lists[i], lists[i + 1])
        if len(lists) > 0:
            return lists[len(lists) - 1]
        return None


    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
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
    merged_list = merger.merge_two_lists(list1, list2)   

    list3 = node.make_linked_list_from_array([1,4,5])
    list4 = node.make_linked_list_from_array([1,3,4])
    list5 = node.make_linked_list_from_array([2,6])
    lists = [list3, list4, list5]
    merged_lists = merger.merge_k_lists(lists)

    node.print_linked_list(merged_lists)