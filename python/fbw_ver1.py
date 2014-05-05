class FBW(object):
    def __init__(self, num):
        self.num = num

    def say(self):
        raise NotImplementedError()

    def __eq__(self, Obj):
        if not isinstance(Obj, FBW):
            return False
        return self.num == Obj.num

    def __str__(self):
        return '%d' % self.num


class Other(FBW):
    def say(self):
        return str(self.num)

class Fizz(FBW):
    def say(self):
        return 'Fizz'

class Buzz(FBW):
    def say(self):
        return 'Buzz'

class Whizz(FBW):
    def say(self):
        return 'Whizz'


class ResultList(object):
    def __init__(self):
        self.res = []

    def add(self, obj):
        if not self.res:
            self.res.append([obj, obj.say()])
            return

        last_obj, last_say = self.res[-1]
        if obj == last_obj:
            last_say = '%s%s' % (last_say, obj.say())
            
            self.res[-1][1] = last_say
            return

        self.res.append([obj, obj.say()])

    def __iter__(self):
        for i in self.res:
            yield i[1]



def type_finder(input, sequence):
    assert len(input) == 3
    for i in input:
        assert isinstance(i, int) and i > 0 and i < 10
    a, b, c = input

    for num in sequence:
        str_num = str(num)
        multiple = False

        if str(a) in [str_num[i] for i in range(len(str_num))]:
            # rule 5
            yield Fizz(num)
            continue

        if num % a == 0:
            multiple = True
            yield Fizz(num)

        if num % b == 0:
            multiple = True
            yield Buzz(num)

        if num % c == 0:
            multiple = True
            yield Whizz(num)

        if not multiple:
            yield Other(num)


def run(input, sequence):
    rl = ResultList()
    for tp in type_finder(input, sequence):
        rl.add(tp)

    return list(rl)


if __name__ == '__main__':
    input = raw_input()
    input = input.split(',')
    input = [int(i) for i in input]
    for i in run(input, range(1, 101)):
        print i

