import pandas as pd
import gradio as gr
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Upload and preprocess dataset
def preprocess_file(file):
    data = pd.read_excel(file.name)
    data.columns = data.columns.str.strip()

    data['Oil Amount (g)'] = pd.to_numeric(data['Oil Amount'].str.extract(r'(\d+\.?\d*)')[0], errors='coerce')
    data['UV Filter Binary'] = data['UV Filter'].apply(lambda x: 1 if "Zinc oxide" in str(x) else 0)
    data['Caffeine Binary'] = data['Caffeine'].apply(lambda x: 1 if "present" in str(x).lower() else 0)

    data.fillna(data.median(numeric_only=True), inplace=True)

    oil_combinations = data['Oil Combination'].dropna().unique().tolist()
    uv_filter_options = ["Zinc oxide", "No zinc oxide"]
    caffeine_options = ["Caffeine present", "No caffeine"]

    return data, oil_combinations, uv_filter_options, caffeine_options

# Train models
def train_models(data):
    features = ['Oil Amount (g)', 'UV Filter Binary', 'Caffeine Binary', 'Emulsifier']
    targets = ['SPF', 'Viscosity', 'Transparency']
    best_models = {}

    for target in targets:
        X = data[features]
        y = data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        print(f"{target} model R^2: {r2:.2f}")
        best_models[target] = model

    return best_models

# Prediction function
def predict(oil_combination, oil_amount, uv_filter, caffeine, emulsifier, file):
    data, oil_combinations, uv_filter_options, caffeine_options = preprocess_file(file)
    models = train_models(data)
    
    oil_amount = float(oil_amount)
    uv_filter_binary = 1 if uv_filter == "Zinc oxide" else 0
    caffeine_binary = 1 if caffeine == "Caffeine present" else 0
    emulsifier = float(emulsifier)

    input_data = pd.DataFrame({
        "Oil Amount (g)": [oil_amount],
        "UV Filter Binary": [uv_filter_binary],
        "Caffeine Binary": [caffeine_binary],
        "Emulsifier": [emulsifier],
    })

    results = {}
    for target, model in models.items():
        results[target] = model.predict(input_data)[0]

    return round(results["SPF"], 2), round(results["Viscosity"], 2), round(results["Transparency"], 2)

# Gradio interface
file_input = gr.File(label="Upload Excel File")
inputs = [
    file_input,
    gr.Textbox(label="Oil Combination", value="Coconut Oil"),
    gr.Number(label="Oil Amount (g)", value=10),
    gr.Dropdown(["Zinc oxide", "No zinc oxide"], label="UV Filter"),
    gr.Dropdown(["Caffeine present", "No caffeine"], label="Caffeine"),
    gr.Number(label="Emulsifier (g)", value=1.5),
]
outputs = [
    gr.Textbox(label="Predicted SPF"),
    gr.Textbox(label="Predicted Viscosity"),
    gr.Textbox(label="Predicted Transparency"),
]

iface = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs=outputs,
    title="Lip Gloss Predictor"
)

iface.launch()
