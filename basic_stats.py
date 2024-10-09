import math as m
import csv
import os

def mean(num_list):
    sums = 0
    for i in range(len(num_list)):
        sums += num_list[i]
    return sums/len(num_list)

def trim_mean(num_list, percent):
    num_list = sorted(num_list)
    trim_amt = int((len(num_list) * percent) / 100)
    print(trim_amt)
    return mean(num_list[trim_amt : len(num_list)-trim_amt])

def weight_mean(num_list, weights):
    sums = 0
    for i in range(len(num_list)):
        sums += num_list[i] * weights[i]
    return sums / sum(weights)

def geo_mean(num_list):
    prod = 1
    for i in num_list:
        prod *= i
    return prod ** (1/len(num_list))

def median(num_list):
    num_list = sorted(num_list)
    if len(num_list) % 2 == 1:
        return num_list[(len(num_list)//2)]
    elif len(num_list) % 2 == 0:
        return ((len(num_list)//2 + (len(num_list)//2 + 1))/2)
    
def mode(num_list):
    cnt_dict = {}
    for i in num_list:
        if i in cnt_dict:
            cnt_dict[i] += 1
        else:
            cnt_dict[i] = 0
    return max(cnt_dict, key=cnt_dict.get)

def range(num_list):
    return max(num_list) - min(num_list)

def variance(num_list, avg, opt):
    if opt == 1:
        return ((avg) ** 2)/len(num_list)
    elif opt == 2:
        return ((avg)**2)/(len(num_list)-1)

def std_dev(vari):
    return m.sqrt(vari)

def z_score(num, avg, sd):
    return (num-avg)/sd




def main():
    nums = [9, 30, 20, 2, 3, 9, 2, 9, 9, 10, 20, 32, 11, 33, 22, 56, 1, 23, 5000, 3, 2, 4, 6, 8, 10]
    trim_perc = 5
    weight = []

    mean_val = mean(nums)
    median_val = median(nums)
    mode_val = mode(nums)
    trim_val = trim_mean(nums, trim_perc)

    print(f"Mean = {mean_val:.2f}")
    print(f"Median = {median_val:.2f}")
    print(f"Mode = {mode_val:.2f}")
    print(f"{trim_perc}% Trimmed Mean = {trim_val:.2f}")

if __name__ == "__main__":
    main()