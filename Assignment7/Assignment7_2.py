def pali(st):
  rev = ""
  for char in st:
    rev = char + rev
  if(st == rev):
    print("Yes")

  else:
    print("No")

def main():
  inW = input("Enter a word ")
  ret = pali(inW)

if __name__ == "__main__":
    main()