def is_max_heap(heap):
    n = len(heap)
    last_non_leaf = (n - 2) // 2
    for i in range(last_non_leaf + 1):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n and heap[i] < heap[left_child]:
            return False
        if right_child < n and heap[i] < heap[right_child]:
            return False
    return True

def checkTwoHeaps(A, B):
    return is_max_heap(A) and is_max_heap(B)
