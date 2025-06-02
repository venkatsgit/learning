class SumPairFinder:
    def __init__(self, array, target_sum):
        self.array = array
        self.target_sum = target_sum
        
        
    def find_all_pairs(self):
        pairs =[]
        for i in range(len(self.array)):
            for j in range(i+1, len(self.array)):
                if self.array[i]+ self.array[j] == self.target_sum:
                  pairs.append({self.array[i], self.array[j]})
        return pairs

if __name__ == "__main__":
    array = [5,6,1, 2, 3, 4,7,8,9,10]
    target_sum = 11
    finder = SumPairFinder(array, target_sum)
    print(finder.find_all_pairs())
