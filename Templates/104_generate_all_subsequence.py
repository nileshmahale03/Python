#genaret all subsequence 
#formula -> (2 ** N)
#Continuous -> No
def generate_subsequence(idx, path):
    if idx == len(A):
        print(path)
        return
    
    #Not Take
    generate_subsequence(idx + 1, path) 

    #Take
    path.append(A[idx])
    generate_subsequence(idx + 1, path)
    path.pop()

A = [1, 6, 3, 7]
generate_subsequence(0, [])