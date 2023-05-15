
##check the memory location of your stored variable
q=100; 
print ("below this is the stored value from x")
print (id(q))  ### id represent the value of q stored in the system
print (" ")
print("##########################################################")
print (" ")
## everything in python is an object
#    data type are classes & variables are objects of these classes
#types of data types
# numbers (int, float and complex)
# strings
# Boolean
x=3; y=5.6; z=3+4j
print(x,y,z)
print (x,type(x)); print (y,type(y)); print (z,type(z))
print (" ")
print("##########################################################")
print (" ")

print(" ##########this is a <string> example ##################")
## to define a string in python, we can either use single or double quotation
lan_name='python scripting' ##--> this is a string, therefore should be in quotation
                     # single or double quotation work
print(lan_name,type(lan_name))

my_name="Marius"
print(my_name,type(my_name))
print (" ")
print("##########################################################")
print (" ")

print(" ##########this is a <Boolean> example ##################")
#### only Capital & Capital False are reserved for Booloean
my_value=True
my_new_value=False
## false has quotation in this case, therefore is string, NOT a Boolean
my_other_new_value="False"

## this will print a as boolean
print(my_value,type(my_value))
print(my_new_value,type(my_new_value))

## this will print as a string
print(my_other_new_value,type(my_other_new_value))
print (" ")
print("##########################################################")
print (" ")

print (" ########Typecasting and data conversion ###########")
a=20; aa=0
print(a,type(a))
b=str(a)
print(b,type(b))
print("##########################")
c=bool(a); ab=bool(aa)
print(c,type(c))
print(ab,type(ab))
print (" ")
print("####################  END  #####################")
print (" ")

'''
NOTE: any data type can be converted into boolean
      bool(any_data_type)=True or False
      =================================================
      bool(empty)=False ==> bool(0),bool(None),bool([]),bool({})
      
      bool(non_empty)=True
      exple: bool(100)=True
             bool(0)=False
      ================================================
      
any data type can be converted into A string but reverse is not always true.

'''
