# Singapore HDB Resale Flat Price Prediction

A machine learning project that explores Singapore's HDB resale housing market and predicts resale prices based on property characteristics.

The project combines data analysis, regression modelling, interactive visualisation, and a Streamlit application to explore historical resale trends and estimate property prices.

## Project Overview

Singapore's HDB resale prices vary according to several factors, including location, flat type, floor area, storey range, flat model, and remaining lease.

This project explores historical resale transaction data and builds machine learning models to estimate resale prices from selected property attributes.

It also includes an interactive application where users can explore market trends and generate a resale price prediction.

## Project Objectives

- Explore historical HDB resale transaction data.
- Prepare and process property-related features.
- Compare multiple regression models.
- Evaluate model performance using standard regression metrics.
- Build an interactive application for resale price prediction.
- Visualise historical prices and property statistics across Singapore towns.

## Project Workflow

```text
Historical HDB Resale Data
          |
          v
Data Preparation & Processing
          |
          v
Feature Encoding
          |
          v
Regression Model Training
          |
          v
Model Evaluation
          |
          v
Saved Random Forest Model
          |
          v
Streamlit Application
          |
          +---- Price Prediction
          |
          +---- Historical Price Analysis
          |
          +---- Interactive Town Map
```

## Machine Learning

The notebook explores three regression algorithms:

- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

The models are evaluated using:

| Metric | Purpose |
|---|---|
| R² Score | Measures how well the model explains variation in resale prices |
| RMSE | Measures prediction error while penalising larger errors |
| MAE | Measures the average absolute prediction error |

The notebook includes model training, evaluation, and saving the trained Random Forest model along with the encoders used for categorical features.

*Actual evaluation scores will be included from the executed notebook results.*

## Streamlit Application

The project includes an interactive Streamlit application with two main areas.

### 1. Singapore Flat Resale Price Predictor

Users can provide property details such as:

- Transaction year
- Town
- Street name
- Flat type
- Storey range
- Flat model
- Floor area
- Remaining lease

The application processes the selected inputs using the saved encoders and Random Forest model.

After the required inputs are selected, users can generate a predicted resale price.

The application also displays a town-level map with property information, including the number of properties and average resale price available in the dataset.

### 2. Historical Price Analysis

The statistics section provides interactive analysis of the resale market.

Users can explore:

- Number of properties available in each town
- Distribution of flat types across towns
- Average resale price trends over time
- Historical price trends for selected towns
- Price comparisons by flat type
- Price comparisons by storey range
- Price comparisons by flat model
- Combined property characteristic comparisons

The visualisations use Plotly to support interactive exploration.

## Interactive Map

The prediction application uses Folium to display the selected town on a map.

The map includes town-level information such as:

- Number of properties
- Average resale price

The map is displayed after a prediction is generated.

## Technology Stack

| Area | Technologies |
|---|---|
| Programming | Python |
| Data processing | Pandas |
| Machine learning | Scikit-learn, XGBoost |
| Model persistence | Pickle |
| Application | Streamlit |
| Visualisation | Plotly, Folium |
| Map integration | Streamlit-Folium |
| Data storage | Parquet |

## Repository Contents

- **Jupyter Notebook:** Data preparation, model experiments, training, and evaluation.
- **Streamlit application:** Interactive price prediction and historical analysis.
- **Saved model:** Trained Random Forest model.
- **Encoders:** Encoded categorical features and town-to-street mapping.
- **Dataset:** Processed Singapore resale transaction data.
- **Images:** Visual assets used in the application.

## Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/SG9822/Singapore_Flat_Price_Prediction.git
cd Singapore_Flat_Price_Prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the project files

Ensure the processed dataset, trained model, and encoder files are available in the locations expected by the application.

Update any local file paths in the application before running it on another computer.

### 4. Run Streamlit

```bash
streamlit run app.py
```

Use the actual application entry-point filename if it differs from `app.py`.

## Project Learning

This project provided practical experience in:

- Preparing property transaction data for machine learning
- Working with categorical and numerical features
- Comparing regression algorithms
- Evaluating predictions using regression metrics
- Saving and loading trained models
- Building interactive Streamlit applications
- Creating interactive charts and maps
- Connecting machine learning outputs with a user-facing application

## Disclaimer

The predicted resale price is a machine learning estimate based on the available dataset and selected property attributes.

It is intended for educational and exploratory purposes and should not be treated as an official property valuation or financial advice.

## Author

**Shanmugagouthaman KR**

GitHub: [SG9822](https://github.com/SG9822)
