def computepay(hrs,rph):
    h = float(hrs)
    r = float(rph)
    if h <= 40:
        return h * r
    else:
        overtime = h - 40
        return 40 * r + 1.5 * r * overtime

hrs = input("Enter Hours:")
rate_per_hour = input("Rate per Hour:")
p = computepay(hrs,rate_per_hour)
print(p)
