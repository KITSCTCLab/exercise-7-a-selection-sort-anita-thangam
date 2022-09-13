from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(1,len(array)):
    t= array[i]
    j=i+1
    while j<=0 and t>array[j]:
      array[j-1]=array[j]
      j+=1
     array[j-1] = t
   return array
    
    
  

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
