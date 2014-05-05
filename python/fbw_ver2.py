WORDS = ['Fizz', 'Buzz', 'Whizz']

def say(input, num):
    str_num = str(num)
    if str(input[0]) in [str_num[i] for i in range(len(str_num))]:
        return WORDS[0]

    res = reduce(lambda acc, index: acc if num%input[index] else '%s%s'%(acc, WORDS[index]), range(len(input)), '')
    return res if res else str(num)

def run(input, sequence):
    assert len(input) == 3
    for i in input:
        assert isinstance(i, int) and i > 0 and i < 10
    return [say(input, num) for num in sequence]

if __name__ == '__main__':
    input = raw_input()
    input = input.split(',')
    input = [int(i) for i in input]
    for i in run(input, range(1, 101)):
        print i
