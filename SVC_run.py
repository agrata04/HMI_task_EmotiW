
import sklearn

class SVC_run:

  def SVC_method(data):
 df = pd.DataFrame(lbp)
  
#use SVC with chi-squared svc
  
  
  target = [02,03,04,05,06,07,08,01]
  
  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109)
  
  #Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

accuracy = metrics.accuracy_score(y_test, y_pred)
print(accuracy)

precision = metrics.precision_score(y_test, y_pred)
print(precision)

con_mat = metrics.confusion_matrix(y_true, y_pred)
print(con_mat)


