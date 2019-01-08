matrix=[]
i=0
j=0
max=0
while i<len(matrix[0]):
    #每行j都要重置
    j=0
    while j<len(matrix[0]):
        if matrix[i][j]==0:
            break;
        else:
            #向右向下扩展
            width=1
            height=1
            #向右扩展
            tmp_j=j+1
            while tmp_j<len(matrix[0]):
                if matrix[i][j]==1:
                    width+=1
                else:
                    break
                tmp_j+=1
            #向下扩展
            tmp_i=i+1
            while tmp_i<len(matrix):
                tmp_matrix=matrix[tmp_i][j:j+]