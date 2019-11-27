hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hour = input("Rate per Hour:")
rph = float(rate_per_hour)

if h <= 40:
    print(h * rph)
else:
    overtime = h - 40
    print(40 * rph + 1.5 * rph * overtime)
