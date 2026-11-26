days = int(input("Enter number of days: "))

total_prepared = 0
total_served = 0
total_waste = 0

for i in range(days):
    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    if prepared < 0 or served < 0 or served > prepared:
        print("Invalid quantities")
        break

    waste = prepared - served

    if prepared == 0:
        percentage = 0
    else:
        percentage = (waste / prepared) * 100

    print("Food Waste:", waste)
    print("Waste Percentage:", percentage, "%")

    if percentage > 10:
        print("High Food Wastage")
    else:
        print("Wastage Within Limit")

    total_prepared += prepared
    total_served += served
    total_waste += waste

else:
    print("\n----- FINAL REPORT -----")
    print("Total Prepared:", total_prepared)
    print("Total Served:", total_served)
    print("Total Waste:", total_waste)