class Peakfinder:
    def __init__(self, array):
        self.array = array
        self.peaks = []

    def find_peaks(self):
        if len(self.array) == 0:
            self.peaks = []
        else:
            for i in range(len(self.array)):
                if i !=0 and i != len(self.array)-1:
                    if self.array[i] > self.array[i-1] and self.array[i]> self.array[i+1]:
                        self.peaks.append(self.array[i])
                        i=i+1

if __name__ =="__main__":
    peakfinder = Peakfinder([17, 18, 16, 39, 40, 41, 42 ,43,40])
    peakfinder.find_peaks()
    print(peakfinder.peaks)
