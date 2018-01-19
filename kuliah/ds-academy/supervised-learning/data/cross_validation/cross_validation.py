from sklearn.cross_validation import StratifiedKFold

folds = StratifiedKFold(label, n_folds=10)
counter = 1
for train_index, test_index in folds:
	counter += 1
	X_text_train, X_text_test = text_data[train_index], text_data[test_index]
    y_train, y_test = label[train_index], label[test_index]