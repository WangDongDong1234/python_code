"""
思路是:
1).先求出数组的总和sum, sum/2=mid
2).然后将数组的元素跟mid比较，取出跟mid最接近的元素，放在第一个小数组里，然后在原来数组删除刚刚被取出的元素，更新原来数组
3).接着再取出离mid最近的元素，放在第二个小数组，在原数组中删除刚刚被取出的元素，更新原来数组
4).遍历原来数组，重复2和3，往后的元素放在第一个小数组或者第二个小数组，取决于两个小数组的所有元素的总和，哪个总和小就放在哪个小数组

"""