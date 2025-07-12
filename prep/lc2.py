# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# idea here is that we use a two pointer approach to add the two numbers
# we use a left pointer to add the first number and a right pointer to add the second number
# we move the left pointer to the right and the right pointer to the left
# if the sum of the two numbers is greater than 9, we carry the 1 to the next digit
# if the sum of the two numbers is less than 10, we add the sum to the result list
# we return the result list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a dummy head node to simplify the linked list construction
    dummy_head = ListNode()
    # Current pointer to build the result linked list
    current = dummy_head
    # Carry from previous addition (0 or 1)
    carry = 0

    # Continue while there are digits to process or there's a carry
    while l1 or l2 or carry:
        # Get values from current nodes (0 if node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        # Calculate total sum including carry from previous step
        total = val1 + val2 + carry
        # Calculate new carry for next iteration
        carry = total // 10
        # Create new node with the ones digit of the sum
        current.next = ListNode(total % 10)
        # Move current pointer to the newly created node
        current = current.next
        
        # Move to next nodes in both linked lists (if they exist)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # Return the actual head of the result linked list (skip dummy head)
    return dummy_head.next
