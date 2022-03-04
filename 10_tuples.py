# tuples are created using ()
# cannot update the value of a tuple. that means tuples are IMMUTABLE(cannot be edited whereas list are mutable and can be updated.)

t=(1,2,3,4,5,6,7,8,9,10)
t1=()              #empty tuple
t2=(1,)            # tuple with single element, for the single element it should always have coma(,) at the end of the value otherwise it will take it as a number.

print(t) 
print(t1)
print(t2)   
print(t[3])
# t[1]=99 this gives an error as tuples are immutable cant be changed.
print(t)