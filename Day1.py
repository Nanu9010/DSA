# n = int(input("Enter Your Amount : "))

# Total = 0

# for i in range (n,n+1):
#     Total += i

# print(Total) 


# n = 11

# total = (n * (n+1) // 2)
# print(total)


# n = int(input("enter number : "))

# total = 0

# for i in range(n):
#     num = int(input(""))
#     total += num

# print(total / n)

# n = int(input("enter num : "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# print(reverse)

# n = abs(int(input(" Enter your ABS :")))

# count = 0 

# if n == 0:
#     count ==1 

# while n>0:
#     count+=1
#     n//=10
# print(count)

# a = int(input("enter num :"))

# z = input("enter ABCD : ")

# if z in "aeiouAEIOU" :
#     print(" this is Vowel")
# else:
#     print(z, "yes this is vowel")

# n = int(input(" eneter num: "))


# n=11

# for i in range(n, (n*10)+1, n):
#     print(i)

# n = 4

# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")


# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact = fact * i
    
# print(fact)

# n = 12

# for i in range(1, n+1):
#     if n%i == 0:
#         print
#     else:
#         print(i, end=" ")


# n = int(input("enter : "))
# sum = 0 
# for i in range(1, n):
#     if n%i == 0:
#         sum = sum +1
        
# if sum == n:
#     print("this is sum", sum)
# else:
#     print("not sum")
# n = 10
# count = 0
# for i in range(1, n):
#     if n%i == 0:
#         count = count + 1
#         print(i)
# if count==2:
#     print("prime num")
# else:
#     print("compunding num")


# n = int(input("enter num :"))

# while n>0:
     
#     sum = n//2
#     print(sum)


# def evenodd(a):
#     if a%2 == 0:
#         return("even")
#     else:
#         return("odd")


# evenodd(44)

# abc = ("hello world")
# for i in range(0, len(abc)):
#     print(abc[i], end=" ")
     

# def everyday():
#     for i in abc:
#         print(i, end = " ")

 
# a= [1,2,4,6,8]

# a.remove(2)
 
# print(a)


# a = ("KartikRaj Nalage")
# b= len(a)-1
# print(a[::-1])

# for i in range(len(a)-1,-1,-1):
#     print(a[i], end="")


name = "KartikRaj Nalage"

append = " "
for i in name:
    if i.islower():
        append = append + i

print(append)
