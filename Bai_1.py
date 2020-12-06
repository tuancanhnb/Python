# 38.Cho một list các số nguyên n phần tử lst được nhập vào từ bàn phím, bạn hãy viết chương trình tính tổng các phần tử trong list vừa nhập

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

tong = 0
for i in lst:
    tong += i
print(tong)

# 39.Cho một list các số nguyên n phần tử lst được nhập vào từ bàn phím, bạn hãy viết chương trình sắp xếp các phần tử trong list theo thứ tự tăng dần và hiển thị list đó ra màn hình

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort()
print(lst)


n = int(input())           # làm kiểu for
lst = []
for i in range(n):
    lst.append(int(input()))

for i in range(len(lst)):
    for j in range(i):
        if lst[i] < lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

print(lst)

# 40. Cho một list các số nguyên n phần tử lst được nhập vào từ bàn phím, bạn hãy viết chương trình hiển thị ra màn hình các số số lẻ trong list vừa nhập.

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

answer = []
for a in lst:
    if a % 2 != 0:
        answer.append(a)

print(answer)

# 41. Cho một list các số nguyên n phần tử lst được nhập vào từ bàn phím, bạn hãy viết chương trình hiển thị ra màn hình các số chia hết cho 5 trong list vừa nhập, nếu list không có số nào chia hết cho 5 thì hiển thị ra màn hình [0]

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

answer = []
for a in lst:
    if a % 5 == 0:
        answer.append(a)
if len(answer) == 0:
    answer =[0]

print(answer)

# 42. Cho chuỗi s được nhập từ bàn phím, bạn hãy viết chương trình chuyển các kí tự trong chuỗi s thành in hoa và hiển thị ra màn hình

s = input()
print(s.upper())

# 43. Cho chuỗi s được nhập vào từ bàn phím, bạn hãy viết chương trình nối 2 kí tự đầu và 2 kí tự cuối của chuỗi s và hiển thị ra màn hình. Nếu chuỗi s có độ dài nhỏ hơn 2 thì hiển thị ra chuỗi rỗng

s = input()
if len(s) < 2:
    print("")
else:
    print(s[0:2] + s[-2:])

# 44. Cho trước hai chuỗi s1 và s2 được nhập từ bàn phím, bạn hãy viết chương trình đổi chỗ 2 ký tự đầu tiên của s1 và s2 cho nhau. Sau đó hiển thị ra màn hình chuỗi mới có giá trị s1 + " " + s2

s1 = input()
s2 = input()
print(s2[0:2] + s1[2:] + " " +s1[0:2] +s2[2:])

# 45. Cho trước chuỗi s được nhập từ bàn phím, bạn hãy viết chương trình để đảo ngược thứ tự xuất hiện của các từ trong chuỗi s và sau đó hiển thị ra màn hình chuỗi đã được xử lý

s = input()
a = s.split(" ")
print(" ".join(reversed(a)))

# 46. Bạn hãy viết hàm trả về tổng của các phần tử trong list các số nguyên được nhập vào từ bàn phím

n = int(input("nhập vào số phần tử: "))
lst = []
for i in range(n):
    lst.append(int(input()))

def sum(lst):
    answer = 0
    for i in lst:
        answer += i
    return answer

print(sum(lst))

# 47. Cho 3 số nguyên a, b, c được nhập vào từ bàn phím, bạn hãy viết hàm trả về số lớn nhất trong 3 số này và hiển thị kết quả ra màn hình

a = int(input("nhập vào số a: "))
b = int(input("nhập vào số b: "))
c = int(input("nhập vào số c: "))

def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
print(maximum(a, b, c))


# 48. Cho chuỗi s được nhập vào từ bàn phím, bạn hãy viết chương trình Python để đếm số các chữ cái in hoa và in thường trong chuỗi và in kết quả ra màn hình theo từng dòng

s = str(input("chuỗi đã cho: "))
b = str(input())
def chuoi(a):
    count_upper = 0
    count_lower = 0
    for i in a:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    print("Given string:", s)
    print("Number of uppercase letters:", count_upper)
    print("Number of lowercase letters:", count_lower)
chuoi(s)

# 49. Bạn hãy viết hàm nhận vào một list và trả về các số xuất hiện trong list đó

