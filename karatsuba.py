def karatsuba(x: int, y: int):
    # Break the recursion written below if the numbers have less than 2 digits.
    if x < 10 or y < 10:
        return x * y
    
    # Get the maximum length of (x, y) and get it divided by half
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # a,b,c,d are a result of x and y digits separated in half (i.e x = 1234 results in a = 12, x = 34)
    a = x // 10 ** half
    b = x % 10 ** half
    c = y // 10 ** half
    d = y % 10 ** half

    # Karatsuba formula is 10^n * ac + 10^(n/2) * (ad+bc) + bd
    # ac, bd and ad_plus_b are calculated recursively.
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a+b, c+d) - ac - bd

    # Using half * 2 resolves the algorithm's issue with odd number of inputs 
    return (10 ** (half * 2)) * ac + (10 ** half) * ad_plus_bc + bd
