# 🎵 Music Recommendation System

## 📌 Overview

This project is a **Music Recommendation System** that suggests songs based on user preferences using machine learning techniques. It analyzes song features such as artist, genre, and other metadata to recommend similar songs.

The system is built with a simple web interface to make interaction easy and user-friendly.

---

## 🚀 Features

* 🎧 Personalized song recommendations
* 🤖 Machine Learning-based similarity model
* 🌐 Web interface using Flask
* ⚡ Fast and efficient performance
* 📊 Data processing using Pandas

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Frontend:** HTML, CSS

---

## 📁 Project Structure

```
Music-Recommendation/
│── app.py                # Main application
│── train.py              # Model training
│── camera.py             # Camera integration (optional)
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
│
├── static/
│   └── css/style.css     # Styling
│
├── templates/
│   └── index.html        # Frontend UI
```

---

## ⚙️ Installation

### 1. Clone Repository

```
git clone https://github.com/Medhari-Sharanya/Stock-price-prediction.git
cd Music-Recommendation
```

### 2. Create Virtual Environment

```
python -m venv venv
```

### 3. Activate Environment

**Windows:**

```
venv\Scripts\activate
```

### 4. Install Requirements

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
python app.py
```

Then open:

```
http://127.0.0.1:5000/
```

---

## 🧠 Working Principle

1. Load dataset of songs
2. Extract features (artist, genre, etc.)
3. Convert text data into numerical vectors
4. Apply **Cosine Similarity**
5. Recommend top similar songs

---

## 📸 Output

* User enters/selects a song
* System recommends similar songs instantly

---

## 📈 Future Enhancements

* 🔐 User authentication system
* 🎵 Integration with Spotify API
* 📱 Responsive mobile UI
* ☁️ Deployment on cloud

---

## 👨‍💻 Author

**Medhari Sharanya**

---

## 📜 License

This project is open-source and available under the MIT License.
