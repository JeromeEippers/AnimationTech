from sklearn.ensemble import ExtraTreesRegressor

def reach_train_value_function(X_train, y_train, PRE_COMPUTE_TABLE_INDICES, reshape_dim):
    model = ExtraTreesRegressor(n_estimators=25, random_state=None)
    model.fit(X_train, y_train)
    preds = model.predict(PRE_COMPUTE_TABLE_INDICES)
    return preds.reshape(reshape_dim, reshape_dim)