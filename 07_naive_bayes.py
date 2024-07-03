import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('/content/tennisdata.csv')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

le = LabelEncoder()
X.Outlook = le.fit_transform(X.Outlook)
X.Temperature = le.fit_transform(X.Temperature)
X.Humidity = le.fit_transform(X.Humidity)
X.Windy = le.fit_transform(X.Windy)
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

model = GaussianNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Accuracy = {accuracy_score(y_test, predictions)}")
