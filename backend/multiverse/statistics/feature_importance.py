import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def get_importance(df: pd.DataFrame):
    #preprocessing,
    df.drop(['id', 'employee_number', 'employee_count'], axis=1, inplace=True)
    df['attrition'] = df['attrition'].map({'Yes': 1, 'No': 0})
    df = pd.get_dummies(df)
    x_train, x_test, y_train, y_test = train_test_split(df.drop('attrition', axis=1), df['attrition'], 
                                                    test_size=0.15, random_state=0)
    rf = RandomForestClassifier(n_estimators=30)
    rf.fit(x_train, y_train)
    feature_importance = pd.Series(rf.feature_importances_, index=df.drop('attrition', axis=1).columns)
    feature_importance = feature_importance.sort_values(ascending=False).nlargest(10)
    fdict = feature_importance.to_dict()
    return fdict