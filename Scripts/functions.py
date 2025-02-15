def customer_record(fh, n):
    """
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
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