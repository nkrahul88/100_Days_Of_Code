

def prime_checker(number):
  prime = True
  i = 2
  while i != number:
    if number % i == 0:
      prime = False
    i += 1
  if prime:
    print("It is a Prime number")
  else:
    print("It is NOT a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
