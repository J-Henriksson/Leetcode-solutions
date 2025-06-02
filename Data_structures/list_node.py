class ListNode():
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next
    
    def print_linked_list(self, root):
        while root != None:
            print(root.val)
            root = root.next
    def make_linked_list_from_int(self, int):
        node = ListNode(int % 10)
        int //= 10
        while int != 0:
            node = ListNode(int % 10, node)
            int //= 10
        return node
    def make_linked_list_from_array(self, list):
        node = ListNode(list.pop())
        for int in reversed(list):
            node = ListNode(int, node)
        return node