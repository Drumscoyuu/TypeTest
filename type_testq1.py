# -*- coding: utf-8 -*-
"""Type_TestQ1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XLCWUDfrD01G3xWTi7b_H1AF-2wa32Yq
"""

for num in range(1, 101):
    string = ''
    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
         print("Fizz")

    elif num % 5 == 0:
         print("Buzz")
    
    else:
         print(num)

    print(string)

