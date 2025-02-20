class Solution(object):
    def rotateRight(self, head, k):
        if not head or k==0:
            return head
        N = 1
        result = head
        while result.next:
            N += 1
            result = result.next
        result.next = head
        num = N - k%N
        result = head
        end = None
        for _ in range(num):
            end = result
            result = result.next
        end.next = None
        return result