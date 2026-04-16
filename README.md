# 🎬 Movie Recommendation System (Hybrid)

A Machine Learning-based Movie Recommendation System that suggests
movies using a **hybrid approach** combining:

-   🎯 Content-Based Filtering\
-   🤝 Collaborative Filtering (SVD)

Built with **Python, Pandas, Scikit-learn, Surprise**, and deployed
using **Streamlit**.

------------------------------------------------------------------------

## 🚀 Features

-   Hybrid recommendation system (Content + SVD)
-   Interactive UI using Streamlit
-   Fast recommendations using pre-trained models
-   Scalable and modular structure

------------------------------------------------------------------------

## 🧠 How It Works

### 1. Content-Based Filtering

-   Uses movie metadata (genres, keywords, etc.)
-   Computes similarity using cosine similarity

### 2. Collaborative Filtering (SVD)

-   Uses user-item interaction (ratings dataset)
-   Predicts user preferences using matrix factorization

### 3. Hybrid Model

Final recommendation score:

Final Score = 0.6 × Content Score + 0.4 × SVD Score

------------------------------------------------------------------------

## 📁 Project Structure

MovieRecc/ │ ├── app.py ├── movies.csv ├── ratings.csv ├──
cosine_sim.pkl ├── svd_model.pkl ├── MovieRecc.ipynb └── README.md

------------------------------------------------------------------------

## ⚙️ Installation

git clone https://github.com/your-username/movie-recommender.git\
cd movie-recommender

pip install -r requirements.txt

------------------------------------------------------------------------

## ▶️ Running the App
Activate virtual environment:
venv\Scripts\activate

Run the project:
streamlit run app.py

Open: http://localhost:8501

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python\
-   Pandas & NumPy\
-   Scikit-learn\
-   Surprise (SVD)\
-   Streamlit

------------------------------------------------------------------------

## 👨‍💻 Author

Shivam Sharma
