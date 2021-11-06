import numpy as np
import random


def encryptPlaintext(plaintext, p, g, y):
  convertedPlaintext = [ord(i) for i in plaintext]
  temp = []
  k = random.randint(0, p - 1)
  for i in convertedPlaintext:
      a = (g**k) % p
      b = ((y**k) * i) % p
      temp.append(a)
      temp.append(b)
  return temp

def getRandomPrimeInteger(bounds):
    for i in range(bounds.__len__()-1):
        if bounds[i + 1] > bounds[i]:
            x = bounds[i] + np.random.randint(bounds[i+1]-bounds[i])
            if isPrime(x):
                return x
        else:
            if isPrime(bounds[i]):
                return bounds[i]
        if isPrime(bounds[i + 1]):
            return bounds[i + 1]
    newBounds = [0 for i in range(2*bounds.__len__() - 1)]
    newBounds[0] = bounds[0]
    for i in range(1, bounds.__len__()):
        newBounds[2*i-1] = int((bounds[i-1] + bounds[i])/2)
        newBounds[2*i] = bounds[i]
    return getRandomPrimeInteger(newBounds)

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

def decryptChipertext(string_chipertext, x, p):
  list_chipertext = string_chipertext.split(" ")

  # perulangan dekrip (a b)
  i = 0
  list_plaintext = []
  while i < len(list_chipertext):
      c = pow(int(list_chipertext[i]), int(p) - 1 - int(x)) % int(p)
      m = (int(list_chipertext[i+1]) * c) % int(p)
      list_plaintext.append(m)
      i = i + 2  # lompat 2 untuk a b berikutnya
  # print(list_plaintext)
  convertedPlaintext = [chr(i) for i in list_plaintext]
  plaintext = ''.join(map(str, convertedPlaintext))
  return plaintext

# generate key
#ex: get 50 random prime integers between 100 and 10000:
def getPropertyValues():
  bounds = [1000, 9000]
  p = getRandomPrimeInteger(bounds)
  g = random.randint(0, p - 1)
  x = random.randint(0, p - 1)
  y = (g**x) % p      # public key
  return {"p" : p, "g" : g, "x" : x, "y" : y}