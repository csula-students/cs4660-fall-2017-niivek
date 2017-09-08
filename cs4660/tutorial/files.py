"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """

        f = open(file_path)
        for line in f:
            self.numbers.append(line.strip().split(" "))


    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        avg = 0
        for x in self.numbers[line_number]:
            print(x)
            avg += x

        avg = avg/len(self.numbers[line_number])
        return avg


    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        lineMax = 0
        for x in self.numbers[line_number]:
            if x > lineMax:
                lineMax = x

        return lineMax

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        lineMin = self.numbers[line_number][0]
        for x in self.numbers[line_number]:
            if x < lineMin:
                lineMin = x

        return lineMin

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        lineSum = 0
        for x in self.numbers[line_number]:
            lineSum += x

        return lineSum

num = []
f = open('../test/fixtures/array.txt', 'r')

for line in f:
    num.append(line.strip().split(" "))

print(num)

line_number = ([100,50,40],[1,2,3],[4,5,6])
avg = 0

for x in line_number[0]:
    avg += x

avg = avg/len(line_number[0])
print("Average Test: %d" % avg)


lineMax = 0
for x in line_number[0]:
    if x > lineMax:
        lineMax = x

print("Line Maximum Test: %d" % lineMax)

lineMin = line_number[0][0]
for x in line_number[0]:
    if x < lineMin:
        lineMin = x

print("Line Mininum Test: %d" % lineMin)

lineSum = 0
for x in line_number[0]:
    lineSum += x

print("Line Sum: %d" %lineSum)