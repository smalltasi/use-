product = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = [name, price]
	product.append(p)
#  也可以寫成  product.append([name, price])
print(product)

for p in product:
	print(p)
	print(p[0], '的價格是', p[1])

with open('product.txt', 'w') as f:
	for pd in product:
		f.write(pd[0] + ' 的價格是 ' + str(pd[1]) + '\n') #pd[1]原是整數再轉為字串
