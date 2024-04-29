
#**Support Vector classifier**: It is a supervised machine learning model that uses classification algorithms for two-group classification problems. It takes the data points and outputs the hyperplane (which in two dimensions it’s simply a line) that best separates the tags.

model_svc=SVC()
model_svc.fit(train_post,train_target)


models_accuracy['Support Vector classifier']=accuracy_score(test_target,model_svc.predict(test_post))