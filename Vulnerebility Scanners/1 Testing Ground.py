my_dict = {"a":1, "b": 1, "c": 3, "d": 1}
keys = my_dict.keys()
print(keys)

j = 0
for i in my_dict:
    if (j == 1):
        print("2nd key using loop: " + i)
    j = j + 1

value = my_dict["a"]
print(value)

def my_function(**kid):
    print("His last name is " + kid ["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_fruits(fruit = "Apple"):
    print("We sold one " + fruit)
my_fruits("Apple")
my_fruits("Orange")
my_fruits("Pear")
my_fruits()

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(4))
print(my_function(8))

#Using OneHotEncoder

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Create a dummy employee dataset
data = {
    'Employee id': [10, 20, 15, 25, 30],
    'Gender': ['M', 'F', 'F', 'M', 'F'],
    'Remarks': ['Good', 'Nice', 'Good', 'Great', 'Nice']
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)
print(f"Original Employee Data:\n{df}\n")

# Use pd.get_dummies() to one-hot encode the categorical columns
df_pandas_encoded = pd.get_dummies(df, columns=['Gender', 'Remarks'], drop_first=True)
print(f"One-Hot Encoded Data using Pandas:\n{df_pandas_encoded}\n")

# Initialize OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

categorical_columns = ['Gender','Remarks']

# Fit and transform the categorical columns
one_hot_encoded = encoder.fit_transform(df[categorical_columns])

# Create a DataFrame with the encoded columns
one_hot_df = pd.DataFrame(one_hot_encoded, 
                          columns=encoder.get_feature_names_out(categorical_columns))

# Concatenate the one-hot encoded columns with the original DataFrame
df_sklearn_encoded = pd.concat([df.drop(categorical_columns, axis=1), one_hot_df], axis=1)

print(f"One-Hot Encoded Data using Scikit-Learn:\n{df_sklearn_encoded}\n")