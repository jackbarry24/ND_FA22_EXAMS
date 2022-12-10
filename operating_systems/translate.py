import math

KB = 2**10
MB = 2**20
GB = 2**30
TB = 2**40

def translate(bytes):
    if bytes < KB:
        return str(bytes) + " B"
    elif bytes < MB:
        return str(bytes/KB) + " KB"
    elif bytes < GB:
        return str(bytes/MB) + " MB"
    elif bytes < TB:
        return str(bytes/GB) + " GB"
    else:
        return str(bytes/TB) + " TB"

def express(bytes, option):
    if option == 'B':
        return bytes
    elif option == 'KB':
        return bytes/KB
    elif option == 'MB':
        return bytes/MB
    elif option == 'GB':
        return bytes/GB
    elif option == 'TB':
        return bytes/TB

def power2(bytes):
    exp = int(math.log(bytes, 2))
    return "2^" + str(exp)
    
