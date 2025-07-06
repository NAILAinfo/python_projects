rates = {
    'USD': {'EUR': 0.85, 'CAD': 1.25, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'CAD': 1.47, 'GBP': 0.88},
    'CAD': {'USD': 0.80, 'EUR': 0.68, 'GBP': 0.59},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'CAD': 1.70}
}

def conventer(a,b ,c):
    if a == b :
        return c
    else:
        return c * rates[a][b]

history = []

val = int(input('Enter the amount :'))
src = input('Source currency (USD/EUR/CAD) :')


if src not in rates:
    print("Invalid source currency.")
else :
    for trg in rates[src].keys():
        result = conventer(src,trg, val)
        if result is not None:
            f = f"{val} {src} is equal to {result:.2f} {trg}"
            print(f)
            history.append(f)

    print("\n--- Conversion History ---")
    for x in history:
        print(x)
        

