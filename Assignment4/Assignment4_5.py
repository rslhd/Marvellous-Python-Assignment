def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

double = lambda no: no * 2

maximum = lambda x, y: x if x > y else y

def filterx(task, value):
    result = []
    for no in value:
        if task(no):
            result.append(no)
    return result

def mapx(task, value):
    result = []
    for no in value:
        result.append(task(no))
    return result

def reduceX(task, values):
    result = values[0]
    for no in values[1:]:
        result = task(result, no)
    return result

def main():
    data = []
    print("Enter number of elements:")
    size = int(input())

    print("Enter the numbers:")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Input data:", data)

    fdata = filterx(is_prime, data)
    print("Filtered prime numbers:", fdata)

    mdata = mapx(double, fdata)
    print("Mapped (doubled values):", mdata)

    if mdata:
        rdata = reduceX(maximum, mdata)
        print("Reduced (maximum value):", rdata)
    else:
        print("Reduce skipped: No data to reduce.")

if __name__ == "__main__":
    main()
