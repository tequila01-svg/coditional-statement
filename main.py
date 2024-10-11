num1=int(input("insert a number: "))
if num1%2==0:
    print("the number is even")
else:
    print("the number is odd")
    
    
 # date and time operations
import datetime   
 
current_time=datetime.datetime.now()
print("the time in WAT is:", current_time)
 
import calendar
 
print("\n", calendar.calendar(2038))