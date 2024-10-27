import random 

rand_list = []
n=10
for i in range(n):
    rand_list.append(random.randint(1,100))

def remove_even(rand_list):
    for i in rand_list[:]:
        if (i % 2) == 0:
            rand_list.remove(i)

    return rand_list

rand_list = remove_even(rand_list)
print(rand_list)
        
