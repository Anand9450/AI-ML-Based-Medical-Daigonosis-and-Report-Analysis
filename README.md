# Unified Medical Intelligence System
 
 This project combines Symptom-based Disease Prediction and MRI Brain Tumor Detection into a single unified application, enhanced with a 24/7 AI Health Assistant powered by **Google Gemini**.
 
 ## Features
 
 1.  **Disease Prediction**: Predicts potential diseases based on user-provided symptoms using a Random Forest model. Provides descriptions, precautions, medications, diets, and workout recommendations.
 2.  **MRI Analysis**: Classifies Brain MRI scans into 4 categories (Glioma, Meningioma, Pituitary Tumor, No Tumor) using a CNN model.
 3.  **AI Health Assistant**: A chatbot interface powered by the **Google Gemini** Large Language Model (LLM) for intelligent, precise, and wise medical information generation and assistance.
 
 ## Setup
 
 1.  **Install Dependencies**:
     ```bash
     pip install -r requirements.txt
     ```
 
 2.  **Configure API Key**:
     *   Create a `.env` file in the root directory.
     *   Add your Google Gemini API key:
         ```
         GEMINI_API_KEY=your_actual_api_key_here
         ```
 
 3.  **Run the Application**:
     ```bash
     python unified_app.py
     ```
 
 4.  **Access the App**:
     Open your browser and go to `http://127.0.0.1:5000`.
 
 ## Project Structure
 
 -   `unified_app.py`: The main Flask application file.
 -   `templates/`: HTML templates for the web interface.
     -   `home.html`: Landing page.
     -   `disease.html`: Disease prediction interface.
     -   `mri.html`: MRI analysis interface.
     -   `chat.html`: Chatbot interface.
 -   `model/`: Contains the `RandomForest.pkl` model.
 -   `kaggle_dataset/`: Contains CSV datasets for disease information.
 -   `tumor_detection_model.h5`: The trained Keras model for tumor detection.
