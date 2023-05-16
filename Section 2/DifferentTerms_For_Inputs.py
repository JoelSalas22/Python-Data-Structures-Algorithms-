# This would be O(2n) dropping the constant we would get O(n)

def print_items(n):
	for i in range(n):
		print(i)

	for j in range(n):
		print(j)

    
# Similar question asked during interviews
# Can't say a == n and b == n. They are two different functions. Say O(a) and O(b) --> O(a+b)
   
def print_items(a, b):
	for i in range(a):
		print(i)

	for j in range(b):
		print(j)
    
    
# Similary if you had nested for loops..
# Would become O(a*b)
  
 def print_items(a, b):
  for i in range(a):
      for j in range(b):
          print(i,j)
