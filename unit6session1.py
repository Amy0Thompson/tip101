class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

nodes = Node(4, Node(3, Node(2, Node(1))))
palindrome = Node(4, Node(3, Node(3, Node(4))))

def count_element(head, val):
    count = 0
    curr = head
    while curr:
        if curr.value == val:
            count += 1
        curr  = curr.next
    return count

def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next
    current.next = None
    return head

# remove_tail(nodes)
# print_list(nodes)


def find_middle_element(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def is_palindrome(head):
    #4 5 6 5 4 - true
    #a b c b a - true
    #1 2 3 4 - false
    if not head:
        return None
    if not head.next:
        return True
    
    first = head
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    curr = slow
    middle = slow
    prev = None
    
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    print_list(head) #last value removed instead of reversing
    
    firstHalf = first
    secondHalf = middle
    
    while secondHalf:
        if firstHalf.value != secondHalf.value:
            print(firstHalf.value)
            print(secondHalf.value)
            return False
        elif firstHalf.value == secondHalf.value:
            return True
        firstHalf = firstHalf.next
        secondHalf = secondHalf.next
    
print(is_palindrome(palindrome)) #not working....
    
    
    
