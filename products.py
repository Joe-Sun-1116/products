import os

products = []

if os.path.isfile('products.csv'):
	print('檔案開啟成功')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)

else:
	print('找不到檔案')




#輸入資料
while True:
	name = input('Please enter name of products.')
	if name == 'q':
		break
	price = input('Please enter the price.')
	products.append([name, price])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')