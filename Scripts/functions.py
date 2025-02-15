def customer_record(fh, n):
    """
    
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    
    """
    result = []
    line = fh.readline()
    count = 0 
    while line != "" and count != n:
        count += 1
        line = fh.readline()
    if line != "":
        result = line.strip().split(",")
    return result 

def customer_best(fh):
    """

    Find the customer with the largest balance.
    Assumes file is not empty.
    
    """
    result = []
    value = 0 
    for line in fh:
        info = line.strip().split(",")
        value2 = float(info[3])
        if value2 > value: 
            value = value2 
            result = line.strip().split(",")
    return result

def append_max_num(fh):
    """

    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    
    """
    num = 0 
    line = fh.readline()
    while line != "":
        value = int(line)
        if value > num:
            num = value
        line = fh.readline()
    fh.write(f"\n{num}")
    return num 