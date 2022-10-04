import io
import sys

#computing max reducing cost of multithreading
# 2 ways to compute max actually in key value database / ML
# * using the multihreading way (brute force)
# * find a way to store diffrently the number
# input :
#     * a filename to a file with the list of couple of letter(key) and an integer (value) as (a,3) separate by ';' # output : 
# ouput :
#     the key of the key of the max value
# the resolution must be done in less time than the naive implemented here on big files tests
#____________

# the naive algorithm implemeted 
# run is the function called by the test runner


def max_in_list(s): 
    pairs=s.replace("(",'').replace(")","").split(';')
    m = -1
    key= "NONE"
    d={}
    for pair in pairs:
        kv=pair.split(',')
        i=int(kv[1])
        d[kv[0]]=i
        if(m < i):
            m=i
            key=kv[0]
    print(key)
    return key

def run(s):
    return max_in_list(s)





