import sys
def calculate_add(a,b):
    return a+b

if __name__=="__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print ("Addition is : ",calculate_add(a,b))