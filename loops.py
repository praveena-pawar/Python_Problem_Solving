# Q1. Loop Predict the Output 
x = 0

for i in range(3):
    x = x + i

print(x)
 
# and the output x = 3





# Q2. Predict the output
x = 10

for i in range(1, 4):   # i = 1, 2, 3
    if i % 2 == 0:
        x = x - i
    else:
        x = x + i

print(x)

# and the output x = 12







# Q3. Predict the output
y = 5

for i in range(2, 7):   # i = 2, 3, 4, 5, 6
    if y % 2 == 0:
        y = y + i
    else:
        y = y - i

print(y)

# and the output y = 3







# Q4. Predict the output
x = 1

for i in range(1, 6):     # i = 1,2,3,4,5
    if i % 2 == 0:
        x = x * i
    else:
        x = x + i

print(x)

# and the output x = 33







# Q5 — Predict the Output (Loop + Conditions + Updates)
x = 10
y = 2

for i in range(1, 5):    # i = 1,2,3,4
    if x % i == 0:
        x = x // i
    else:
        y = y + i

print(x, y)

# and the output x = 5 and y = 9





# Q6 — Predict the Output (Loop + Conditions + Updates)
x = 7
for i in range(1, 6):
    if x % i == 0:
        x += i
    else:
        x -= 1
    if x < 5:
        break
print(x)

# and the output 7




# Q7 — Predict the Output (Loop + Conditions + Updates)
a = 3
b = 1
for i in range(5):
    if (a + b) % 2 == 0:
        a -= i
        b += 2
    else:
        a += 3
        b -= 1
print(a, b)

# and the output 11 2




# Q7 — Predict the Output (Loop + Conditions + Updates)
total = 0
for i in range(1, 8):
    if i % 2 == 0:
        total += i // 2
    else:
        total = total * 2 + 1
    if total > 15:
        total -= 5
print(total)

# and the output 22




# Q8 — Predict the Output (Loop + Conditions + Updates)
n = 5
result = 1
for i in range(1, n+1):
    if result % 2 == 0:
        result += i
    else:
        result *= i
    if result > 20:
        result //= 2
print(result)

# and the output 12




# Q9 — Predict the Output (Loop + Conditions + Updates)
value = 8
for i in range(2, 6):
    if value % i == 0:
        value = value // 2
    else:
        value += i
    if value < 3:
        value += i * 2
print(value)

# and the output 16




# Q10 — Most Difficult
a, b = 2, 9
for i in range(1, 6):
    if a * b % i == 0:
        a += i
        b -= 1
    else:
        a -= 1
        b += i
    if a > b:
        break
print(a, b)

# and the output 7 14



