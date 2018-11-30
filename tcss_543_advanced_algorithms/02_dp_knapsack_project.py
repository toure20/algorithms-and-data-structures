# bottom-up dp: traverses iteratively starting from the smallest subset (bottom) going up
# ex: fib(1), fib(2), fib(3), fib(4), ... , fib(n)
def knapsack_bottom_up_dp(weights, values, W):
    # generating array for storing optimal values
    n = len(weights)
    opt_vals = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # computing possible optimal values
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            wi = weights[i - 1]
            # if weight of the current item is greater than the current weight
            # take the previous optimal value from previous top slot (i - 1)
            if wi > w:
                opt_vals[i][w] = opt_vals[i - 1][w]
            # otherwise, take the maximum between:
            # putting the current item into the knapsack or not
            else:
                opt_vals[i][w] = max(values[i - 1] + opt_vals[i - 1][w - wi], 
                                     opt_vals[i - 1][w])

    # backtracking
    opt_subset = [0 for i in range(n)]
    i, w = n, W
    while i > 0 and w > 0:
        wi = weights[i - 1]
        if w - wi >= 0 and opt_vals[i][w] == values[i - 1] + opt_vals[i - 1][w - wi]:
            opt_subset[i - 1] = 1
            w -= wi
        i -= 1    

    # for i in opt_vals: print(i)
    return (opt_vals[-1][-1], opt_subset)

# top-down: recursively computes values starting from the biggest (top) going down
# ex: fib(n), fib(n-1), fib(n-2), ... , fib(1)
def knapsack_top_down_dp(weights, values, W):
    # generating array for storing optimal values with 0 in edges and -1 elsewhere
    n = len(weights)
    opt_vals = [[0 for _ in range(W + 1)]]
    [opt_vals.append([0 if j == 0 else -1 for j in range(W + 1)]) for _ in range(n)]

    # run recursion
    max_val = helper(weights, values, opt_vals, n, W)

    # backtracking
    opt_subset = [0 for i in range(n)]
    i, w = n, W
    while i > 0 and w > 0:
        wi = weights[i - 1]
        if w - wi >= 0 and opt_vals[i][w] == values[i - 1] + opt_vals[i - 1][w - wi]:
            opt_subset[i - 1] = 1
            w -= wi
        i -= 1  

    # for i in opt_vals: print(i)
    return (max_val, opt_subset)

def helper(weights, values, opt_vals, i, w):
    # base case
    if opt_vals[i][w] >= 0:
        return opt_vals[i][w]

    # skip the item if the wieght of item is bigger than the remaining weight in the knapsack
    if weights[i - 1] > w :
        max_val = helper(weights, values, opt_vals, i - 1, w)
    # otherwise, recursively compute maximum between picking the item or not picking the item
    else:
        max_val = max(values[i - 1] + helper(weights, values, opt_vals, i - 1, w - weights[i - 1]),
                      helper(weights, values, opt_vals, i - 1, w))
    
    # memorize the computed maximum value
    opt_vals[i][w] = max_val
    return max_val

# brute force: generate all possible 2^n variants and determine the maximum optimal value
# without bit manipulation
import itertools
def knapsack_brute_force(weights, values, W):
    # initializing length, maximum total value and optimal subset of selected items
    n, max_val, opt_subset = len(weights), 0, []

    # creating a generator, that traveses through all possible combinations of selecting n items
    combinations = map(list, itertools.product([0, 1], repeat=n))

    # iterating over all combinations
    for cmb in combinations:
        # calcualting total weight and total value for current combination
        tot_weights = sum([a*b for a,b in zip(weights, cmb)])
        tot_values = sum([a*b for a,b in zip(values, cmb)])

        # updating maximum total value and optimal subset to current 
        if tot_weights <= W and tot_values > max_val:
            max_val = tot_values
            opt_subset = cmb
    
    return (max_val, opt_subset)

