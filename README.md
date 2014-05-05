# FizzBuzzWhizz

你是一名体育老师，在某次课距离下课还有五分钟时，你决定搞一个游戏。此时有100名学生在上课。游戏的规则是：


1.  你首先说出三个不同的特殊数，要求必须是个位数，比如3、5、7。
2.  让所有学生拍成一队，然后按顺序报数。
3.  学生报数时，如果所报数字是第一个特殊数（3）的倍数，那么不能说该数字，而要说Fizz；如果所报数字是第二个特殊数（5）的倍数，那么要说Buzz；如果所报数字是第三个特殊数（7）的倍数，那么要说Whizz。
4.  学生报数时，如果所报数字同时是两个特殊数的倍数情况下，也要特殊处理，比如第一个特殊数和第二个特殊数的倍数，那么不能说该数字，而是要说FizzBuzz, 以此类推。如果同时是三个特殊数的倍数，那么要说FizzBuzzWhizz。
5. 学生报数时，如果所报数字包含了第一个特殊数，那么也不能说该数字，而是要说相应的单词，比如本例中第一个特殊数是3，那么要报13的同学应该说Fizz。如果数字中包含了第一个特殊数，那么忽略规则3和规则4，比如要报35的同学只报Fizz，不报BuzzWhizz。


现在，我们需要你完成一个程序来模拟这个游戏，它首先接受3个特殊数，然后输出100名学生应该报数的数或单词。比如，
 

    输入
    3,5,7
    输出（片段）

    1
    2
    Fizz
    4
    Buzz
    Fizz
    Whizz
    8
    Fizz
    Buzz
    11
    Fizz
    Fizz
    Whizz
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz 
    …
    一直到100



## Python 版本

#### python/fbw_ver1.py

企业级，高大上版本。其实我不会JAVA

#### python/fbw_ver2.py

这才是python该有的表达力


**run**

    cd python
    python file.py

    输入三个特殊数， 英文逗号分割，回车


**test**

对应各自的 `python/test_ver1.py`,  `python/test_ver2.py`

直接 python file.py 运行


## Erlang 版本

#### erlang/fbw.erl

**run & test**

    cd erlang
    erl     # 打开erlang shell
    > c(fbw).
    > fbw:start([3,5,7])           # 运行
    > fbw:start([4,6,7], 1, 200)   # 运行，并且以 4,6,7为特殊数，以此遍历1到200的数
    > fbw:test()                   # 测试



