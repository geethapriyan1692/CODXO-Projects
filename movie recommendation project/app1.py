from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pickled objects
with open('cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

with open('indices.pkl', 'rb') as f:
    indices = pickle.load(f)

with open('titles.pkl', 'rb') as f:
    titles = pickle.load(f)

def recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form['movie_title']
    try:
        recommended_movies = recommendations(title)
        return render_template('index.html', movies=recommended_movies, movie_title=title)
    except KeyError:
        return render_template('index.html', error=f"Movie '{title}' not found in the dataset.")

if __name__ == '__main__':
    app.run(debug=True)
