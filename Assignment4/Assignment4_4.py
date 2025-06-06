from functools import reduce

increase = lambda no: no % 2 == 0

square = lambda no: no * no

add = lambda x, y: x + y

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

    fdata = filterx(increase, data)
    print("Filtered even numbers:", fdata)

    mdata = mapx(square, fdata)
    print("Mapped (squared values):", mdata)

    if mdata:
        rdata = reduceX(add, mdata)
        print("Reduced (sum of squares):", rdata)
    else:
        print("Reduce skipped: No data to reduce.")

if __name__ == "__main__":
    main()
