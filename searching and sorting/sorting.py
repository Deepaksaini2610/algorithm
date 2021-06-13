from stri import merge, mergeSort


class sorting:
    def __init__(self,list):
        self.list = list
    def bubblieSort(self):
        for i in range(len(self.list)):
            for j in range(i+1,len(self.list)):
                if self.list[i] > self.list[j]:
                    list2= self.list[i]
                    self.list[i] = self.list[j]
                    self.list[j] = list2
        # print(time.time())
        print("for bubble sort")
        print(self.list)
    # from typing import List
    def mergeSort(self):
        if len(self.list) <= 1:
            return self.list
        n1 = len(self.list)
        m = n1 // 2
        left_list = self.list[:m]
        right_list = self.list[m:]
        # print (f"{left_list} {right_list}")
        left_list = mergeSort(left_list)
        right_list = mergeSort(right_list)
        return merge(left_list,right_list)
    def merge(self,left,right):
        # left.remove(left[0])
        # print(left)
        emptylist = []
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                emptylist.append(left[0])
                left.remove(left[0])
            else:
                emptylist.append(right[0])
                right.remove(right[0])
        if len(left) == 0:
            emptylist = emptylist + right
        else:
            emptylist = emptylist + left
        return emptylist
    def insertion(self):
    # print(len(list))
        for i in range(1,len(self.list)):
            j = i - 1
            key = self.list[i]
            while key < self.list[j] and j >= 0:
                self.list[j + 1] = self.list[j]
                j = j - 1
                self.list[j+1] = key
        for i in range(len(self.list)):
            print(self.list[i])
        
list = [3,2,1,6,1444,121,43234,8000]
s1 = sorting(list)
l1 = int(input("enter 1 for bubble, 2 for merge and 3 for insertion"))
if l1 == 1:
    s1.bubblieSort()
elif l1 == 2:
    print(s1.mergeSort())
else:
    s1.insertion()