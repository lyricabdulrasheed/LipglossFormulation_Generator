import gradio as gr

# Ethics DataCard content for Lip Gloss Formulation Model
datacard_content = """
# Ethics DataCard for Lip Gloss Formulation Model

## Dataset Overview
**Input Variables**: Oil Combination, Oil Amount (g), UV Filter (Zinc oxide), Caffeine (Presence), Emulsifier (Type and Amount).
**Output Variables**: SPF (Sun Protection Factor), Viscosity, Transparency.

## Data Collection Process
- **Sourcing**: The dataset used to train this model was randomly generated using ChatGPT for initial prototype purposes. The data includes a variety of synthetic cosmetic formulations, including oils, emulsifiers, and UV filters. 
- **Privacy**: The dataset does not contain personal information and is based on simulated data. Once real experimental data is collected, it will replace the synthetic data used for training.
- **Data Integrity**: The data used was not validated or curated in real-world experiments and is intended as a proof of concept. Domain experts in cosmetics should evaluate the accuracy of predictions before use.

## Bias Considerations
- **Potential Bias**: The synthetic dataset may over-represent certain ingredients or formulations that are popular or commonly used in the training process. As the data is generated randomly, it may not capture the full diversity of user preferences or ingredients used in the cosmetic industry.
- **Mitigation**: Future versions of the model will focus on more diverse, real-world data from multiple sources, including consumer surveys, dermatological studies, and industry-wide ingredient usage.

## Fairness & Justice
- The model does not take into account cultural preferences, skin tone, or sensitivities to certain ingredients (e.g., allergens). 
- **Model Inclusivity**: The model will be enhanced in future iterations to consider formulations for different skin types, including oily, dry, sensitive, and normal skin.
- **Bias Reduction**: Steps will be taken to ensure that no specific demographic or skin type is unfairly overrepresented or underrepresented.

## Privacy and Security
- **User Data**: Any user-uploaded data (such as ingredient combinations) is handled with confidentiality and not stored beyond the session unless explicitly requested and consented to by the user.
- **Data Usage**: The model does not collect any personal, identifiable information unless explicitly stated by the user. Users are encouraged to review and consent to privacy policies before uploading data.

## Sustainability and Environmental Impact
- **Sustainable Formulations**: The model encourages using plant-based and eco-friendly ingredients when suggesting formulations, especially focusing on oils and emulsifiers that are biodegradable and non-toxic.
- **Environmental Responsibility**: Future versions will include considerations for sustainable sourcing of ingredients, taking into account environmental impact and reducing the carbon footprint of cosmetic products.

## Model Limitations
- **Accuracy**: The model predictions (SPF, Viscosity, and Transparency) are based on synthetic data and may not reflect real-world outcomes. Further validation and testing are needed before these predictions can be used for actual product formulations.
- **Generalization**: The model may not perform well in regions where the dataset does not cover local preferences or formulations used in different climates, skin types, or cultural settings.

## Accountability and Transparency
- **Model Monitoring**: The development team will monitor the performance of the model over time, incorporating user feedback and real-world data to improve accuracy and reliability.
- **Transparency**: A clear disclaimer is included, highlighting that the model's predictions are based on prototype data, which will be replaced with validated, real-world data in future updates.

## Societal Impact
- **Cosmetic Industry**: This model has the potential to revolutionize the cosmetic industry by suggesting safer, more effective formulations. However, it is important to note that the model should not be solely relied upon for safety, and the final formulations should undergo rigorous testing before market release.
- **Environmental Impact**: By recommending sustainable ingredients, the model contributes to reducing environmental harm caused by harmful chemicals and non-biodegradable packaging commonly found in cosmetic products.
"""

# Function to display the DataCard
def display_datacard():
    return datacard_content

# Gradio interface to display the ethics DataCard
iface = gr.Interface(fn=display_datacard, inputs=[], outputs="markdown", title="Lip Gloss Formulation Ethics DataCard")

# Launch the Gradio interface
iface.launch()
