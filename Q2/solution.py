# record class to help input the records
class Record:
    def __init__(self, num, valid, error_code="true"):
        self.num = num
        self.isValid = valid
        self.error_code = error_code

# solution function


def sol_function():
    # inputs - n: number of records, r: list of records
    n = int(input())
    r = []
    for i in range(n):
        lines = input().split()
        if lines[1] == "false":
            t = Record(int(lines[0]), lines[1], lines[2])
        else:
            t = Record(int(lines[0]), lines[1])
    r.append(t)

    # testing
    # print(r)

    # allValid and errorCodes
    allValid = "Yes"
    errorCodes = []
    for record in r:
        if record.isValid == "false":
            allValid = "No"
            errorCodes.append(record.error_code)

    print(allValid)
    if allValid == "True":
        print(" ".join(errorCodes))


if __name__ == '__main__':
    sol_function()
