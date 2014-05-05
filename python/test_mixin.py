class FBWTest(object):
    def _test(self, input, sequence, expected):
        result = FBWTest.fbw_func(input, sequence)
        self.assertEqual(result, expected)

    def test_case1(self):
        self._test(
                [3,5,7],
                [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Whizz', '8',
                    'Fizz', 'Buzz', '11', 'Fizz', 'Fizz', 'Whizz',
                    'FizzBuzz',
                    '16', '17', 'Fizz', '19', 'Buzz',
                    ]
                )

    def test_case2(self):
        self._test(
                [3,5,7],
                [90,91,92,93,94,95,96,97,98,99,100],
                ['FizzBuzz', 'Whizz', '92', 'Fizz', '94', 'Buzz',
                 'Fizz', '97', 'Whizz', 'Fizz', 'Buzz']
                )


    def test_case3(self):
        self._test(
                [2,6,9],
                [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
                ['1', 'Fizz', '3', 'Fizz', '5', 'FizzBuzz', '7', 'Fizz',
                 'Whizz', 'Fizz', '11', 'Fizz', '13', 'Fizz', '15',
                 'Fizz', '17', 'FizzBuzzWhizz', '19', 'Fizz']
                )

    def test_case4(self):
        self._test(
                [3,3,3],
                [1,2,3,4,5,6,7,8,9,10],
                ['1', '2', 'Fizz', '4', '5', 'FizzBuzzWhizz', '7',
                 '8', 'FizzBuzzWhizz', '10']
                )

