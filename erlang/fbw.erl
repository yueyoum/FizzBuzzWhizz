-module(fbw).
-export([start/1,
         start/3]).

-export([init/3,
        rule5/3,
        handler/3,
        to_integer_list/1]).

-include_lib("eunit/include/eunit.hrl").

-vsn(2.3).


start(Input) ->
    start(Input, 1, 100).

start(Input, StartNum, EndNum) ->
    Sequence = lists:seq(StartNum, EndNum),
    spawn(?MODULE, init, [Input, Sequence, self()]).


init([A, B, C], Sequence, StartPid) ->
    register(main, self()),

    WhizzPid = spawn_link(?MODULE, handler, [C, "Whizz", null]),
    BuzzPid = spawn_link(?MODULE, handler, [B, "Buzz", WhizzPid]),
    FizzPid = spawn_link(?MODULE, handler, [A, "Fizz", BuzzPid]),

    Rule5Pid = spawn_link(?MODULE, rule5, [A, "Fizz", FizzPid]),

    Result = loop(Rule5Pid, Sequence, []),
    output(Result),

    StartPid ! {result, Result},

    lists:foreach(fun(P) -> exit(P, finish) end, [Rule5Pid, FizzPid, BuzzPid, WhizzPid]).


loop(_, [], Result) ->
    lists:reverse(Result);

loop(Rule5Pid, [Head | Tail], Result) ->
    Rule5Pid ! {do, Head},
    receive
        {ok, Res} ->
            loop(Rule5Pid, Tail, [Res | Result])
    end.

output([]) ->
    ok;

output([Head | Tail]) ->
    io:format("~p~n", [Head]),
    output(Tail).


to_integer_list(Num) ->
    do_to_integer_list(Num, []).

do_to_integer_list(0, Res) ->
    Res;

do_to_integer_list(Num, Res) ->
    do_to_integer_list(Num div 10, [Num rem 10 | Res]).


rule5(X, Word, Next) ->
    receive
        {do, Num} ->
            case lists:any(fun(N) -> N =:= X end, to_integer_list(Num)) of
                true ->
                    main ! {ok, Word};
                false ->
                    Next ! {do, Num, ""}
            end
    end,
    rule5(X, Word, Next).


handler(X, Word, Next) ->
    receive
        {do, Num, LastWord} ->
            ActualWord =
            case Num rem X of
                0 ->
                    Word;
                _ ->
                    ""
            end,
            case Next of
                null ->
                    FinalWord =
                    case LastWord ++ ActualWord of
                        [] ->
                            integer_to_list(Num);
                        W ->
                            W
                    end,
                    main ! {ok, FinalWord};
                Next ->
                    Next ! {do, Num, LastWord ++ ActualWord}
            end
    end,
    handler(X, Word, Next).





%% test
%%


t_common(Input, StartNum, EndNum, Expected) ->
    ?MODULE:start(Input, StartNum, EndNum),
    Result =
    receive
        {result, R} ->
            R
    end,
    ?assert(Result =:= Expected).


case1_test() ->
    t_common(
     [3,5,7],
     1,
     20,
     ["1","2","Fizz","4", "Buzz", "Fizz", "Whizz",
     "8", "Fizz", "Buzz", "11", "Fizz", "Fizz",
     "Whizz", "FizzBuzz", "16", "17",
     "Fizz", "19", "Buzz"]
     ).

case2_test() ->
    t_common(
     [3,5,7],
     90,
     100,
     ["FizzBuzz", "Whizz", "92", "Fizz", "94", "Buzz",
     "Fizz", "97", "Whizz", "Fizz", "Buzz"]
     ).


case3_test() ->
    t_common(
     [2,6,9],
     1,
     20,
     ["1", "Fizz", "3", "Fizz", "5", "FizzBuzz", "7",
     "Fizz", "Whizz", "Fizz", "11", "Fizz", "13", "Fizz",
     "15", "Fizz", "17", "FizzBuzzWhizz", "19", "Fizz"]
     ).


case4_test() ->
    t_common(
     [3,3,3],
     1,
     10,
     ["1", "2", "Fizz", "4", "5", "FizzBuzzWhizz", "7",
     "8", "FizzBuzzWhizz", "10"]
     ).


