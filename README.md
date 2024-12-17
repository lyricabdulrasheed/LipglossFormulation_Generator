---
title: LLCResultsGenorator
emoji: 🐠
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 5.4.0
app_file: app.py
pinned: false
license: cc-by-nc-nd-4.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
Lip Gloss Formulation Predictor

Welcome to the Lip Gloss Formulation Predictor, a powerful tool designed for Lyricslip Candy LLC to optimize and experiment with lip gloss formulations. This system uses machine learning to predict key attributes of your lip gloss products, such as SPF, Viscosity, and Transparency, based on ingredient combinations and amounts.

Features

Upload Formulation Data: Upload your Excel files containing ingredient and formulation data.
Data Preprocessing: Automatically cleans and processes data, filling missing values and converting inputs for machine learning.
AI-Powered Predictions: Uses Random Forest models to predict product characteristics:
SPF: Sun Protection Factor of the formulation.
Viscosity: The thickness of the gloss.
Transparency: The clarity of the gloss.
Customizable Inputs: Experiment with ingredient combinations, amounts, and properties through an interactive interface.
Interactive Gradio UI: Easy-to-use GUI for quick predictions and results visualization.
How It Works

Upload Your Data:
Use the Upload Excel File button to upload a dataset containing your lip gloss formulation data.
The dataset should include columns like:
Oil Amount
UV Filter
Caffeine
Emulsifier
SPF, Viscosity, Transparency
Train Models:
The app trains machine learning models using the uploaded data.
Random Forest Regressors are built for predicting SPF, Viscosity, and Transparency.
Make Predictions:
Use dropdowns and numerical inputs to adjust ingredients:
Select an Oil Combination (e.g., Coconut Oil, Almond Oil).
Adjust the Oil Amount (g).
Choose UV Filter and Caffeine options.
Set the Emulsifier (g) amount.
Click the Submit button to get predictions.
Optimize Your Product:
Use the predicted values to refine and improve formulations, ensuring they meet your desired characteristics.
Prerequisites

To run the application locally or deploy it in a cloud environment like Hugging Face Spaces, ensure the following dependencies are installed:

Python 3.8 or later
Libraries:
gradio
pandas
scikit-learn
openpyxl
Install all dependencies using:

pip install gradio pandas scikit-learn openpyxl
Setup Instructions

Clone the Repository:
git clone https://github.com/lyricslip-candy/lip-gloss-predictor.git
cd lip-gloss-predictor
Run the Application:
python app.py
Access the Interface:
Open your web browser and go to http://localhost:7860.
Upload Your Data:
Use the interface to upload your Excel formulation dataset.
Experiment and Predict:
Input custom ingredient combinations to see how they affect SPF, viscosity, and transparency.
Input Data Format

Your Excel file should contain the following columns:

Oil Amount: The amount of oil used (e.g., 10g or 15.5g).
UV Filter: Description of UV-filtering agents (e.g., Zinc oxide or None).
Caffeine: Specify whether caffeine is present (e.g., present or absent).
Emulsifier: Amount of emulsifier used (e.g., 1.5).
SPF, Viscosity, Transparency: Target values for predictions (if available).
Example Use Case for Lyricslip Candy LLC

Formulation Testing:
Use the app to experiment with ingredient amounts and types.
Predict how new formulations will perform without needing lab testing.
Product Optimization:
Adjust oil amounts, UV filters, and other components to meet your desired SPF, viscosity, and transparency specifications.
Innovative Products:
Use insights to design innovative lip glosses that stand out in the market.
Business Benefits

Cost Efficiency: Reduce trial-and-error costs by predicting outcomes virtually.
Faster Development: Quickly iterate on new formulations and refine products.
Data-Driven Decisions: Leverage historical data to make informed formulation choices.
Customer Satisfaction: Deliver products with consistent quality and performance.
Support

Powered by AI to help Lyricslip Candy LLC deliver the perfect lip gloss every time!

Dataset Information: The dataset used in this app was a randomly generated dataset provided by ChatGPT, which served as a placeholder for testing purposes. It is designed to be replaced with actual research data once collected. I personally created the dataset titles to align with my research variables, ensuring that the app framework could later accommodate real-world data once it becomes available.

For more information about the dataset, including ethical considerations and data handling, please refer to the Ethics Data Card and the DEON Checklist.

