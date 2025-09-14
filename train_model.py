"""Example training script.

This script trains a simple pipeline on the synthetic sample dataset included and saves:
- Model/diet_pipeline.joblib  (the full pipeline)
- Model/label_encoders.joblib (dictionary with 'target' label encoder)

Run locally in a safe environment. Do NOT commit Model/ dir to git.
"""
import os
import joblib
import pandas as pd
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

BASE = Path(__file__).resolve().parent
DATA = BASE / 'Dataset' / 'sample_dataset.csv'
MODEL_DIR = BASE / 'Model'
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
# basic cleanup - this assumes the sample headers are present
numeric_cols = ['Age','Weight_kg','Height_cm']
cat_cols = ['Gender','Diabetes_Status','Activity_Level']
target_col = 'Diet_Recommendation'

X = df[numeric_cols + cat_cols]
y = df[target_col]

# simple label encoder for target
le = LabelEncoder()
y_enc = le.fit_transform(y)

num_pipe = Pipeline([
    ('impute', SimpleImputer(strategy='median')),
    ('scale', StandardScaler())
])
cat_pipe = Pipeline([
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('ohe', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', num_pipe, numeric_cols),
    ('cat', cat_pipe, cat_cols)
])

pipeline = Pipeline([
    ('pre', preprocessor),
    ('clf', RandomForestClassifier(n_estimators=50, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)
pred = pipeline.predict(X_test)
print(classification_report(y_test, pred, zero_division=0))

# Save pipeline and encoders
joblib.dump(pipeline, MODEL_DIR / 'diet_pipeline.joblib')
joblib.dump({'target': le}, MODEL_DIR / 'label_encoders.joblib')
print('Saved pipeline and encoders to Model/')
