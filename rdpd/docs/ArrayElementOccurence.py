class ArrayElementOccurence:
    def __init__(self, array):
        self.array = array
        
    def find_occurence(self):
        occurence = {}
        for element in self.array:
            if element in occurence:
                occurence[element] += 1
            else:
                occurence[element] = 1
        return sorted(occurence.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,9]
    finder = ArrayElementOccurence(array)
    print(finder.find_occurence())

