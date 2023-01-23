#  Roman to Integer

dict1={ "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
      }

value=dict1.values()
key=dict1.keys()

roman_int=(list(zip(key,value)))
print(roman_int)