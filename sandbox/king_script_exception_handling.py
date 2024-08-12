#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

## DONT FORGET TO USE PROPER EXCEPTION HANDLING!! ## 

print("HELLOworld!!")

try:
    data = {'A':1, 'B':2}
    print(data['C'])
except KeyError:
    print('Exception in the code')
finally:
    print('Hit the <finally> code block...')







### HANDLING MORE THAN 1 'TYPE' of EXCEPTION...
try:
    data = {'A':1, 'B':2}
    print(data['C'])
except KeyError:
    print('Exception in the code')
except ZeroDivisionError:
    print('Error Divide by zero attempted')
finally:
    print('Hit the <finally> code block...')