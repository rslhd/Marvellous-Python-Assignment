def Predict(chars):
    if(chars == "a" or chars == "e" or chars == "i" or chars == "o" or chars == "u"):
        print("It is a vowel")

    else:
        print("It is a consonant")    

def main():
    character = input("Enter a single character ")
    Predict(character)

if __name__ == "__main__":
    main()            