from MyPythonSub import InputIntList

no_sort_list = InputIntList("элементы исходного списка, значения которых больше предыдущего элемента")
print([no_sort_list[i] for i in range(len(no_sort_list)) if i != 0 and no_sort_list[i] > no_sort_list[i-1]])
