# Fake News Classifier & Deployment
## Overview
This is a Repo contains classify the News article for Real/Fake News ditection

## Dataset
- Features used : Text
- Target : label ( Fake / Real )
- Total samples : [ 9900 ]
## Model Comparison
| Model | Accuracy | Precision | Recall | F1-Score |
|---------|----------|-----------|--------|----------|
| Multinomial Naive Bayes | 0.97 | 0.97 | 0.97 | 0.97 |
| Logistic Regression | 0.99 | 0.99 | 0.99 | 0.99 |

## Final Model

**Model:** Logistic Regression  
**Accuracy:** 99.09%

### Why this model?

Logistic Regression was selected as the final model because it achieved the best overall performance among the evaluated models. It obtained an accuracy of **99.09%** and outperformed Multinomial Naive Bayes across all evaluation metrics, including Precision, Recall, and F1-Score. Since it achieved the highest F1-Score, indicating the best balance between Precision and Recall, it was considered the most reliable model for classifying Fake and Real news articles.
## Web Application
Deployed using Gradio .
### Screenshots
![Gradio Interface](screenshots/gradio_interface.png)
## Installation
git clone https://github.com/rotoncsedu/fake-news-classifier <br>
cd fake-news-classifier<br>
pip install -r requirements . txt<br>
## Usage
Run the web app :<br>
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

## 👨‍💻 Author

Md. Al-Imran Roton

Programmer, Begum Rokeya University, Rangpur

Machine Learning & AI Enthusiast