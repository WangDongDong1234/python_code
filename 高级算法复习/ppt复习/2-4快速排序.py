"""
快速排序:思想是确定一个基准数  找到基准数的正确位置确保基准数的左边小于等于基准数，基准数的右边大于等于基准数然后快排左边和右边
"""
def quickSort(array,left,right):
   if left>right:
       return
   base=array[left]
   i=left
   j=right
   while i<j:
       while array[j]>=base and j>i:#确保j>i
           j-=1
       while array[i]<=base and j>i:#确保j>i
           i+=1
       if i<j:#确保j>i
           array[i],array[j]=array[j],array[i]
   #i=j的情况
   array[left]=array[i]
   array[i]=base
   quickSort(array,left,i-1)
   quickSort(array,j+1,right)

array=[2,4,6,8,5,7,9,1,3,3,5,4,7,8]
quickSort(array,0,len(array)-1)
print(array)