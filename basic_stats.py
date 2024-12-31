import math as m

def mean(num_list:list) -> int|float:
    """
    Returns the mean/average of the given dataset

    Parameters:
        num_list(list): List of data values

    Returns:
        int|float: The mean or average value of the dataset
    """
    sums = 0
    for i in range(len(num_list)):
        sums += num_list[i]
    return sums/len(num_list)

def trim_mean(num_list:list, percent:float) -> int|float:
    """
    Retruns the trimmed mean of a dataset

    Parameters:
        num_list(list): List of values to trim and evaluate mean of
        percent(float): Percent value in decimal form (0-1) indicating percentage to trim from dataset

    Returns:
        int|float: Mean of the trimmed dataset
    """
    num_list = sorted(num_list)
    num_list = sorted(num_list)
    trim_amt = int((len(num_list) * percent) / 100)
    print(trim_amt)
    return mean(num_list[trim_amt : len(num_list)-trim_amt])

def weight_mean(num_list:list, weights:list) -> int|float:
    """
    Returns the weighted mean of the inputed dataset

    Parameters:
        num_list(list): List of data values to be evaluated
        weights(list): List of weighted values corresponding to num_list

    Returns:
        int|float: Weighted Mean value of dataset
    """
    if len(weights) == len(num_list):
        sums = 0
        for i in range(len(num_list)):
            sums += num_list[i] * weights[i]
        return sums / sum(weights)
    else:
        return "ERROR!: List lengths do not coincide. Please ensure correct data values have been entered"

def geo_mean(num_list:list) -> int|float:
    """
    Returns the geometric mean of the data set that is input

    Parameters:
        num_list(list): List of the data to be calculated

    Returns:
        int|float: Geometric Mean of dataset
    """
    prod = 1
    for i in num_list:
        prod *= i
    return prod ** (1/len(num_list))

def median(num_list:list) -> int|float:
    """
    Returns middle value(median) of the set of data values

    Parameters:
        num_list(list): List of data values to be calculated

    Returns:
        int|float: Middle most value of data set
    """
    num_list = sorted(num_list)
    if len(num_list) % 2 == 1:
        return num_list[(len(num_list)//2)]
    elif len(num_list) % 2 == 0:
        return ((len(num_list)//2 + (len(num_list)//2 + 1))/2)
    
def mode(num_list:list) -> int|float:
    """
    Returns the single mode of a dataset

    Parameters:
        num_list(list): List of data values to be calculated

    Returns:
        int|float: Most frequent value in dataset, a.k.a. the mode
    """
    cnt_dict = {}
    for i in num_list:
        if i in cnt_dict:
            cnt_dict[i] += 1
        else:
            cnt_dict[i] = 0
    return max(cnt_dict, key=cnt_dict.get)

def range(num_list:list)-> int|float:
    """
    Returns the range of a data set

    Parameters:
        num_list(list): List of data values to be calculated

    Returns:
        int|float: difference between max and min values in list
    """
    return max(num_list) - min(num_list)

def variance(num_list:list, avg:int|float, opt:int) -> int|float:
    """
    Returns the variance of a data set given list of numbers, the avg/mean, and an option
    deciding whether to return a sample or population variation

    Parameters:
        num_list(list): Gives list of numbers to be analyzed
        avg(float): Gives the average/mean value of the data set
        opt(int): Used to represent whether calculation should be for sample(1) or population(2)

    Returns:
        int|float: The vairiance of the dataset
    """
    if opt == 1:
        return ((avg) ** 2)/len(num_list)
    elif opt == 2:
        return ((avg)**2)/(len(num_list)-1)

def std_dev(vari:int|float) -> float:
    """
    Returns the standard deviation of a dataset given that dataset's Variance

    Parameters:
        vari(int|float): The variance of the dataset being evaluated

    Returns:
        float: The standard deviation of the data
    """
    return m.sqrt(vari)

def z_score(num, avg, sd):
    return (num-avg)/sd

def percentile(num_list, perc):
    num_list = sorted(num_list)
    percent = (perc/100) * (len(num_list) + 1)
    int_perc, dec_perc = m.modf(percent)
    return num_list[int_perc] + dec_perc * (num_list[int_perc+1]-num_list[int_perc])

def quartile(num_list, qrt):
    if qrt == 1:
        qrt = 25
    elif qrt == 2:
        qrt == 50
    elif qrt == 3:
        qrt == 75

    return percentile(num_list, qrt)

def iqr(num_list):
    return quartile(num_list, 3) - quartile(num_list, 1)


def cof_of_vari(stand_dev:float, var_mean:int|float) -> float:
    """
    
    """
    return (stand_dev/var_mean) * 100

def skewness(num_list:list, var_mean:int|float, standard_dev:float) -> float:
    """
    
    """
    leng = len(num_list)
    coef = leng/((leng-1) * (leng-2))
    sums = 0
    for i in num_list:
        pass
        


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