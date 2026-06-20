# Fake News Classifier & Deployment
## Overview
This is a Repo contains classify the News article for Real/Fake News ditection

2

## Dataset
- Features used : Text
- Target : label ( Fake / Real )
- Total samples : [ 9900 ]
## Model Comparison
| Model | Accuracy | Precision | Recall | F1 - Score |
| - - - - - - - - - - - - - - - - - - - - - - - - -| - - - - - - - - - -| - - - - - - - - - - -| - - - - - - - -| - - - - - - - - - -|
| Multinomial Naive Bayes | 0.97 | 0.97 | 0.97 | 0.97 |
| Logistic Regression | 0.99 | 0.99 | 0.99 | 0.99 |
## Final Model
** Model :** Logistic Regression
** Accuracy :** 0.990877
** Why this model ?**
Logistic Regression was selected as the final model because it achieved the best overall performance, with an Accuracy, Precision, Recall, and F1-Score of 0.99. Since it outperformed Multinomial Naive Bayes across all evaluation metrics and achieved the highest F1-Score, it was considered the most reliable model for classifying Fake and Real news articles.
## Web Application
Deployed using Gradio .
### Screenshots
![ Gradio Interface ]( screenshots\gradio_interface.png)
## Installation
git clone https://github.com/rotoncsedu/fake-news-classifier
cd fake-news-classifier
pip install -r requirements . txt
## Usage
Run the web app :
python app . py
## Project Structure

fake - news - classifier /
│
├── data/
│   └── fake_and_real_news.csv
│
├── notebooks/
│   ├── 1_eda.ipynb
│   └── 2_training.ipynb
│
├── models/
│   └── best_model.pkl
│
├── screenshots/
│   └── gradio_interface.png
│
├── app.py
├── procecssing.py
├── requirements.txt
└── README.md
## Technologies Used
- Python
- Pandas , NLTK , Matplotlib , Seaborn
- Scikit - learn
- Gradio