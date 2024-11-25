import gradio as gr

# Deon checklist for Lip Gloss Formulation Generator Model (in markdown)
deon_checklist_md = """
# Deon Checklist for Lip Gloss Formulation Generator Model

## 1. Data Collection

### Input Variables:
- **Oil Combination**: A combination of oils used in the formulation (e.g., jojoba oil, coconut oil).
- **Oil Amount (g)**: The weight of oil used in the formulation.
- **UV Filter (Zinc oxide)**: The presence of Zinc oxide as a UV filter in the formulation.
- **Caffeine (presence)**: Whether caffeine is included in the formulation.
- **Emulsifier**: Type and amount of emulsifier used (e.g., lecithin, beeswax).

### Output Variables:
- **SPF**: Sun Protection Factor predicted for the lip gloss.
- **Viscosity**: Thickness or flow resistance of the formulation.
- **Transparency**: The visual clarity of the formulation.

### Data Source:
The dataset used for training the model was initially generated using ChatGPT by creating random values for cosmetic ingredients, including oil combinations, emulsifiers, and properties such as SPF, viscosity, and transparency. This synthetic dataset was used solely in the prototype phase to develop the Lip Gloss Formulation Generator model. The dataset is considered a placeholder for testing and prototyping. Once real-world experimental data is available, this synthetic data will be replaced to improve the model's predictions and its real-world applicability.

### Data Validation:
The dataset, uploaded by the user in the form of an Excel file, has been processed to extract relevant features and fill missing values. However, it is crucial to verify the data's quality and completeness through domain experts in the cosmetic industry to ensure the model's predictions are reliable.

### Sensitive Data:
The dataset is related to cosmetic formulations and does not contain sensitive personal information. However, care should be taken to ensure that any uploaded datasets do not inadvertently include proprietary or sensitive data without the necessary consent.

## 2. Fairness & Justice

### Inclusion of Diverse Preferences:
- How will you ensure the model’s predictions are fair and inclusive of diverse preferences (e.g., different skin tones, textures, or cultural preferences)?
  - The model will aim to incorporate diverse data types, considering various oils, emulsifiers, and other ingredients used in cosmetics. Future updates should strive to include datasets representing a variety of skin tones, textures, and cultural preferences, ensuring the model serves a broad user base.

### Biases in Data:
- Are there biases in the dataset (e.g., overrepresentation of certain ingredients or preferences)?
  - Since the dataset was randomly generated for testing purposes, there may be an overrepresentation of certain ingredients or combinations that are not reflective of actual consumer preferences. Efforts should be made to diversify future datasets by including a wider range of ingredients and formulations that cater to different skin types and cultural needs.

### Skin Sensitivities & Allergies:
- How will you ensure the model does not disproportionately recommend formulations that may not be suitable for certain skin types or allergies?
  - The model should consider common allergens or skin sensitivities when recommending formulations. Future iterations should incorporate warnings or suggestions based on known allergens and ensure that sensitive skin types are taken into account when recommending certain oils, emulsifiers, or other ingredients.

## 3. Transparency

### Data Source Transparency:
- How will you ensure transparency about the data sources and the formulation process of the model?
  - Users will be informed that the dataset used for training the model in its initial stage was randomly generated and may not fully represent real-world data. Clear communication about the prototype nature of the dataset will be included in the app's interface and documentation.

### Model Limitations:
- What information will be made available to users about the model’s capabilities and limitations?
  - Users will be made aware that the model's predictions are based on a synthetic dataset, and the results should be taken with caution. We will include clear disclaimers about the model's limitations and the fact that the predictions (e.g., SPF, Viscosity, Transparency) are based on prototype data and not real-world formulations.

### Communicating Limitations to Decision-Makers:
- How will you communicate the model’s predictions and limitations to decision-makers?
  - Decision-makers will be explicitly informed of the model's current limitations. They will be encouraged to use the app's predictions as a starting point but will be advised to conduct real-world testing to verify the formulations before use. This will be communicated in both the app interface and any accompanying documentation.

## 4. Privacy

### User Data Privacy:
- How will you ensure the privacy of users, especially regarding their personal data, preferences, and beauty profiles?
  - User-uploaded data will be handled securely, anonymized, and not stored beyond the duration of the current session. Any personal data shared, such as custom formulations or preferences, will be treated with the utmost privacy and will not be retained without explicit consent from the user.

### Misuse of Personal Data:
- What steps will you take to prevent the misuse of this data, especially in terms of tracking personal beauty habits?
  - The app will not track any personally identifiable information unless the user explicitly opts into a feature that requires storing personal data. The user will have full control over what data is shared and how it is used, with clear privacy policies in place to protect their data.

### Third-Party Data:
- If external data sources (e.g., third-party databases) are integrated, how will you balance accuracy with protecting user privacy?
  - Any external data sources used in future updates will be anonymized and aggregated to avoid tracking individual users. External data will be carefully evaluated for privacy compliance and transparency to ensure it does not inadvertently breach user confidentiality.

## 5. Accountability

### Accountability for Harmful Formulations:
- Who will be held accountable if the model generates harmful or unsafe lip gloss formulations?
  - The developers and relevant regulatory bodies will be responsible for ensuring that the model does not generate harmful or unsafe formulations. There should also be a system in place for users to provide feedback and report unsafe or inaccurate predictions, which can be promptly addressed.

### Monitoring & Adjusting the Model:
- What system will you establish to monitor and adjust the model over time to ensure it stays safe and relevant?
  - A feedback mechanism will be established within the app, allowing users to report any issues or inaccuracies with the model's predictions. Regular updates and reviews of the model will be conducted to ensure it reflects the latest scientific research and safety standards in the cosmetic industry.

## 6. Inclusivity

### Diverse Data Representation:
- How will you ensure that the model includes diverse data from different demographic groups and skin types?
  - Future iterations of the model will ensure the inclusion of a diverse set of formulations and ingredients that cater to various skin types, tones, and cultural needs. Collaboration with dermatologists and cosmetic scientists from different demographic backgrounds will be key to improving inclusivity.

### Addressing Vulnerable Populations:
- How will you ensure that the model accounts for the needs of different communities, including vulnerable populations (e.g., people with skin sensitivities or allergies)?
  - The model will incorporate features that allow users to select formulations based on specific skin sensitivities or allergies. Known allergens will be flagged, and suggestions will be tailored to meet the needs of individuals with different skin types or sensitivities.

## 7. Sustainability

### Sustainability in Ingredient Sourcing:
- How will the model’s recommendations affect sustainability in terms of ingredient sourcing and packaging?
  - The model will prioritize sustainable ingredients, such as plant-based oils, and recommend packaging solutions that are eco-friendly, recyclable, or biodegradable. Sustainability will be a core factor in future updates to ensure the model aligns with environmental best practices.

### Long-Term Sustainability:
- How will you ensure the model remains sustainable, considering the evolving nature of climate change and its effects on ingredient availability?
  - The model will be regularly updated to reflect the latest developments in sustainable ingredient sourcing, taking into account the impacts of climate change and the availability of natural resources. It will also stay informed of the latest environmental standards within the cosmetic industry to ensure continued sustainability.

### Broader Implications:
- What are the broader social and environmental implications if this model becomes widely adopted?
  - The model has the potential to encourage more eco-conscious and sustainable formulations by recommending ingredients and packaging that reduce environmental impact. However, it is essential to monitor the broader social and environmental implications, ensuring that the widespread adoption of the model leads to positive outcomes, such as reducing waste and promoting environmentally friendly practices in the beauty industry.
"""

# Function to display the Deon checklist
def display_deon_checklist():
    return deon_checklist_md

# Gradio interface to display the Deon checklist
iface = gr.Interface(fn=display_deon_checklist, inputs=[], outputs="markdown", title="Deon Checklist for Lip Gloss Formulation Generator")

# Launch the Gradio interface
iface.launch()
