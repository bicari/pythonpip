
import csv


def read_csv(path='data.csv'):
    list_dict = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        firstline = next(reader)
        #print(firstline)
        for i in reader:
            new_reader = (zip(firstline, i))
            dict_reader = {key: value for key, value in new_reader}
            list_dict.append(dict_reader)
        #print(list_dict)
    return list_dict        

if __name__ == '__main__':
    var = read_csv('data.csv')
    print(var)