n = int(input("nhập vào số phần tử: "))
lst = []
for i in range(n):
    lst.append(int(input("nhập vào phần tử trong dãy: ")))

def chuoi(lst):
    answer = []
    for v in lst:
        if v not in answer:
            answer.append(v)
    return answer
print(chuoi(lst))

# 50. Cho số tự nhiên n được nhập vào từ bàn phím, bạn hãy viết hàm kiểm tra xem n có phải là số nguyên tố không, nếu có trả về True, ngược lại trả về False

n = int(input("nhập số: "))

def ktra(x):
    count = 0
    for a in range(1, n + 1):
        if n % a == 0:
            count += 1
    if count == 2:
        return True
    return False
print(ktra(n))

# bài tập cuối chương CodeLearn:

# 51. Cho trước list res là list chứa các phần tử integer được nhập từ bàn phím. Viết chương trình Python để tìm ra các phần tử chẵn trong list đó. Kế tiếp, in kết quả là một list các số chẵn ra màn hình

n = int(input("nhập vào số phần tử: "))
res = []
for i in range(n):
    res.append(int(input("nhập vào phần tử: ")))

def even_number(res):
    answer = []
    for a in res:
        if a % 2 == 0:
             answer.append(a)
    return answer
print(even_number(res))

# 52. Viết chương trình Python để tính a mũ b với a, b là hai số tự nhiên được nhập từ bàn phím. Sau đó, in kết quả ra màn hình

a = int(input("nhập vào a: "))
b = int(input("nhập vào b: "))

def index_number(a, b):
    mu = 1
    for i in range(b):
        mu *= a
    return mu

print(index_number(a, b))

# 53. Viết chương trình Python để tìm ước chung lớn nhất của hai số a, b với a, b là hai số tự nhiên được nhập từ bàn phím. Sau đó, in kết quả ra màn hình

a = int(input("nhập vào a: "))
b = int(input("nhập vào b: "))

def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(gcd(a, b))

# 54. Cho 3 số nguyên a, b và c là 3 cạnh của một tam giác. Viết chương trình để kiểm tra xem tam giác đó là tam giác đều, tam giác cân hay tam giác thường và in ra màn hình kết quả  "Equilateral triangle", "Isosceles triangle" hoặc "Scalene triangle" tương ứng

a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("Equilateral triangle")
elif a == c or a == b or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# 55. Cho trước chuỗi str được nhập từ bàn phím. Viết chương trình Python để tìm ra từ có độ dài lớn hơn 3. Sau đó, in kết quả là mội list các chuỗi thoả mãn điều kiện đó ra màn hình

str = str(input("nhập vào chuỗi: "))
lst = []
a = str.split(" ")

def ktra(a):
    for i in a:
        if len(i) > 3:
            lst.append(i)
    return lst

print(ktra(a))

# 56. Cho trước danh sách res gồm nhiều số nguyên được nhập từ bàn phím. Viết chương trình Python để chuyển đổi các phần tử trong list thành một số tự nhiên. Tiếp đến, in ra màn hình kết quả

n = int(input("nhập vào số phần tử: "))
res = []

for i in range(n):
    res.append(str(input("nhập vào các phần tử: ")))

print("".join(res))

# 57... cắt chuỗi các thứ

s = str(input("nhập vào chuỗi: "))

def format(s):
    if len(s) >= 3:
        if s[-3:] != "ing":
            print(s + "ing")
        elif s[-3:] == "ing":
            print(s + "ly")
    else:
        print(s)
format(s)

# 58. Cho số là số nguyên dương n được nhập từ bàn phím. Viết chương trình Python để tính tổng tất cả các ước số nguyên dương khác n của n. Sau đó, in kết quả ra màn hình

n = int(input("nhập vào số: "))

def sumOfAll(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
print(sumOfAll(n))

# 59. Cho trước nlà số nguyên được nhập từ bàn phím. Viết chương trình Python để kiểm tra số đó có phải là số abundant hay là không. Sau đó, in kết quả True hoặc False ra màn hình

n = int(input("nhập vào số: "))

def is_abundant(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    
    if tong > n:
        return True
    elif tong < n:
        return False

print(is_abundant(n))