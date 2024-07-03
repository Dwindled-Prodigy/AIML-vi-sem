from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

iris = datasets.load_iris()
print("Dataset loaded successfully")

for i in range(len(iris.target_names)):
  print(f"Label {i} - {iris.target_names[i]}")

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1)

model = KNeighborsClassifier(3)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

for i in range(len(X_test)):
  print(f"Sample {X_test[i]}: Actual: {y_test[i]} Predicted: {predictions[i]}")

print(f"Accuracy = {model.score(X_test, y_test)}")