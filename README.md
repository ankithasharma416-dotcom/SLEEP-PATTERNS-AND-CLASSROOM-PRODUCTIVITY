# Sleep Patterns and Classroom Productivity Among Engineering Students

College mini-project at NMAMIT, Nitte. The project explores self-reported sleep habits and classroom productivity among engineering students and evaluates whether selected survey responses can predict a student's productivity rating.

## Objectives

- Summarize reported sleep duration, sleep quality, daytime sleepiness, and classroom productivity.
- Explore the relationship between sleep duration and productivity ratings.
- Compare classification approaches for predicting the self-reported productivity rating.
- Preserve the final trained model and its evaluation outputs for review and reuse.

## Dataset

[`dataset.csv`](dataset.csv) contains 117 survey responses and 16 columns. Each row is a student response. The target is the survey's classroom productivity rating, scored 1–5. The model uses nine sleep, bedtime, routine, sleepiness, screen-time, caffeine, and study-time features; see [`src/predict.py`](src/predict.py) for the exact column names.

The notebook's uploaded source was recorded as 117 rows × 17 columns and included a `Timestamp` field. The checked-in `dataset.csv` has 16 columns and omits `Timestamp`. The 117 response rows' distribution counts and sleep-duration/productivity cross-tab match the notebook outputs. `Timestamp` is not used as a model feature. The notebook loads its upload with `keep_default_na=False`, so empty survey answers remain empty strings and its null check does not count them. In the caffeine column, 47 such empty-string responses are displayed by pandas as `None` in the notebook's frequency table. They are retained as recorded; no imputation or edits to the original responses are applied. The notebook's “no missing values” statement should therefore be read as “no null values,” not as evidence that no response fields are blank.

## Exploratory data analysis

The notebook is the detailed record of loading, data checks, descriptive summaries, category distributions, and the sleep-duration/productivity cross-tab. The notebook outputs report 42 students (35.90%) in the 6–7 hour sleep category; the most common sleep-quality rating is 3 (51 responses); “Sometimes” is the most common lecture sleepiness response (44); and productivity rating 3 is the most common target value (55). These are descriptive summaries, not evidence of causation.

Saved charts are in [`plots/`](plots/). They were generated from the matching notebook counts and crosstab. The model charts use the cross-validation results recorded in the notebook.

## Machine-learning workflow

The notebook splits the data with `train_test_split(test_size=0.25, random_state=42, stratify=y)`, giving 87 training and 30 test rows. Categorical features are one-hot encoded with unknown categories ignored; the two numeric rating features pass through unchanged. Models are compared using a shuffled 4-fold `StratifiedKFold` with `random_state=42` on the training partition. KNN neighborhood sizes are compared using cross-validated macro F1. The selected KNN pipeline is then fit on the training partition and evaluated once on the held-out test partition.

Models compared in the final notebook comparison: Dummy Classifier, Decision Tree, Random Forest, Logistic Regression, SVM, and KNN (K=3). The notebook also contains earlier exploratory model runs; the CSV records the final comparison table from notebook cell 46.

## Final model and performance

The saved model is [`models/final_classroom_productivity_model.pkl`](models/final_classroom_productivity_model.pkl): a scikit-learn pipeline with one-hot categorical encoding, passthrough numeric values, and `KNeighborsClassifier(n_neighbors=3)`. K=3 had the best macro F1 (0.431) among the six tested K values in the notebook's unscaled KNN parameter comparison. The notebook separately explored a scaled KNN variant; it was not used for the final model.

Held-out test results from the notebook:

| Metric | Score |
|---|---:|
| Accuracy | 56.67% (17/30) |
| Macro F1 | 0.28 |
| Weighted F1 | 0.51 |

The full classification report and 5×5 confusion matrix are in [`results/final_evaluation.txt`](results/final_evaluation.txt). Model comparison and KNN parameter values are in [`results/model_comparison.csv`](results/model_comparison.csv) and [`results/knn_parameter_comparison.csv`](results/knn_parameter_comparison.csv). Performance is preliminary: the dataset is small, self-reported, and the target classes are imbalanced; the model does not establish cause and effect.

## Repository structure

```text
dataset.csv
data_science_project_final.ipynb       # primary detailed workflow and recorded outputs
models/final_classroom_productivity_model.pkl
plots/                                  # eight labeled SVG charts
results/                                # CV tables and final evaluation
src/predict.py                          # prediction helper and CLI
README.md
requirements.txt
```

## Setup and use

Use Python 3.10 or newer, then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Open `data_science_project_final.ipynb` in Jupyter Notebook or Google Colab to review the complete analysis. In Colab, upload the survey CSV when prompted. The notebook's recorded upload included an extra `Timestamp` column, but that field is not used in the analysis or model. Its saved outputs document the original run; rerunning it requires the same source survey export for identical column names and results.

To make one prediction with the checked-in model, run from the repository root and supply values using the survey's category labels. Example:

```bash
python src/predict.py --sleep-duration "6-7" --bedtime "10-11 PM" --schedule-consistency 4 --late-study-frequency Sometimes --sleep-quality 3 --lecture-sleepiness Sometimes --screen-time "30-60 minutes" --caffeine 1 --study-hours "1-2 hours"
```

The command prints an integer productivity rating from 1 to 5. Predictions are exploratory and should not be used as definitive assessments of students.

## Team

| Name | USN |
|---|---|
| Ananya Shetty | NN25ISE028 |
| Ankitha Sharma | NN25ISE032 |
| Aadi D Rai | NN25ISE002 |

**Project guide:** Dr. Vandana B S, NMAMIT, Nitte

**Domain:** Machine Learning
