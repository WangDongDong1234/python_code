n=int(input())
array_str=input().strip()
array=[int(item) for item in array_str.split()]
array.sort()
print(array)
min_cha=1
if n%2!=0:
    mid=n//2
    i=mid-1
    j=mid+1
    while array[i]==array[mid]:
        min_cha+=1
        i-=1
    while array[j]==array[mid]:
        min_cha+=1
        j+=1
else:
    mid_left=n//2-1
    mid_right=n//2
    i=mid_left-1
    left_same=1
    while array[i]==array[mid_left]:
        left_same+=1
        i-=1
    j=mid_right+1
    right_same=1
    while array[j]==array[mid_right]:
        right_same+=1
        j+=1
    min_cha=left_same*right_same
max_cha=0
start=0
end=len(array)-1
i=start+1
left_start=1
while array[i]==array[start]:
    left_start+=1
    i+=1
j=end-1
right_end=1
while array[j]==array[end]:
    right_end+=1
    j-=1
max_cha=left_start*right_end
print(min_cha,max_cha)




