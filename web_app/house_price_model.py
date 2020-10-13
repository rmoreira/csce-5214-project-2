class HousePriceModel:
    
    def __init__(self, model_name, param, features):
        self.model_name = model_name
        pipe = Pipeline(steps=[('scaler', StandardScaler()), ('rf', RandomForestRegressor(random_state=42))])
        self.model = GridSearchCV(estimator=pipe, param_grid=param, cv=3, n_jobs=-1, verbose=2)
        self.features = features
        self.feature_imp = self.metrics = None
        self.y_predict = self.y_error = None
    
    def evaluate(self, X_train, y_train, X_test, y_test):
        self.y_train = y_train
        start_time = time.time()
        self.model.fit(X_train, y_train)
        stop_time = time.time()
        self.y_predict = np.round(self.model.predict(X_test), 1)
        self.residuals = pd.DataFrame(columns=['Residuals'])
        self.residuals['Residuals'] = y_test - self.y_predict
        mse = mean_squared_error(y_test, self.y_predict)
        metrics_dict = {'model_name': self.model_name,
                        'mse': mse,             # mean squared error
                        'rmse': np.sqrt(mse),   # relative mean squared error
                        'mae': mean_absolute_error(y_test, self.y_predict),     # mean absolute error
                        'R-squared': self.model.score(X_train, y_train),
                        'training_time': stop_time - start_time}  
        self.metrics = pd.DataFrame(metrics_dict, index=[0])
        
        # sort feature importance in descending order
        self.feature_imp = pd.Series(self.model.best_estimator_._final_estimator.feature_importances_, 
                                index=self.features).sort_values(ascending=False)
    
    def plot_feature_importance(self, figsize=(6, 6)):
        fig, ax = plt.subplots(figsize=figsize)
        
        # create a bar plot of feature importance
        sns.barplot(x=self.feature_imp, y=self.feature_imp.index)

        # add labels to graph
        plt.xlabel('Score', size=13)
        plt.ylabel('Features', size=13)
        plt.title('Feature Importance', size=15)
        plt.show()