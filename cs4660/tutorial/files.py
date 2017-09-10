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
            avg += float(x)

        avg = avg/len(self.numbers[line_number])
        return float(avg)


    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        lineMax = self.numbers[line_number][0]
        for x in self.numbers[line_number]:
            if x > lineMax:
                lineMax = x

        return int(lineMax)

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        lineMin = self.numbers[line_number][0]
        for x in self.numbers[line_number]:
            if x < lineMin:
                lineMin = x

        return int(lineMin)

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        lineSum = 0
        for x in self.numbers[line_number]:
            lineSum += int(x)

        return int(lineSum)

