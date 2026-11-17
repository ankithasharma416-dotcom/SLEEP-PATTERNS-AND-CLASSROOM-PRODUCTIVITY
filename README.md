Sleep Patterns and Classroom Productivity Among Engineering Students

Project Overview

This project studies the relationship between sleep patterns and classroom productivity among engineering students using data analysis and machine learning.

The project uses survey responses to train a machine learning model that predicts students' self-reported classroom productivity ratings based on selected sleep-related and study-related factors.

Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

Machine Learning

The project compares multiple classification algorithms and selects K-Nearest Neighbors (KNN) as the final model based on cross-validation Macro F1-score.

The final model uses KNN with K = 3.

Model Evaluation

The final model achieved:

- Test Accuracy: 56.67%
- Macro F1-score: 0.28
- Weighted F1-score: 0.51

These results are preliminary. The dataset is relatively small and the target classes are imbalanced, so predictions should be interpreted cautiously.

Project Files

- "data.csv" – Survey dataset.
- "Sleep_Productivity.ipynb" – Jupyter notebook containing data processing, model training, and evaluation.
- "final_classroom_productivity_model.pkl" – Saved trained machine learning pipeline.

Limitations

- The dataset is based on self-reported survey responses.
- The number of responses is limited.
- The model identifies patterns and does not establish cause-and-effect relationships.
- Predictions are not intended to be treated as definitive assessments of student productivity.

Team Members

- Ananya Shetty
- Ankitha Sharma
- Aadi D Rai

Project Guide

Dr. Vandana B S

NMAMIT, Nitte