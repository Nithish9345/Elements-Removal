class ElementRemoval:
    def element(self, array):
        s = 0
        for i in array:
            s += sum(array)
            array[i] = 0

        return s

array = list(map(int, input().split()))
array.sort()
object = ElementRemoval()
print(object.element(array))
