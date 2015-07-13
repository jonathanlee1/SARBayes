#!/usr/bin/env python2
# SARbayes/machine-learning/evaluate.py


import numpy as np
import Orange
import sys
import time

STATS_TEMPLATE = '''Statistics: 
    
    Model name: "{}"
    Runtime: {:.3f} s
    Evaluation method: Cross Validation
    Features: {}
    
    Predicted       Actual          Instances       
    ================================================
    {}
    
    Accuracy: {:.3f} %
'''


def cross_validate(data, learner, folds=10):
    rounded = int(np.ceil(len(data)/folds)*folds)
    increment = rounded // folds
    predictions = np.empty(len(data))
    
    for index in range(0, len(data), increment):
        lowerbound, upperbound = index, index + increment
        train_data = Orange.data.Table.from_table_rows(data, 
            list(range(lowerbound)) + list(range(upperbound, len(data)))
        )
        test_data = Orange.data.Table(data[lowerbound:upperbound])
        assert len(train_data) + len(test_data) == len(data)
        
        classifier = learner()(train_data)
        _predictions = classifier(test_data)
        for _index, _value in enumerate(_predictions):
            predictions[index + _index] = _value
    else:
        return predictions


def get_class_names(data):
    classes = set(instance.get_class() for instance in data)
    return {class_type.value: class_type._value for class_type in classes}


def get_confusion_matrix(data, learner, folds=10):
    predictions = cross_validate(data, learner, folds)
    class_names = get_class_names(data)
    n_classes = len(class_names)
    confusion_matrix = np.zeros((n_classes, n_classes))
    
    for instance, predicted_class in zip(data, predictions):
        actual_class = instance.get_class()._value
        confusion_matrix[int(predicted_class), int(actual_class)] += 1
    else:
        return confusion_matrix


def print_statistics(data, learner, folds=10, _file=sys.stdout):
    start = time.time()
    confusion_matrix = get_confusion_matrix(data, learner, folds)
    end = time.time()
    class_names = get_class_names(data)
    
    correct = 0
    for index in range(confusion_matrix.shape[0]):
        correct += confusion_matrix[index, index]
    else:
        accuracy = 100*correct/len(data)
    
    print(STATS_TEMPLATE.format(
        learner.name, 
        end - start, 
        ', '.join(attr.name for attr in data.domain.attributes), 
        '\n    '.join(row_name.ljust(16) + col_name.ljust(16) + 
            str(int(
                confusion_matrix[int(row_value), int(col_value)])).ljust(16) 
            for row_name, row_value in class_names.items()
            for col_name, col_value in class_names.items()
        ), 
        accuracy
    ), file=_file)


data = Orange.data.Table('ISRID')
learner = Orange.classification.NaiveBayesLearner
print_statistics(data, learner)
