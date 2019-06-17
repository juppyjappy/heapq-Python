import heapq

#Max ver.


def _siftdown_max(heap, startpos, pos):
    'Maxheap variant of _siftdown'
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if parent < newitem:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def _siftup_max(heap, pos):
    'Maxheap variant of _siftup'
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the larger child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of larger child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[rightpos] < heap[childpos]:
            childpos = rightpos
        # Move the larger child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown_max(heap, startpos, pos)
def _heapify_max(x):
    """Transform list into a maxheap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup_max(x, i)
def _heappush_max(heap, item):
    heap.append(item)
    _siftdown_max(heap, 0, len(heap)-1)
def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup_max(heap, 0)
        return returnitem
    return lastelt


a = [1,7,3,5,4]

#heapify
#配列a = [1,7,3,5,4]をheapにする
_heapify_max(a)
print(a) #[7, 5, 3, 1, 4]

#heappop
#最大値の取り出し
print(_heappop_max(a)) #7
print(a) #[5, 4, 3, 1]

#heappush
#要素(2)の挿入
_heappush_max(a,2)
print(a) #[5, 4, 3, 1, 2]

#最大値の取り出し
print(_heappop_max(a)) #5