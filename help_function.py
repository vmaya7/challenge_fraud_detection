import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import scikitplot as skplt
import seaborn as sns #Visualization
import matplotlib.pyplot as plt #Visualization

'''
evaluate
    Input
        model --> model used
        x --> Xtrain/X_test or vector of predictions
        y --> y_train/y_test
        pred_vector = False --> is vector of predictions used?
        normalize_m = None --> Do I want normalize?
        
    Output
        classification_report and plot confussion matrix
'''


def evaluate(model, x, y, pred_vector = False, normalize_m = None):
    
    if pred_vector:
        y_predict = x
    else:
        y_predict = model.predict(x)
    print(classification_report(y, y_predict))
    plt.rcParams.update({'font.size': 14})
    cm = confusion_matrix(y, y_predict)
    skplt.metrics.plot_confusion_matrix(y, y_predict,  figsize=(12,12), normalize = normalize_m)

def get_importance(model, columns):
    plt.figure(figsize=(15, 10))
    coeff = list(model.coef_[0])
    df = pd.DataFrame({'Variables': columns, 'Coefficients': coeff})
    df = df.sort_values('Coefficients', ascending = True)
    sns.barplot(y = 'Variables', x = 'Coefficients', data = df)
    #_ = plt.xticks(rotation=90)