import csv

def create_real_array(exist_file_name):  # создаем проверочный массив из csv
    real_array = []
    with open(exist_file_name, 'r') as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            real_array.append(row)
    for row_num in range(len(real_array)):  # приводим дату к нормальному формату
        date = real_array[row_num][0]
        right_date = '{}{}.{}{}.20{}{}'
        real_array[row_num][0] = right_date.format(*date)
    # print(real_array)
    return real_array

def create_prediction_data(prediction_array, num):  # создаем 1 запись из проверяемого массива
    ticker = prediction_array[0][num]
    date = prediction_array[1][num]
    invest_horizont = prediction_array[2][num]
    prediction_price = prediction_array[3][num]
    prediction_action = prediction_array[4][num]
    return {'ticker': ticker,
            'date': date,
            'invest_horizont': invest_horizont,
            'prediction_price': prediction_price,
            'prediction_action': prediction_action}

def find_true_csv(real_file_name):  # ищем по тикерам *.csv-файлы, по которым будем проверять записи
    not_exist = 0
    try:
        with open(real_file_name, 'r') as true_csv:
            return real_file_name
    except:
        not_exist = []
        return print(real_file_name + ' is not exist')
        # not_exist.append(real_file_name)

def find_data(prediction_dict,
              real_array):  # ищем в проверяющем массиве строку, в которой совпадает дата с проверяемой записью
    num_row = 0
    f_num_row = 0
    for row in real_array:
        if prediction_dict['date'] == row[0]:
            f_num_row = num_row
        num_row += 1
    return int(f_num_row)

def comparison(num_row, prediction_dict,
               real_array):  # сравниваем проверяемую запись с проверяющим массивом по нужным датам начиная со строки, на которой даты совпали
    ticker = ''
    if prediction_dict['prediction_action'] == 'Покупать':
        for row in real_array[int(num_row): int(prediction_dict['invest_horizont']) + int(num_row)]:
            if prediction_dict['prediction_price'] >= row[3]:
                ticker = prediction_dict['ticker']
                prediction = True
                break
        if ticker != prediction_dict['ticker']:
            ticker = prediction_dict['ticker']
            prediction = False
        result = [ticker, prediction]
    else:
        for row in real_array[int(num_row): int(num_row) + int(prediction_dict['invest_horizont'])]:
            if prediction_dict['prediction_price'] <= row[3]:
                ticker = prediction_dict['ticker']
                prediction = True
                break
            if ticker != prediction_dict['ticker']:
                ticker = prediction_dict['ticker']
                prediction = False
        result = [ticker, prediction]
    return result