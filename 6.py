orginalPrice = float(input("Enter the orginal cost of the item: "))
salePrice = float(input("Enter the sale price: "))
percentOff = int((orginalPrice - salePrice)/ orginalPrice * 100)
print("Orginal price: $", format(orginalPrice, ".2f"), sep= "")
print("Sale price: $", format(salePrice, ".2f"), sep= "")
print("Percent off: ", format(percentOff, "d"),"%",sep= "")
if(percentOff >= 50):
    print("You got a great sale!")
    print("Congratulations!")
print("Done!")


    



