import pandas as pd
import transformation as tf

def main():
    data = pd.read_csv("iris.txt", header=None)
    del data[4]

    # minmax = tf.minmax(data)
    # minmax.to_csv("iris_minmax.csv",header=False,index=False)

    zscore = tf.zscore(data)
    # zscore.to_csv("iris_zscore.csv",header=False,index=False)

    # decimal = tf.decimal(data)
    # decimal.to_csv("iris_decimal.csv",header=False,index=False)
    #
    # sigmoid = tf.sigmoid(data)
    # sigmoid.to_csv("iris_sigmoid.csv",header=False,index=False)
    #
    # softmax = tf.softmax(data)
    # softmax.to_csv("iris_softmax.csv",header=False,index=False)

    # data = pd.read_csv("newthyroid.txt", sep="\t",header=None)
    # del data[5]
    #
    # minmax = tf.minmax(data)
    # minmax.to_csv("thyroid_minmax.csv",header=False,index=False)
    #
    # zscore = tf.zscore(data)
    # zscore.to_csv("thyroid_zscore.csv",header=False,index=False)
    #
    # decimal = tf.decimal(data)
    # decimal.to_csv("thyroid_decimal.csv",header=False,index=False)
    #
    # sigmoid = tf.sigmoid(data)
    # sigmoid.to_csv("thyroid_sigmoid.csv",header=False,index=False)
    #
    # softmax = tf.softmax(data)
    # softmax.to_csv("thyroid_softmax.csv",header=False,index=False)

if __name__ == '__main__':
    main()
