#load data from .txt file
data = open('data1.txt','r').read()
words = data.split('\n')

numbers = [str(x) for x in range(10)]

results = []
results_sum = 0

for word in words:
    if (len(word)==0):
        break
    temp_res = [None, None]
    left_ready, right_ready = False, False
    lp, rp = 0, 0

    for i, letter in enumerate(word):
        lp = i
        rp = -i-1
        if ((word[lp] in numbers) and (not left_ready)):
            temp_res[0] = word[lp]
            left_ready = True
        if ((word[rp] in numbers) and (not right_ready)):
            temp_res[1] = word[rp]
            right_ready = True
    results.append(f'{temp_res[0]}{temp_res[1]}')

for number in results:
    results_sum += int(number)

print('Results sum: ', results_sum)

#Great answer: 55447