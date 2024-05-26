def f(x):
  if x < 0:
    return "عدد سالب"
  elif x == 0:
    return 1
  else:
    r = 1
    for i in range(1, x + 1):
      r *= i
    return r
while True:
  num = int(input("أدخل عدد "))
  r = f(num)
  print(r)
  if r == "عدد سالب":
    break

