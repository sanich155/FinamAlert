# counts = np.unique(result_array[1], return_counts=True)
# count_false = counts[1][0]
# count_true = counts[1][1]
# precent_of_true_predict = print("Правильность предсказаний равна =", "{:.0%}".format(count_true/(count_true+count_false)))
# # precent_of_true_predict

def count(arr):
    t_arr = 0
    for elem in arr[1]:
        if elem == True:
            t_arr += 1
    return t_arr/len(arr[1])
