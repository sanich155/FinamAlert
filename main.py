from comparison import create_real_array
from comparison import create_prediction_data
from comparison import find_true_csv
from comparison import find_data
from comparison import comparison

from read_prediction import create_prediction_array


if __name__ == '__main__':
    file_path = 'prediction\\prediction_all.csv'  # путь к проверяемому файлу
    prediction_array = create_prediction_array(file_path)  # создаем проверяемый массив
    tikers_list = prediction_array[0]
    result_ticker = []
    result_prediction = []
    result_array = []  # создаем массив с результатами
    need_info = []
    for num in range(len(prediction_array[0])):  # перебираем поочереди записи в проверяемом массиве
        prediction_dict = create_prediction_data(prediction_array, num)  # создаем проверяемую запись
        # real_file_name = 'tickets\\' + prediction_dict[
        #     'ticker'] + '.csv'  # создаем имя проверяющего файла из названия тикера в проверяемой записи
        exist_file_name = 'tickets\\' + prediction_dict['ticker'] + '.csv'  # создаем имф файла, который точно существуют

        try:
            if exist_file_name:  # из файла который точно существует
                real_array = create_real_array(exist_file_name)  # создаем проверяющий массив
                num_row_of_date = find_data(prediction_dict,
                                            real_array)  # находим номер строки в проверяющем массиве, на которой совпадают даты с проверяемой записью
                result_array = comparison(num_row_of_date, prediction_dict,
                                          real_array)  # сравниваем и записываем в массив с результатами название тикера и результат проверки
        except:
            need_info.append(exist_file_name)
            print(exist_file_name + 'not exist')
    print(result_array)
    print(len(real_array[0]))
    print(len(real_array[1]))
    print(len(need_info))