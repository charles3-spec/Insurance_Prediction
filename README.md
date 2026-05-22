# Insurance Prediction 📊💡

A machine learning project that predicts insurance charges based on historical customer data using **Regression Analysis**. This project includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment of the trained model through an interactive **Streamlit web application**.

---

## 🚀 Project Overview

The goal of this project is to build a predictive system capable of estimating insurance charges using factors such as:

* Age
* Sex
* BMI
* Number of children
* Smoking status
* Region

Using regression algorithms, the model learns patterns from historical insurance datasets and predicts future insurance costs with high accuracy.

The final trained model is deployed using **Streamlit**, allowing users to interact with the prediction system through a clean and user-friendly web interface.

---

## 🛠️ Technologies Used

* **Python**
* **Jupyter Notebook**
* **Pandas**
* **Scikit-learn**
* **Streamlit**

---

## 📂 Project Structure

```bash
Insurance_Prediction/
│
├── data/
├──└── insurance.csv          # Dataset files
|
├── .gitignore                # Ignore these files
├── app.py                    # Streamlit application
├── Insurance_pipeline.ipynb  # Jupyter notebooks for analysis and training                 
├── insurance_prediction.pkl  # Saved trained models                  
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## 📈 Machine Learning Workflow

### 1. Data Collection

Historical insurance dataset containing customer demographic and health-related information.

### 2. Data Preprocessing

* Handling missing values
* Encoding categorical variables
* Feature scaling
* Data splitting

### 3. Exploratory Data Analysis (EDA)

Visualizations and statistical analysis were used to identify:

* Relationships between features
* Correlations
* Data distributions
* Outliers

### 4. Model Training

Regression algorithms were trained and evaluated to predict insurance charges.

Examples include:

* Linear Regression
* Random Forest Regressor
* Decision Tree Regressor

### 5. Model Evaluation

Performance metrics used:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### 6. Deployment

The final model was integrated into a Streamlit application for real-time predictions.

---

## 🌐 Streamlit Application

The Streamlit app allows users to:

✅ Input customer information
✅ Generate insurance charge predictions instantly
✅ Interact with the model through a simple UI

To run the Streamlit app locally:

```bash
streamlit run app.py
```

---

## ⚙️ Installation Guide

### Clone the Repository

```bash
git clone https://github.com/your-username/Insurance_Prediction.git
cd Insurance_Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📊 Example Prediction Inputs

| Feature  | Example   |
| -------- | --------- |
| Age      | 29        |
| Gender   | Male      |
| BMI      | 27.5      |
| Children | 2         |
| Smoker   | No        |
| Region   | Southeast |

---

## 🎯 Project Objectives

* Apply regression analysis to real-world insurance data
* Build an accurate predictive machine learning model
* Deploy the model as a web application
* Demonstrate end-to-end machine learning workflow

---

## 📌 Future Improvements

* Improve model accuracy using advanced algorithms
* Deploy application to cloud platforms
* Add authentication and user history
* Integrate database storage
* Enhance UI/UX design

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Saint Anumba** 🚀
