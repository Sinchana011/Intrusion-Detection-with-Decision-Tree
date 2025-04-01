# Intrusion-Detection-with-Decision-Tree

This repository contains implementations of an Intrusion Detection System (IDS) using the DecisionTreeClassifier on two different datasets:
1. small_IDS – A lightweight dataset for quick experimentation.
2. IntrusionDetectionKDD – Uses the NSL-KDD dataset, a standard benchmark for intrusion detection.

This project builds an Intrusion Detection System (IDS) that can classify network traffic as either normal or attack using a DecisionTreeClassifier.

Technologies used:
1. Python
2. pandas
3. scikit-learn -> Machine learning (LabelEncoder, train_test_split, accuracy_score)

Project Workflow:
1. Data preprocessing:
   Read the dataset into a pandas DataFrame
   Identify categorical columns and apply Label Encoding
2. Model training
   Split dataset into train (80%) and test (20%)
   Train the DecisionTreeClassifier
3. Model Evaluation
   Compare model performance on both datasets