# with bit manipulation
def knapsack_brute_force_bm(weights, values, W):
    # initializing length, maximum total value and optimal subset of selected items
    n, max_val = len(weights), 0
    opt_subset = [0]*n
    i, m = 1, 2**n

    # iterating over all combinations
    while i < m:
        j, tot_weights, tot_values, cur = i, 0, 0, 0
        cur_subset = [0]*n
        while j:
            if j & 1:
                tot_weights += weights[cur]
                tot_values += values[cur]
                cur_subset[cur] = 1
            j >>= 1
            cur += 1
        i+=1
        
        # updating maximum total value and optimal subset to current 
        if tot_weights <= W and tot_values > max_val:
            max_val = tot_values
            opt_subset = cur_subset
    
    return (max_val, opt_subset)

# correctness testing
def easy_test():
    print("BOTTOM UP:")
    print(knapsack_bottom_up_dp([2,2,3], [2,3,4], 6))
    print(knapsack_bottom_up_dp([2,2,3], [7,2,1], 6))

    print("TOP DOWN:")
    print(knapsack_top_down_dp([2,2,3], [2,3,4], 6))
    print(knapsack_top_down_dp([2,2,3], [7,2,1], 6))

    print("BRUTE FORCE:")
    print(knapsack_brute_force([2,2,3], [2,3,4], 6))
    print(knapsack_brute_force([2,2,3], [7,2,1], 6))

    print("BRUTE FORCE (bit manip.):")
    print(knapsack_brute_force_bm([2,2,3], [2,3,4], 6))
    print(knapsack_brute_force_bm([2,2,3], [7,2,1], 6))

import random
import time
import numpy as np
import pandas as pd

# N = np.arange(1, 26, 1)         #[1, 2, ..., 25]
# K = np.arange(0.2, 1.1, 0.2)    #[0.1, 0.2, ..., 1]
# wi_vi_power = np.arange(3, 10, 2)  #[3, 5, 7, 9]
N = np.arange(1, 100, 1)         #[1, 2, ..., 25]
K = np.arange(0.2, 1.1, 0.2)    #[0.1, 0.2, ..., 1]
wi_vi_power = np.arange(3, 6, 2)  #[3, 5, 7, 9]
# functions = [knapsack_brute_force, knapsack_bottom_up_dp, knapsack_top_down_dp]
functions = [knapsack_bottom_up_dp, knapsack_top_down_dp]
def main():
    test()

# full testing
def test():
    runtimes = [[], [], []] # BF_time, DP_BU_time, DP_TD_time 
    n_arr = []
    W_arr = []
    wi_vi_range_arr = []

    for ni in N:
        for wi_vi in wi_vi_power:
            test_case_w = np.random.randint(10**wi_vi, size=ni)
            test_case_v = np.random.randint(10**wi_vi, size=ni)
            sum_test_case = sum(test_case_w)
            for ki in K:           
                n_arr.append(ni)
                W_arr.append(int(sum_test_case * ki))

                print(test_case_w)

                wi_vi_range_arr.append(10**wi_vi)

                for i in range(len(functions)):
                    print(test_case_w)
                    start = time.clock()
                    functions[i](test_case_w, test_case_v, int(sum_test_case * ki))
                    end = time.clock()
                    runtimes[i].append(end - start)

    # df = pd.DataFrame({"BF": runtimes[0], "BU": runtimes[1], "TD": runtimes[2],
    #                    "n": n_arr, "W": W_arr, "wi, vi range": wi_vi_range_arr})
    df = pd.DataFrame({"BU": runtimes[0], "TD": runtimes[1],
                       "n": n_arr, "W": W_arr, "wi, vi range": wi_vi_range_arr})

    df.to_csv("df.csv")

main()

# print(random.sample(range(200), 1))
# print(random.sample(range(300), 100))
n = 23

# start = time.clock()
# print(knapsack_brute_force(random.sample(range(n * 10), n),random.sample(range(n * 10), n), 1000))
# end = time.clock()
# print(end - start)

# start = time.clock()
# print(knapsack_brute_force_bm(random.sample(range(n * 10), n),random.sample(range(n * 10), n), 1000))
# end = time.clock()
# print(end - start)