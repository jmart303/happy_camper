
def solution(n):
	mu_list = []
	for x in str(n):
		mu_list.append(x)
	x = mu_list[0]
	y = mu_list[1]
	x = int(x)
	y = int(y)
	z = x + y
	print(z)
	return z

n = 29
solution(n)