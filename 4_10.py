import sys

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_value

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def _sift_down(self, index):
        size = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    commands = data[1:]

    heap = MaxHeap()
    output = []
    i = 0
    while i < len(commands):
        if commands[i] == '0':
            value = int(commands[i + 1])
            heap.insert(value)
            i += 2
        else:
            output.append(str(heap.extract()))
            i += 1

    print('\n'.join(output))

if __name__ == "__main__":
    main()
