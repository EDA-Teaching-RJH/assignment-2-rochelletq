### Part Three -- your code goes here. 
def remove_items(test_list, item):
 
      res = [i for i in test_list if i != item]
      return res

if __name__ == "__main__":
    my_list = [3,1,4,1,5,9,2,6,5,3]
    item = 1

my_list = remove_items(my_list, item)
my_list.sort()
points = (7,8)
my_list.extend(points)
print(my_list)


