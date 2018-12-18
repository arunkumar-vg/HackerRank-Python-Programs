def capitalize(s):
    a_string=s.split(" ")
    return(' '.join((word.capitalize() for word in a_string))) 

def solve(s):
    return(capitalize(s))