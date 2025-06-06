from functools import reduce

increase = lambda no: 70 <= no <= 90
add = lambda no: no + 10
product = lambda x, y: x * y

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


def reduceX(task,values):
    result=1

    for no in values:
        result= task(result,no)
        
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
    print("Filter output:", fdata)

    mdata = mapx(add, fdata)
    print("Map data:", mdata)

    
    rdata = reduceX(product,mdata)
    print("reduce : ",rdata)

if __name__ == "__main__":
    main()
