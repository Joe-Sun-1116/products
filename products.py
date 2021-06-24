import os

def read_file(filename)
	products = []
	if os.path.isfile(filename):
		print('檔案開啟成功')
		with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
			print(products)
	else:
		print('找不到檔案')
	return products

# 輸入資料
def user_input(products):
	while True:
		name = input('Please enter name of products.')
		if name == 'q':
			break
		price = input('Please enter the price.')
		products.append([name, price])
	return products

def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

def write_file(filename, products)
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

products = read_file('products.csv')
products = user_input(products)
print_prosuct(products)
write_file('products.csv', products)
