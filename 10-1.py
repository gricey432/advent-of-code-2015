def look_and_say(s):
    result = ''
    digit = s[0]
    count = 0
    for c in s:
        if c == digit:
            count += 1
        else:
            result += str(count) + digit
            digit = c
            count = 1
    result += str(count) + digit
    return result

result = '3113322113'  # input from adventofcode
for i in range(40):  # 40 is magic number from adventofcode
    result = look_and_say(result)

print len(result)
