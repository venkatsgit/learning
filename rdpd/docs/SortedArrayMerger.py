class SortedArrayMerger:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def merge(self):
        merged_array =[]
        if len(self.array1) == 0:
            merged_array = self.array2
        elif len(self.array2) == 0:
            merged_array = self.array1
        else:
            i=j=0
            while i < len(self.array1) and j < len(self.array2):
                if self.array1[i] < self.array2[j]:
                    merged_array.append(self.array1[i])
                    i=i+1
                else:
                    merged_array.append(self.array2[j])
                    j=j+1
                print(merged_array)
            if(i < len(self.array1)):
                merged_array.append(self.array1[i::])
            if(j < len(self.array2)):
                merged_array.append(self.array2[j::])
        return merged_array


if __name__ == "__main__":
    merger = SortedArrayMerger([1, 3, 5,7,8,9], [2, 4, 6,10,11])
    print(merger.merge())

