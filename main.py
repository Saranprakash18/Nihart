s = "a)b(c)d"


result = ""
open_count = 0

for ch in s:
    if ch == '(':
        open_count += 1
        result += ch
    elif ch == ')':
        if open_count > 0:   
            open_count -= 1
            result += ch
    else:
        result += ch


final = ""
for ch in reversed(result):
    if ch == '(' and open_count > 0:
        open_count -= 1
        continue
    final += ch

final = final[::-1]

print(final)
