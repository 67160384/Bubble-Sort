class BubbleSorter:
    def __init__(self,nums):
        self.array = nums

    def sort(self):
        n = len(self.array)
        for i in range(0,n-1):
            for j in range(0,n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            print(f"After round {i + 1}:", self.array)

    def display(self):
        print("Current data:", self.array)

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)
    print("Before sorting:")
    sorter.display()
    print()

    sorter.sort()
    print()
    print("After sorting:")
    sorter.display()
