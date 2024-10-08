import math as m
import os
import csv

def expected_value(vals_list, probs_list):
    sum = 0
    if len(vals_list) == len(probs_list):
        for i in range(len(vals_list)):
            sum += vals_list[i] * probs_list[i]
    return sum

def random_variance(vals_list, probs_list, expec_val):
    sum = 0
    if len(vals_list) == len(probs_list):
        for i in range(len(vals_list)):
            sum += (vals_list[i]-expec_val)*probs_list[i]
    return sum

def random_std_deviation(expec_val):
    return m.sqrt(expec_val)

def main():
    file = input("Enter csv file ")
    pass

if __name__ == '__main___':
    main()