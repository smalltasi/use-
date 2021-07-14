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

with open('product.csv', 'w', encoding='utf-8') as f:   #csv要加編碼 通用utf-8
	f.write('商品,價格\n')
	for pd in product:
		f.write(pd[0] + ',' + str(pd[1]) + '\n') #pd[1]原是整數再轉為字串