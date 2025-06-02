class ListNode():
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

class MergeTwoLists(object):
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
    
    def print_linked_list(self, root: ListNode):
        while root != None:
            print(root.val)
            root = root.next
    def make_linked_list(self, int) -> ListNode:
        node = ListNode(int % 10)
        int //= 10
        while int != 0:
            node = ListNode(int % 10, node)
            int //= 10
        return node



    

if __name__ == "__main__":
    merger = MergeTwoLists()
    list1 = merger.make_linked_list(1237)
    list2 = merger.make_linked_list(1289)
    list3 = merger.merge_two_lists(list1, list2)   
    merger.print_linked_list(list3)
