import csv
#создаем список предсказаний, которые надо проверить
def create_prediction_array(file_path):
    with open(file_path, 'r') as fp:
        reader = csv.reader(fp)

        prepeare_list = []
        t_list = []
        d_list = []
        lpr_list = []
        lp = []
        hpr_list = []
        c_list = []
        prediction = []
        a = 1
        for i in reader:
            prepeare_list.append(i)

        for each in prepeare_list:
            if a == 1:
                t_list = t_list + each
            if a == 2:
                d_list = d_list + each
            if a == 3:
                lpr_list = lpr_list + each
            if a == 4:
                hpr_list = hpr_list + each
            if a == 5:
                c_list = c_list + each
            a = a + 1
            if a == 6:
                a = 1

        for each in lpr_list:
            if each != '':
                lp.append(each)
            else:
                lp.append(1)

        prediction.append(t_list)
        prediction.append(d_list)
        prediction.append(lp)
        prediction.append(hpr_list)
        prediction.append(c_list)

    return prediction