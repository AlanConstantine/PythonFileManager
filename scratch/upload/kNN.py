# -*- coding: utf-8 -*-
# @Date    : 2017-04-03 15:47:04
# @Author  : Alan Lau (rlalan@outlook.com)
import numpy as np
import distance
import fwalker
import reader
import statistic


def get_data(data_path):
    label_vec = []
    files = fwalker.fun(data_path)
    for file in files:
        ech_label_vec = []
        ech_label = int((file.split('\\'))[-1][0])
        ech_vec = ((np.loadtxt(file)).ravel())
        ech_label_vec.append(ech_label)
        ech_label_vec.append(ech_vec)
        label_vec.append(ech_label_vec)
    return label_vec


def find_label(train_vec_list, vec, k):
    get_label_list = []
    for ech_trainlabel_vec in train_vec_list:
        ech_label_distance = []
        train_label, train_vec = ech_trainlabel_vec[0], ech_trainlabel_vec[1]
        vec_distance = distance.Euclidean(train_vec, vec)
        ech_label_distance.append(train_label)
        ech_label_distance.append(vec_distance)
        get_label_list.append(ech_label_distance)
    result_k = np.array(get_label_list)
    order_distance = (result_k.T)[1].argsort()
    order = np.array((result_k[order_distance].T)[0])
    top_k = np.array(order[:k], dtype=int)
    find_label = statistic.orderdic(statistic.statistic(top_k), True)[0][0]
    return find_label


def classify(train_vec_list, test_vec_list, k):
    error_counter = 0
    for ech_label_vec in test_vec_list:
        label, vec = ech_label_vec[0], ech_label_vec[1]
        get_label = find_label(train_vec_list, vec, k)
        print('Original label is:'+str(label) +
              ', kNN label is:'+str(get_label))
        if str(label) != str(get_label):
            error_counter += 1
        else:
            continue
    true_probability = str(
        round((1-error_counter/len(test_vec_list))*100, 2))+'%'
    print('Correct probability:'+true_probability)


def main():
    k = 3
    train_data_path = r'D:\DevelopmentLanguage\Python\MachineLearning\Learning\KNN\lab3_0930\input_digits\trainingDigits'
    test_data_path = r'D:\DevelopmentLanguage\Python\MachineLearning\Learning\KNN\lab3_0930\input_digits\testDigits'
    train_vec_list = get_data(train_data_path)
    test_vec_list = get_data(test_data_path)
    classify(train_vec_list, test_vec_list, k)

if __name__ == '__main__':
    main()
