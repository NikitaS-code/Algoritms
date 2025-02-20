n = int(input())
durability = list(map(int, input().split())) 
k = int(input())  
press_sequence = list(map(int, input().split()))  


press_count = [0] * n


for press in press_sequence:
    press_count[press - 1] += 1  

for i in range(n):
    if press_count[i] > durability[i]:
        print("YES")  
    else:
        print("NO")   