import pandas as pd
from sklearn.model_selection import train_test_split
import category_encoders as ce
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv("C:\\Users\\Muthukumar_S\\Downloads\\car.data", header = None)
df.columns = ["buying", "maintenance", "no_doors", "no_persons", "luggage_boot", "safety", "class"]
X = df.drop(['buying'], axis=1)
y = df['buying']
encoder = ce.OrdinalEncoder(cols=['maintenance', 'no_doors', 'no_persons', 'luggage_boot', 'safety','class'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)
clf_gini = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
clf_gini.fit(X_train, y_train)
y_pred_gini = clf_gini.predict(X_test)
from sklearn.metrics import accuracy_score
print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y_test, y_pred_gini)))
y_pred_train_gini = clf_gini.predict(X_train)
print(y_pred_train_gini)
print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train_gini)))
print('Training set score: {:.4f}'.format(clf_gini.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(clf_gini.score(X_test, y_test)))
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred_gini)
print('Confusion matrix\n\n', cm)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred_gini))

