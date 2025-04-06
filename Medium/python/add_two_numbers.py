class ListNode():
    def __init__(self, val: int, next):
        self.val = val
        self.next = next

class AddTwoNumbers():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> int:
        """Adds two numbers represented by linked lists and returns the result as a linked list. Since the nodes given as parameters represent the first digits of the 2 numbers, the function
        adds their values and stores their remainder, while looping through the values from each list the previous remainder is added to their value. The loop stops once both lists don't have any 
        remaining values and the remainder is 0.

        Analysis: Overall a pretty decent solution. Pretty intuitive and scores good on the leetcode comparison thingy.
        Runtime: Beats 84.70%
        Memory: Beats 84.30%

        Args:
            l1 (ListNode): ListNode containing one of the numbers to be added.
            l2 (ListNode): ListNode containing the other number to be added.

        Returns:
            start_node (ListNode): The node of the first number of the result.
        """
        node_l1 = l1.next
        node_l2 = l2.next
        node = ListNode((l1.val + l2.val) % 10, None)
        remainder = (l1.val + l2.val) // 10
        start_node = node

        while node_l1 != None or node_l2 != None or remainder != 0:
            sum = 0
            if node_l1 != None:
                sum += node_l1.val
                node_l1 = node_l1.next
            if node_l2 != None:
                sum += node_l2.val
                node_l2 = node_l2.next
            new_node = ListNode((sum + remainder) % 10, None)
            remainder = (sum + remainder) // 10
            node.next = new_node    
            node = node.next
    
        return start_node

if __name__ == "__main__":
    l13 = ListNode(3, None)
    l12 = ListNode(4,l13)
    l11 = ListNode(2,l12)
    l23 = ListNode(4, None)
    l22 = ListNode(6,l23)
    l21 = ListNode(5,l22)

    add_two_numbers = AddTwoNumbers()

    print(add_two_numbers.addTwoNumbers(l11, l21).val)
    print(add_two_numbers.addTwoNumbers(l11, l21).next.val)
    print(add_two_numbers.addTwoNumbers(l11, l21).next.next.val)