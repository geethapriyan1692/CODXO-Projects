## Fake News Detection
## Project Overview
This project focuses on building a machine learning model to classify news articles as either "fake" or "real." By analyzing various features of news articles, the project aims to help in detecting misinformation and improving the credibility of information sources.

## Technologies Used
Python
Scikit-learn
Pandas
NumPy
NLTK for natural language processing
Matplotlib/Seaborn for data visualization
## Dataset
The dataset consists of labeled news articles categorized as real or fake.
Features include the title, text, author, and publication date of the news articles.
## Key Features
Exploratory Data Analysis (EDA): Visualizing word distributions and other key patterns between fake and real news.
Text Preprocessing: Tokenization, removal of stop words, stemming/lemmatization, and vectorization (using TF-IDF).
Modeling: Using algorithms like Logistic Regression, Naive Bayes, and Support Vector Machines (SVM) for classification.
Evaluation Metrics: Assessing model performance using accuracy, precision, recall, F1-score, and confusion matrix.
## How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/geethapriyan1692/fake-news-detection.git
Install dependencies: Navigate to the cloned directory and install the required libraries:

bash
Copy code
pip install -r requirements.txt
Run the Jupyter Notebook: Open the fake_news_detection.ipynb file in Jupyter Notebook and follow the steps to preprocess the data, build models, and evaluate results.

## Dataset: The dataset used can be obtained from sources like Kaggle and should be placed in the data/ directory.

## Project Structure
bash
Copy code
fake-news-detection/
│
├── data/                          # Folder for datasets
├── fake_news_detection.ipynb       # Jupyter notebook with the code
├── requirements.txt               # List of dependencies
└── README.md                      # Project documentation
## Results
The Decision tree  performed best in this project, achieving an accuracy of 99%. The TF-IDF vectorizer helped in capturing important features of the text data, significantly improving model performance.

Future Improvements
Exploring deep learning techniques such as LSTM or transformers (BERT) for more accurate text classification.
Implementing better feature selection techniques for more efficient model training.
Collecting larger and more diverse datasets to improve model generalization.
Contributing
Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository and submit a pull request.
