import heapq
class NLargestNumFinder:
    def __init__(self, list):
        self.list = list

    def find(self, n):
        heapq.heapify(self.list)
        print(self.list)

if __name__ == "__main__":
    print(NLargestNumFinder([9,909,98,12,24]).find(3))


