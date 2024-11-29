#load data from .txt file
data = open('data2.txt','r').read()
words = data.split('\n')

numbers = [str(x) for x in range(10)]
numbers_text = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numb_convert={
    'one':'1', 
    'two':'2', 
    'three':'3', 
    'four':'4', 
    'five':'5', 
    'six':'6', 
    'seven':'7', 
    'eight':'8', 
    'nine':'9',
}

results = []
results_sum = 0

def decode_word(word):
    min_idx = len(word)
    max_idx = -1
    min_word = ''
    max_word = ''

    for nb in numbers_text:
        
        idx = word.find(nb)
        # print(nb, word,idx,min_word,max_word)
        if (idx < min_idx) and (idx != -1):
            min_word = nb
            min_idx = idx
        elif (idx > max_idx) and (idx != -1):
            max_word = nb
            max_idx = idx
    if len(min_word)>2:
        word = word.replace(min_word, numb_convert[min_word],1)
    if len(max_word)>2:
        word = word.replace(max_word, numb_convert[max_word],1)

    return word

for word in words:
    if (len(word)==0):
        break
    temp_res = [0, 0]
    left_ready, right_ready = False, False
    lp, rp = 0, 0

    new_word = decode_word(word)
    for i in range(len(new_word)):
        lp = i
        rp = -i-1

        if ((new_word[lp] in numbers) and (not left_ready)):
            temp_res[0] = new_word[lp]
            left_ready = True

        if ((new_word[rp] in numbers) and (not right_ready)):
            temp_res[1] = new_word[rp]
            right_ready = True

    print(f'{temp_res[0]}{temp_res[1]}')
    results.append(f'{temp_res[0]}{temp_res[1]}')

for number in results:
    results_sum += int(number)

print('Results sum: ', results_sum)

#55103 - too high