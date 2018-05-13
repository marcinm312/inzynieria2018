def dodaj(a,b):
	return a + b

def get_help():
	print("To jest prosty kalkulator")
	print("Podaj dwie liczby, a ja je dodam")

get_help()
x = int(input())
y = int(input())
print(dodaj(x,y))