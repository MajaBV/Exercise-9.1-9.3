print("Hello there. This is kilometers to miles converter. Please enter below the number of kilometers that you'd like to convert into miles.")

while True:
    km = (input("Km: "))
    km = float(km.replace(",", "."))
    miles = km * 0.621371192

    print("{} km = {} miles".format(km, miles))

    search = input("Do you want another conversion (y/n): ")
    if search.lower() != "yes" and search.lower() != "y":
        break