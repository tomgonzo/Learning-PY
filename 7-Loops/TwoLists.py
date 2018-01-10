#Challenge 5 - Two-List Multiplication

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
products = []

for i in list1: #for each item in list1
	for j in list2: #run through items in list2
		products.append(i*j) #then add the products to products list

print(products) #print products list