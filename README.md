# 🇸🇬 Singapore Flat Resale Price Prediction

A machine learning project that explores Singapore's HDB resale housing market and predicts resale prices based on property attributes.

This project combines **data preprocessing, exploratory data analysis, machine learning, and an interactive Streamlit application** to help users explore historical resale prices and estimate the price of a flat using its characteristics.

## 📌 Project Overview

The Singapore HDB resale market contains transactions with different property types, locations, floor areas, and remaining lease periods.

The objective of this project is to analyze historical resale transactions, identify pricing patterns, compare machine learning models, and build an interactive application where users can explore market statistics and predict resale prices.

The project includes:

- Historical resale price analysis
- Exploratory data visualization
- Data preprocessing and categorical encoding
- Machine learning model comparison
- Random Forest resale price prediction
- Interactive Streamlit application
- Singapore town-level map visualization

## 🎯 Project Objectives

- Explore historical Singapore HDB resale transaction data.
- Understand resale price patterns across towns and flat characteristics.
- Prepare and transform data for machine learning.
- Compare Decision Tree, Random Forest, and XGBoost regression models.
- Select a suitable model based on evaluation metrics.
- Build an interactive application for property exploration and price prediction.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Data Storage | Parquet |
| Machine Learning | Scikit-learn, XGBoost |
| Model Evaluation | R², RMSE, MAE |
| Visualization | Plotly |
| Interactive Application | Streamlit |
| Maps | Folium, Streamlit-Folium |
| Image Processing | Pillow |
| Categorical Encoding | Scikit-learn Label Encoding |
| Model Persistence | Pickle |

## 📂 Project Structure

```text
Singapore_Flat_Price_Prediction/
│
├── README.md
│
├── mainscreen.py
├── home.py
├── stats.py
├── predictor.py
│
├── Singapore_Data.xlsx
├── singapore_data.parquet
│
├── encoders.pkl
├── random_forest_model.pkl
│
├── Singapore_1.jpg
├── Singapore_2.jpg
├── Singapore_3.jpg
│
└── Singapore Resale Flat Prices Predicting.ipynb
```

### File Description

| File | Description |
|---|---|
| `mainscreen.py` | Main Streamlit application entry point. Provides navigation between Home, Stats, and Price Predictor. |
| `home.py` | Displays the project introduction, Singapore images, and application overview. |
| `stats.py` | Provides interactive resale price analysis, town-level statistics, and feature comparisons. |
| `predictor.py` | Collects user inputs, loads the trained model and encoders, predicts resale prices, and displays location information. |
| `Singapore_Data.xlsx` | Source dataset used for the project. |
| `singapore_data.parquet` | Processed dataset used by the Streamlit application. |
| `encoders.pkl` | Saved categorical encoders and town-to-street mapping required by the prediction application. |
| `random_forest_model.pkl` | Trained Random Forest regression model used for price prediction. |
| `Singapore_1.jpg` | Singapore image displayed in the Home section. |
| `Singapore_2.jpg` | Singapore image displayed in the Home section. |
| `Singapore_3.jpg` | Singapore image displayed in the Home section. |
| `Singapore Resale Flat Prices Predicting.ipynb` | Jupyter Notebook containing data exploration, preprocessing, model training, evaluation, and prediction experiments. |

> **Note:** The structure above represents the recommended clean application layout. Include the files only if they are present in your final repository. The large trained model file may need to be downloaded separately if it is not committed to GitHub.

## Model File

The trained Random Forest model is used by the Streamlit application to generate resale price predictions.

Due to the large size of the serialized model file, approximately 800 MB, it is not included directly in this GitHub repository.

The model was trained as part of the Jupyter Notebook workflow.

To run the prediction application, the trained model file and the required encoder files must be available locally in the project directory.

The application cannot generate predictions without the trained model file.


## 📊 Dataset

The project uses Singapore HDB resale transaction data.

The dataset contains property information such as:

- Transaction year
- Town
- Street name
- Flat type
- Storey range
- Floor area
- Remaining lease
- Flat model
- Resale price

The data is prepared and transformed into a format suitable for analysis and machine learning.

The processed dataset is stored in Parquet format for use in the Streamlit application.

## 🔍 Exploratory Data Analysis

The project explores resale transactions through different property attributes.

The analysis includes:

