sp=int(input("Enter selling price of the item?"))
cp=int(input("Enter cost price of the item?"))
ans='profit' if sp-cp>0 else 'loss'
print(ans)
