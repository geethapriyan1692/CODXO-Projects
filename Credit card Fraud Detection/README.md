## Credit Card Fraud Detection
## Project Overview
This project aims to detect fraudulent credit card transactions using machine learning techniques. Given the highly imbalanced nature of the dataset, the focus is on building models that can accurately identify fraud cases while minimizing false positives and negatives.

## Technologies Used
Python
Scikit-learn
Pandas
NumPy
Matplotlib/Seaborn for data visualization
SMOTE (Synthetic Minority Over-sampling Technique) for handling class imbalance
## Dataset
The dataset contains transactions made by European cardholders in September 2013.
It includes 31 features, with V1-V28 being the principal components obtained via PCA. The only columns which have not been transformed with PCA are Time, Amount, and Class (target variable).
## Key Features
## Exploratory Data Analysis (EDA): Understanding the distribution of fraudulent vs. non-fraudulent transactions.
## Data Preprocessing: Handling missing values, feature scaling, and addressing the class imbalance using SMOTE.
## Modeling: Building machine learning models like Logistic Regression, Decision Trees, Random Forests, and XGBoost to classify transactions.
## Evaluation Metrics: Using confusion matrix, precision, recall, F1-score, and AUC-ROC curve to evaluate model performance.
## How to Run
Clone the repository:




## Dataset: Download the dataset from Kaggle and place it in the data/ folder.

## Project Structure

│
├── data/                           # Contains the dataset
├── credit_card_fraud_detection.ipynb # Jupyter notebook with the code
├── requirements.txt                # List of dependencies
└── README.md                       # Project documentation

## Results
The best-performing model in terms of fraud detection was theDecision Tree classifier, with an AUC-ROC score of 0.98 and a balanced precision-recall trade-off. The implementation of SMOTE significantly improved recall rates.

## Future Improvements
Implementing more advanced models such as deep learning using LSTM or Autoencoders for anomaly detection.
Optimizing model hyperparameters using techniques like GridSearchCV.
Exploring more sophisticated techniques for handling class imbalance.
## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

Let me know if you'd like any adjustments!
