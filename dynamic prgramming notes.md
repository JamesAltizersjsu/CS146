dynamic programming intuition
fibo(n)=nth fibonacci number
recursive find
fibo(1)=1,1
fibo(2)=1+1=2
fibo(3)=1+2=3
fibo(4)=2+3=5
make an array entry for each value, and the time and space  complexities are o(n)
as you are sliding on a linear array to look up and get values
it is a way of thinking or a paradigm
divide the problem into subproblems
overlapping subproblems is a property that dynamic programming can take advantage of repeat work
memoization is storing the previous results  to find new ones and it speeds up the programming in subsequent runs
knapsack problem for tabulation:
EX:
n=3 ,w=5 profits{2,4,6} weights ={5,6,2}
expected output=6
1. include in sack
2. don't include in the sack

   
