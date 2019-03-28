products = []
while True:
	name = input('請輸入商名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	#products.append(p)
	products.append([name, price])
print(products)
for product in products:
	print(product[0], '的價格是', product[1])
	#print(product)
	#print(product[0])
#print(products[0][0])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
