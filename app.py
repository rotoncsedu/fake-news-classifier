from preprocessing import preprocess
import joblib
import gradio as gr

def predict_news(text):
    cleaned_text = preprocess(text)
    print(f"Cleaned Text: {cleaned_text}")
    # Load the saved model
    model_path = r'models\best_model.pkl'
    model = joblib.load(model_path)
    
    # Make a prediction
    confidence = model.predict_proba([cleaned_text])[0]
    labels = model.classes_
    fake_idx = list(labels).index('Fake')
    real_idx = list(labels).index('Real')

    prediction = labels[confidence.argmax()]
    print(f"Prediction: {prediction}")
    print(f"Confidence: {confidence[fake_idx]*100:.2f}% Fake, {confidence[real_idx]*100:.2f}% Real")

    return (
        prediction,
        f"{confidence[fake_idx]*100:.2f}%",
        f"{confidence[real_idx]*100:.2f}%"
    )

pred, fake_conf, real_conf = predict_news("The economy is booming and unemployment is at an all-time low.")
# ui = gr.Interface(
#     fn=predict_news,
#     inputs=gr.Textbox(lines=4, placeholder="Enter news text here..."),
#     outputs=[
#         gr.Label(label="Prediction"),
#         gr.Textbox(label="Fake Confidence"),
#         gr.Textbox(label="Real Confidence")
#     ],
#     title="Fake News Classifier",
#     description="Enter a news article to predict whether it's real or fake."
# )

# ui.launch(share=False)

examples = [
    ["Scientists discover a new species of frog in the Amazon rainforest after a five-year research project."],
    ["Government approves a new infrastructure budget for highway development next year."],
    ["Aliens have secretly taken control of all world governments according to leaked documents."]
]

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # Fake News Classifier
        
        Paste a news article below and the model will predict
        whether the article is **Fake** or **Real**.
        """
    )

    with gr.Row():

        with gr.Column(scale=2):

            news_input = gr.Textbox(
                lines=12,
                label="News Article",
                placeholder="Paste the news article here..."
            )

            predict_btn = gr.Button("Analyze News")

        with gr.Column(scale=1):

            prediction = gr.Label(
                label="Prediction"
            )

            fake_conf = gr.Textbox(
                label="Fake Confidence"
            )

            real_conf = gr.Textbox(
                label="Real Confidence"
            )

    gr.Examples(
        examples=examples,
        inputs=news_input
    )

    predict_btn.click(
        fn=predict_news,
        inputs=news_input,
        outputs=[
            prediction,
            fake_conf,
            real_conf
        ]
    )

demo.launch()
