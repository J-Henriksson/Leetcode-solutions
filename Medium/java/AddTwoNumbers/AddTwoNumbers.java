package Medium.java.AddTwoNumbers;


public class AddTwoNumbers {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return numberToListNode(listNodeToLong(l1) + listNodeToLong(l2));
    }

    public long listNodeToLong(ListNode l1) {
        long convertedNumber = 0;
        ListNode nexListNode = l1;
        for (long i = 1; nexListNode != null; i*=10) {
            convertedNumber+= nexListNode.val * i;
            nexListNode = nexListNode.next;
        }
        return convertedNumber;
    }

    public ListNode numberToListNode(long number) {
        ListNode nextListNode = new ListNode();
        ListNode firstListNode = new ListNode((int) (number % 10));

        int length = (number == 0) ? 0 : (int) Math.log10(Math.abs(number)) + 1;
        if (length > 1) {
            firstListNode.next = nextListNode;
            for (int i = 1; i < length; i++) {
                nextListNode.val = (int) ((number / (long) Math.pow(10, i)) % 10);
                if (i != length - 1) {
                    nextListNode.next = new ListNode();
                    nextListNode = nextListNode.next;
                } 
            }
        }

        return firstListNode;
    }






    /**
     * Solution 1
     * Runtime: Beats 100% of all users
     * Memory: Beats 93.31% of all users
     * 
     * Adds two numbers represented by linkedLists and returns the result in its own
     * LinkedList.
     *
     * Adds the values of the linkedLists by adding the two 
     * corresponding nodes from each list and then adding the remainder
     * to the next addition.
     * 
     * @param l1 A linkedList representation of a number (in reversed order).
     * @param l2 A linkedList representation of a number (in reversed order).
     * @return An LinkedList containing the result of the addition.
     */
    public ListNode listNodeAddition(ListNode l1, ListNode l2) {
        ListNode list1 = l1;
        ListNode list2 = l2;

        ListNode firstListNode = list1;

        int value = 0;
        int addToNextValue = 0;

        while (list1.next != null && list2.next != null) {
            value = list1.val + list2.val + addToNextValue;
            addToNextValue = (value / 10) % 10;

            list1.val = value % 10;



            list1 = list1.next;
            list2 = list2.next;
        }

        value = list1.val + list2.val + addToNextValue;
        addToNextValue = (value / 10) % 10;
        list1.val = value % 10;

        if (list1.next == null && list2.next != null) {
            list1.next = list2.next;
            list1 = list1.next;
            while (addToNextValue != 0) {
                value = list1.val + addToNextValue;
                addToNextValue = (value / 10) % 10;
                list1.val = value % 10;
                if (list1.next == null && addToNextValue != 0) {
                    list1.next = new ListNode(addToNextValue);
                    addToNextValue = 0;
                }
                else if (list1.next != null) {
                    list1 = list1.next;
                }
            }
        }
        else if (list1.next != null && list2.next == null) {
            list1 = list1.next;
            while (addToNextValue != 0) {
                value = list1.val + addToNextValue;
                addToNextValue = (value / 10) % 10;
                list1.val = value % 10;
                if (list1.next == null && addToNextValue != 0) {
                    list1.next = new ListNode(addToNextValue);
                    addToNextValue = 0;
                }
                else if (list1.next != null) {
                    list1 = list1.next;
                }
            }
        }
        else if (list1.next == null && list2.next == null && addToNextValue != 0) {
            list1.next = new ListNode(addToNextValue);
            addToNextValue = 0;
        }
        
        return firstListNode;
    }






    public static void main(String[] args) {
        AddTwoNumbers test = new AddTwoNumbers();

        //Test
        ListNode listNode2Node1 = new ListNode(1);

        ListNode listNode3Node3 = new ListNode(1);
        ListNode listNode3Node2 = new ListNode(9, listNode3Node3);
        ListNode listNode3Node1 = new ListNode(9, listNode3Node2);


        
        System.out.println(test.listNodeAddition(listNode2Node1, listNode3Node1));
        //test.listTest(node1);

    }
}
