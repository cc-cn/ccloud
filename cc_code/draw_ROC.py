from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt


print('hello world')

num=1000
y_true=np.zeros(num)

for i in range(num):
    y_true[i]=np.random.randint(0,2)

y_score=np.zeros(num)
for i in range(num):
    if y_true[i]==1:
        y_score[i]=np.random.uniform(0.4,1)
    else:
        y_score[i] = np.random.uniform(0, 0.6)

fpr, tpr, thresholds=metrics.roc_curve(y_true, y_score, pos_label=None, sample_weight=None, drop_intermediate=True)


auc=metrics.auc(fpr, tpr)
print(auc)

'''
#print(thresholds)
plt.plot(fpr, tpr)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC')

plt.show()
'''




