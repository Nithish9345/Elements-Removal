class ElementRemoval:
    def element(self, array):
        s = 0
        for i in range(len(array)):
            s += sum(array)
            array[i] = 0

        return s

array = list(map(int, input().split()))
array.sort(reverse=True)
object = ElementRemoval()
print(object.element(array))
