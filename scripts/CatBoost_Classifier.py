

#**CatBoost Classifier**: CatBoost is an algorithm for gradient boosting on decision trees. It divides a given dataset into random permutations and applies ordered boosting on those random permutations. CatBoost converts categorical values into numbers using various statistics on combinations of categorical features and combinations of categorical and numerical features.


model_cat=CatBoostClassifier(loss_function='MultiClass',eval_metric='MultiClass',task_type='GPU',verbose=False)
model_cat.fit(train_post,train_target)


models_accuracy['CatBoost Classifier']=accuracy_score(test_target,model_cat.predict(test_post))