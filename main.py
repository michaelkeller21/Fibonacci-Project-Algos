import time
from fibonacci_recursion import fibonacci_recursion
from fibonacci_memoization import fibonacci_memoization
from fibonacci_fast_doubling import fibonacci_fast_doubling

def main():
    print("Fibonacci Algorihm Comparison")
    print("n\tRecursion\tMemoization")
    for i in range (1, 41):
        recur_sum=0
        memo_sum=0
        for j in range(1, 6):
            recur_start=time.perf_counter()
            fibonacci_recursion(i)
            recur_end=time.perf_counter()
            recur_run=(recur_end-recur_start)*1000            
            recur_sum+=recur_run 
            memo_start=time.perf_counter()
            fibonacci_memoization(i)
            memo_end=time.perf_counter()
            memo_run=(memo_end-memo_start)*1000            
            memo_sum+=memo_run
        recur_average=recur_sum/5
        memo_average=memo_sum/5
        print(str(i)+"\t"+ str(recur_average)+"\t"+ str(memo_average))
    print("any further runs will take too much time for recursion")
    
    print("n\tMemoization\tFast Doubling")
    for i in range (1, 51):
        n=5000*i
        memo_sum=0
        doubling_sum=0
        for j in range(1, 6):
            memo_start=time.perf_counter()
            fibonacci_memoization(n)
            memo_end=time.perf_counter()
            memo_run=(memo_end-memo_start)*1000            
            memo_sum+=memo_run
            doubling_start=time.perf_counter()
            fibonacci_fast_doubling(n)
            doubling_end=time.perf_counter()
            doubling_run=(doubling_end-doubling_start)*1000            
            doubling_sum+=doubling_run
        memo_average=memo_sum/5
        doubling_average=doubling_sum/5
        print(str(n)+"\t"+ str(memo_average)+"\t"+ str(doubling_average))
    print("any further runs will take too much time")

if __name__=="__main__":
    main()
