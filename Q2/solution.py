# record class to help input the records
class Rec:
    def __init__(self, num, valid, error_code="true"):
        self.val = num
        self.isValid = valid
        self.errorCode = error_code

# solution function
def sol_function():
    # inputs - n: number of records, r: list of records
    n = int(input())
    r = []
    for i in range(n):
        lines = input().split()
        if lines[1] == "false":
            t = Rec(int(lines[0]), lines[1], lines[2])
        else:
            t = Rec(int(lines[0]), lines[1])
        r.append(t)

    # testing
    # print(r)

    # allValid and errorCodes
    allValid = "Yes"
    errorCodes = []
    for record in r:
        if record.isValid == "false":
            allValid = "No"
            errorCodes.append(record.errorCode)

    print(allValid)
    if allValid == "No":
        print(" ".join(errorCodes))


if __name__ == '__main__':
    sol_function()
