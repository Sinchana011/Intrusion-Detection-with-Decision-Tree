# -*- coding: utf-8 -*-
"""IntrusionDetectionKDD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TRFYCy11UXlG5utlyJho1tZD3wLJzBDH
"""

import pandas as pd

column_names = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
    'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
    'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
    'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate',
    'attack_type', 'difficulty_level' # This is the label column
    # If your file has a 43rd column (often 'difficulty'), add it here:
    # 'difficulty_level'
]

try:
  df = pd.read_csv('/content/KDDTest+.txt', header=None, names=column_names)
  print("Data loaded successfully")
  print(df.head())
  print(f"Shape of the data: {df.shape}")
except FileNotFoundError:
  print("File not found, please check the path")
except Exception as err:
  print(err)

df.head()

from sklearn.preprocessing import LabelEncoder
protocol_type_encoder = LabelEncoder()
df['protocol_type'] = protocol_type_encoder.fit_transform(df['protocol_type'])

service_encoder = LabelEncoder()
df['service'] = service_encoder.fit_transform(df['service'])

flag_encoder = LabelEncoder()
df['flag'] = flag_encoder.fit_transform(df['flag'])

attack_type_encoder = LabelEncoder()
df['attack_type'] = attack_type_encoder.fit_transform(df['attack_type'])

df.head()

from sklearn.model_selection import train_test_split
x = df.drop(columns=['attack_type'])
y = df['attack_type']

x.head()

y.head()

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
print(f'Training smaples: {len(x_train)} and testing samples: {len(x_test)}')

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print('Model training completed')

predict_attacks = model.predict(x_test)
print('Predictions: ',predict_attacks.tolist())
print('Actual results: ',y_test.tolist())

from sklearn.metrics import accuracy_score
model_accuracy = accuracy_score(y_test, predict_attacks)
print(f'Model accuracy is: {(model_accuracy*100):.2f}')