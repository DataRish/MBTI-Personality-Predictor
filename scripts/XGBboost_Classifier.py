
#XGBoost Classifier : It is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a wrapper class to allow models to be treated like classifiers or regressors in the scikit-learn framework

model_xgb=XGBClassifier(gpu_id=0,tree_method='gpu_hist',max_depth=5,n_estimators=50,learning_rate=0.1)
model_xgb.fit(train_post,train_target)


models_accuracy['XGBoost Classifier']=accuracy_score(test_target,model_xgb.predict(test_post))