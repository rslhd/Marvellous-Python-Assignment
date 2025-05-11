def Length(name):
    value = len(name)
    return value

def main():
    print("Enter a name")
    nameX = input()
    result = Length(nameX)

    print("Length of the name is ", result)

if __name__ == "__main__":
    main()        