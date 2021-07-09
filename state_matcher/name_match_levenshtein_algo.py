import numpy as np
from  fuzzywuzzy import  fuzz 

"""
This is python implementation of Lavenshtein distance used in lingustic as a metric.
    Space Complexity = O(n**2)
    Time Complexity = O(n**2)
    rahul rah
"""


def name_matching_algo(original_string, test_string):
    """
        Get the result from name_matching and print it
    """

    result_case_1 = name_matching_levestein(original_string, test_string, ratio_calc=True) * 100
    result_case_2 = name_matching_part_2(original_string, test_string)
    result = max(result_case_1, result_case_2) 
    return { result : original_string }



def name_matching_levestein(original_string, test_string, ratio_calc=False):
    """ 
    It predicts the result on the basis of operation in testing string to be like original 
    Substitution operations can be like 
    1) Insertion ( cost is 1)
    2) Deletion  ( cost is 1)
    3) Substition (cost is 2 if we want a ratio)  

    ((|a|+|b|)− (number of operations)) / (|a|+|b|) is the ratio formula 

    for more accuracy we can use fizzbuzz library 
"""

    rows = len(original_string) + 1
    cols = len(test_string) + 1
    distance_matrix = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        distance_matrix[i][0] = i
    for k in range(1, cols):
        distance_matrix[0][k] = k


    

    for row in range(1, rows):
        for col in range(1, cols):
            if original_string[row-1] == test_string[col-1]:
                cost = 0
            else:
                if ratio_calc == True:
                    cost = 2  
                else:
                    cost = 1
            distance_matrix[row][col] = min(distance_matrix[row-1][col] + 1,          # Cost of deletions
                                            distance_matrix[row][col-1] + 1,          # Cost of insertion 
                                            distance_matrix[row-1][col-1] + cost)     # Cost of substitutions

    if ratio_calc:
        Ratio = ((len(original_string) + len(test_string)) -
                 distance_matrix[row][col]) / (len(original_string)+len(test_string))
        return Ratio
    else:
        return "Number of change to made are {}".format(distance_matrix[row][col])

def name_matching_part_2(original_string, test_string):

    result1 = fuzz.ratio(original_string, test_string)

    # substring case 

    result2 = fuzz.partial_ratio(original_string, test_string)

    #ignore word order 

    result3 = fuzz.token_sort_ratio(original_string, test_string)

    result_list = [result1, result2, result3]

    return max(result_list)

name_matching_algo("Rahul Beniwal", "RahulBeniwal")



# 