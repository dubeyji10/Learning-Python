# 06 , 32

print(" list 1")
shopping_list = ["milk","eggs","butter","spam","bread","rice","pasta"]
for i in shopping_list:
      print("buy "+i)


print("\n\n list 2 ")
for item in shopping_list:
    if item == 'spam':
        print("item ignored is "+item)
        continue

    print("buy "+item)

#        in list 2 spam was skipped


# example of break
print("\n\n list 3")

for item in shopping_list:
    if item == 'spam':
         break

    print("buy "+item)
# here loop will stop at spam

