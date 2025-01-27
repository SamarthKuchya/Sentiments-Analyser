# Sentiments Analyser

A sentiment analysis application using a custom-trained LSTM model. The app predicts whether a given text has a **Positive**, **Neutral**, or **Negative** sentiment, and provides an associated emoji as output. The embeddings are based on the GloVe word vectors.

---

## Features

- **Custom-trained LSTM model** for sentiment classification.
- Leverages **GloVe word embeddings** (50-dimensional vectors).
- Outputs sentiment predictions with emojis for a more visual representation.

---

## How It Works

1. **Pre-trained Word Embeddings:**
   - Loads GloVe 6B 50-dimensional word embeddings.
   - Maps words in the input text to their corresponding vector representations.

2. **LSTM Model Prediction:**
   - The model takes processed text embeddings as input and predicts the sentiment.

3. **Visual Output:**
   - Sentiments are categorized as:
     - **Positive 😊**
     - **Neutral 😐**
     - **Negative 😢**

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SamarthKuchya/Sentiments-Analyser.git
   cd Sentiments-Analyser
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the GloVe embeddings:
   - Download `glove.6B.50d.txt` from [GloVe official website](https://nlp.stanford.edu/projects/glove/).
   - Place the file in the root directory of the project.

4. Ensure the trained LSTM model (`model.h5`) is available in the root directory.

---

## Usage

1. Import the module and use the `predict` function:
   ```python
   from sentiment_analyser import predict
   
   result = predict("I love this app, it's amazing!")
   print(result)  # Outputs sentiment and emoji
   ```

2. Run the provided script:
   ```bash
   python sentiment_analyser.py
   ```

---

## Example

Input:
```text
Lately, doesn't sync between web app and Android reminders well. Still a nice app, but that is an inconvenience.
```

Output:
```text
["Negative 😢", "/static/img/negative.png"]
```

---

## File Structure

```plaintext
.
├── sentiment_analyser.py   # Main script for prediction
├── model.h5               # Trained LSTM model
├── glove.6B.50d.txt       # GloVe word embeddings
├── requirements.txt       # Required Python libraries
```

---

## Dependencies

- Python 3.7+
- TensorFlow/Keras
- NumPy

Install all dependencies via `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## License
This project is licensed under the MIT License.

---

## Author
[Samarth Kumar Kuchya](https://github.com/SamarthKuchya)
