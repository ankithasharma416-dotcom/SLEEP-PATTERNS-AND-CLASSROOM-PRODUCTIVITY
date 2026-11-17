Sleep Patterns and Classroom Productivity Among Engineering Students



Machine Learning Project

College: NMAMIT, Nitte



1\. Project Overview



This project studies the relationship between sleep patterns and classroom productivity among engineering students using data analysis and machine learning.



The project uses survey responses to train a machine learning model that predicts students' self-reported classroom productivity ratings based on selected sleep-related and study-related factors.



2\. Project Objectives



\- Study sleep patterns among engineering students.

\- Analyze the relationship between sleep habits and classroom productivity.

\- Identify factors associated with students' classroom productivity.

\- Apply machine learning classification algorithms to predict productivity ratings.

\- Compare multiple classification models and select a suitable final model.



3\. Technologies Used



\- Python

\- Google Colab

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Joblib



4\. Machine Learning Methodology



The project follows these steps:



1\. Survey dataset collection.

2\. Data loading and preprocessing.

3\. Feature selection.

4\. Splitting the dataset into training and testing sets.

5\. Training and comparison of multiple classification algorithms.

6\. Model evaluation using Accuracy, Macro F1-score, Weighted F1-score and confusion matrices.

7\. Final model selection, training and saving.



Final Model



The selected final model is K-Nearest Neighbors (KNN) with:



\- Algorithm: K-Nearest Neighbors

\- Number of Neighbors (K): 3



KNN was selected based on cross-validation Macro F1-score.



5\. Model Evaluation



The final model achieved the following test results:



Evaluation Metric| Score

Accuracy| 56.67%

Macro F1-score| 0.28

Weighted F1-score| 0.51



Results Interpretation



The model achieved a test accuracy of 56.67%.



The dataset is relatively small and the target classes are imbalanced. Therefore, the evaluation results are preliminary, and predictions should be interpreted cautiously.



6\. Project Structure



Sleep-Patterns-and-Classroom-Productivity/

│

├── dataset.csv

├── data\_science\_project\_final.ipynb

├── final\_classroom\_productivity\_model.pkl

├── README.md

├── requirements.txt

├── .gitignore

│

├── plots/

├── src/

└── results/



7\. Project Files



File| Description

dataset.csv| Survey dataset containing student responses

data\_science\_project\_final.ipynb| Notebook containing preprocessing, model training and evaluation

final\_classroom\_productivity\_model.pkl| Saved final trained KNN model pipeline

requirements.txt| Required Python libraries

plots/| Directory for project visualizations

src/| Directory for source code

results/| Directory for model evaluation results



8\. Installation and Setup



Clone the repository:



git clone YOUR\_GITHUB\_REPOSITORY\_URL



Navigate to the project directory:



cd SLEEP-PATTERNS-AND-CLASSROOM-PRODUCTIVITY



Install the required dependencies:



pip install -r requirements.txt



9\. How to Run



1\. Open Google Colab or Jupyter Notebook.

2\. Open "data\_science\_project\_final.ipynb".

3\. Load the survey dataset.

4\. Execute the notebook cells sequentially.

5\. Explore the data analysis, model training and evaluation results.



10\. Limitations



\- The dataset is based on self-reported survey responses.

\- The number of responses is limited.

\- The target classes are imbalanced.

\- The model identifies patterns and does not establish cause-and-effect relationships.

\- Predictions are not intended to be treated as definitive assessments of student productivity.



11\. Team Members



Name| USN

Ananya Shetty| NN25ISE028

Ankitha Sharma| NN25ISE032

Aadi D Rai| NN25ISE002



12\. Project Guide



Dr. Vandana B S

NMAMIT, Nitte



\---



Project Domain: Machine Learning

Project Title: Sleep Patterns and Classroom Productivity Among Engineering Students

