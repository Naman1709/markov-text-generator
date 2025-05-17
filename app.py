from flask import Flask, render_template, request
from markov import MarkovChainTextGenerator

app = Flask(__name__)

# Global cache
model_cache = {
    "n": None,
    "generator": None
}

@app.route("/", methods=["GET", "POST"])
def generate():
    generated_text = ""
    seed = ""
    n = 3  # Default
    num_words = 50  # Default
    if request.method == "POST":
        seed = request.form["seed"]
        num_words = int(request.form["num_words"])
        n = int(request.form["n_value"])

        # Only retrain if n changed
        if model_cache["n"] != n:
            with open("shakespeare.txt", "r", encoding="utf-8") as f:
                text = f.read()

            generator = MarkovChainTextGenerator(n=n)
            generator.train(text)

            # Update cache
            model_cache["n"] = n
            model_cache["generator"] = generator
        else:
            generator = model_cache["generator"]

        generated_text = generator.generate_text(seed, num_words)

    return render_template("index.html", generated_text=generated_text, seed=seed, n_value=n, num_words=num_words)


if __name__ == "__main__":
    app.run(debug=True)