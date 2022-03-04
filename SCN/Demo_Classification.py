from SCN import SCN
import numpy as np
import itertools
import matplotlib.pyplot as plt
import scipy.io

# Parameter Setting
L_max = 10                    # maximum hidden node number
tol = 0.01                    # training tolerance
T_max = 100                    # maximun candidate nodes number
Lambdas = [0.5, 1, 5, 10, 30, 50, 100]  # scope sequence
r = [0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999]  # 1-r contraction sequence
nB = 1       # batch size
verbose = 4

# Model Initialization
M = SCN(L_max, T_max, tol, Lambdas, r, nB, verbose)

mat = scipy.io.loadmat('Demo_Iris.mat')
T = mat['T']
X = mat['X']
T2 = mat['T2']
X2 = mat['X2']
class_names = np.array(['setosa', 'versicolor', 'virginica'])

ErrorList,RateList = M.classification(np.array(X), np.array(T))


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

plt.figure()
fig, ax1 = plt.subplots()
color1 = 'tab:red'
ax1.set_ylabel('RMSE', color=color1)
ax1.plot(range(0, ErrorList.shape[1]),
         ErrorList.reshape(-1, 1).tolist(), 'r.-')
ax1.legend(['Training RMSE'])


ax2 = ax1.twinx()
color2 = 'tab:blue'
ax2.set_ylabel('ACC', color=color2)
ax2.plot(range(0, RateList.shape[1]),
          RateList.reshape(-1, 1).tolist(), 'b.-')
ax2.axis(ymin=0, ymax=1)
ax2.legend(['Training ACC'])


(ErrorA, CMA) = M.getAccuracy(X, T)

plt.figure()


plot_confusion_matrix(CMA, classes=class_names,
                      title='Confusion matrix, Training')


(ErrorB, CMB) = M.getAccuracy(X2, T2)

plt.figure()

plot_confusion_matrix(CMB, classes=class_names,
                      title='Confusion matrix, Testing')

plt.show()
