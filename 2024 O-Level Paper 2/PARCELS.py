flag = True
while flag:
    length = float(input("What is the length of the parcel? "))
    width = float(input("What is the width of the parcel? "))
    depth = float(input("What is the depth of the parcel? "))
    if length > 50 and length > 50 and depth > 50:
        parcel_size = "large"
    elif length > 50 and width > 50 and depth <= 50:
        parcel_size = "medium"
    elif length <= 50 or width <= 50:
        parcel_size = "small"
    more_parcels = input("Do you want to enter another parcel? Y or N ")
    if more_parcels == "N":
        flag = False
print("The size of your parcel is", parcel_size)