# Deployment Guide

This guide explains how to deploy the Unified Medical Intelligence System.

## Prerequisites

1.  **GitHub Account**: You need to push your code to a GitHub repository.
2.  **Cloud Platform Account**: We recommend **Render** (easiest/free tier) or **Heroku**.

## Option 1: Deploy on Render (Recommended)

1.  **Push Code to GitHub**:
    *   Initialize git if you haven't: `git init`
    *   Add files: `git add .`
    *   Commit: `git commit -m "Initial commit"`
    *   Create a repo on GitHub and push your code.
    *   **Important**: Your model file `tumor_detection_model.h5` is large (~128MB). GitHub has a 100MB limit. You need to use **Git LFS** (Large File Storage) or exclude it and download it during build (advanced).
        *   **Easy Fix**: If you can't use Git LFS, try to compress the model or use a cloud storage link to download it in the code.
        *   **Git LFS Setup**:
            ```bash
            git lfs install
            git lfs track "*.h5"
            git add .gitattributes
            git commit -m "Add model with LFS"
            ```

2.  **Create Web Service on Render**:
    *   Go to [dashboard.render.com](https://dashboard.render.com/).
    *   Click **New +** -> **Web Service**.
    *   Connect your GitHub repository.
    *   **Runtime**: Python 3
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `gunicorn unified_app:app`
    *   **Environment Variables**:
        *   Add `GEMINI_API_KEY` with your actual API key.
        *   Add `PYTHON_VERSION` set to `3.9.18` (or similar) if needed.

3.  **Deploy**: Click "Create Web Service". Render will build and deploy your app.

## Option 2: Deploy with Docker

If you prefer using Docker or want to deploy on a VPS (like DigitalOcean, AWS EC2):

1.  **Build the Image**:
    ```bash
    docker build -t medical-app .
    ```

2.  **Run the Container**:
    ```bash
    docker run -p 5000:5000 -e GEMINI_API_KEY=your_key_here medical-app
    ```

## Important Notes

*   **Model Size**: The `tumor_detection_model.h5` file is large. Ensure your deployment platform has enough memory (RAM) to load the TensorFlow model. The free tiers of some platforms might crash if the model uses too much memory.
*   **API Keys**: Never commit your `.env` file to GitHub. Always set the `GEMINI_API_KEY` as an environment variable in your deployment platform's dashboard.