- Number of properties available across towns
- Distribution of flat types across towns
- Average resale price trends over the years
- Town-level resale price comparisons
- Price comparisons by flat type
- Price comparisons by storey range
- Price comparisons by flat model
- Combined feature analysis

Interactive visualizations are created using Plotly.

## 🤖 Machine Learning

Three regression models were evaluated:

1. Decision Tree Regressor
2. Random Forest Regressor
3. XGBoost Regressor

The models were evaluated using:

- **R²** — measures how well the model explains variation in resale prices.
- **RMSE** — measures prediction error while giving greater weight to larger errors.
- **MAE** — measures the average absolute prediction error.

### Model Evaluation Results

The following results were obtained from the project notebook:

| Model | R² | RMSE | MAE |
|---|---:|---:|---:|
| Decision Tree | 0.969677 | 31,497.64 | 20,577.27 |
| Random Forest | **0.979403** | **25,959.31** | **17,717.28** |
| XGBoost | 0.962046 | 35,238.64 | 24,365.53 |

Based on the evaluation results, **Random Forest achieved the highest R² and the lowest RMSE and MAE among the three evaluated models.**

Therefore, Random Forest was selected for the interactive price prediction application.

The final Random Forest model was trained using 20 estimators and a random state of 42.

## 🏘️ Streamlit Application

The project includes an interactive Streamlit application with three main sections.

### 1. Home

The Home section introduces the project and explains its purpose.

It includes:

- Project overview
- Singapore images
- Project objectives
- Application features
- Instructions for using the predictor

### 2. Statistics

The Statistics section allows users to explore historical resale transaction data.

Users can:

- View the number of properties available across towns.
- Explore flat type distributions.
- Select a town.
- View average resale prices over the years.
- Compare resale prices by flat type.
- Analyze storey range and flat model.
- Explore combinations of property characteristics.

### 3. Price Predictor

The Price Predictor section allows users to estimate a resale flat's price using property information.

Users can enter:

- Transaction year
- Floor area
- Remaining lease
- Town
- Street name
- Flat type
- Storey range
- Flat model

The application encodes the categorical inputs using the saved encoders and passes the prepared input to the trained Random Forest model.

The predicted resale price is displayed in the application.

The predictor also displays location information using an interactive Singapore map.

## 🗺️ Interactive Map

The application uses Folium and Streamlit-Folium to display Singapore town locations.

The map provides location context for the selected property and displays relevant town-level information.

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SG9822/Singapore_Flat_Price_Prediction.git
```

```bash
cd Singapore_Flat_Price_Prediction
```

### 2. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn xgboost plotly folium streamlit-folium streamlit-option-menu pillow pyarrow
```

### 3. Verify Required Files

Ensure the application files and required assets are available:

```text
mainscreen.py
home.py
stats.py
predictor.py
singapore_data.parquet
encoders.pkl
random_forest_model.pkl
Singapore_1.jpg
Singapore_2.jpg
Singapore_3.jpg
```

The application requires the processed dataset, saved encoders, trained model, and image files to be accessible.

### 4. Run the Streamlit Application

```bash
streamlit run mainscreen.py
```

The application will open in your browser.

## 💡 Example Prediction

The notebook includes an example input with the following encoded property attributes:

```python
user_input = [[2015, 80, 30, 12, 3, 5, 7, 2]]
```

The example prediction from the notebook was:

```text
Predicted resale price: 637200
```

This is an example output from the notebook, not a guarantee of the price of an actual property.

## 📈 Key Learnings

Through this project, I explored:

- Preparing housing transaction data for analysis.
- Handling categorical variables for machine learning.
- Comparing regression models using multiple evaluation metrics.
- Understanding the importance of model selection.
- Building interactive analytical applications using Streamlit.
- Connecting machine learning predictions with user inputs.
- Presenting data insights through charts and maps.

## 🔮 Future Improvements

Potential improvements include:

- Deploying the Streamlit application publicly.
- Improving the application layout and user experience.
- Refining the model through further experimentation.
- Improving data and model loading workflows.
- Adding additional property comparisons and analytical views.
- Making the application easier to run across different environments.

## 👨‍💻 Author

**Shanmugagouthaman KR**

GitHub: [SG9822](https://github.com/SG9822)

---

*This project was developed as an individual academic project to explore data analytics, machine learning, and interactive application development using Singapore HDB resale transaction data.*
