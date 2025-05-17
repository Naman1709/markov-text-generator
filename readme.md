# Markov Chain Text Generator

This is a simple web application that generates text using a Markov chain model trained on Shakespeare's works.

Built using **Flask** (Python web framework) and **Bootstrap** (for styling), the app allows users to:

- Choose the `n`-gram size for the Markov chain.
- Enter a seed phrase.
- Set how many words to generate.
- View dynamically generated text based on Shakespearean data.

---

## 🧠 How It Works

The app uses a basic Markov chain logic:

1. It reads in Shakespeare's text from a `.txt` file.
2. It trains a Markov model of order `n` (configurable).
3. It generates new sequences of words by walking randomly through the chain, starting from the given seed.

---

## 🔧 Features

- Adjustable `n`-gram size (`n`)
- User-provided seed text
- Custom word count
- Basic model caching to avoid retraining if `n` is unchanged
- Styled UI with Bootstrap

---

## 📦 Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/Naman1709/markov-text-generator.git
   cd markov-text-generator
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app:**

   ```bash
   python app.py
   ```

4. Open your browser and visit:  
   `http://127.0.0.1:5000/`
