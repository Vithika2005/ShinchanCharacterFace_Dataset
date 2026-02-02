# ShinchanCharacterFace_Dataset
ETL for Shinchan Character Faces. This project builds a curated dataset of Shinchan anime character faces from publicly available videos, using a fully automated ETL pipeline. It is designed for machine learning, computer vision, and anime face recognition research.

🛠 Pipeline Overview
1. Extract (E)
Download raw Shinchan videos from multiple sources (YouTube, Dailymotion, Facebook, Reddit) using yt-dlp.
Support for multiple formats and resolutions, automatically selecting the best available.
Videos include full episodes, trailers, and dubbed content.

2. Transform (T)
Frame Extraction: Convert videos to frames using ffmpeg. Frames can be extracted at 1–5 frames per second depending on dataset size requirements.
Anime Face Detection: Detect all Shinchan character faces in the extracted frames using a pre-trained anime face detection model.
Face Cropping: Crop detected face regions and standardize them into uniform sizes for ML training.
Deduplication: Remove duplicate images using perceptual hashing (imagehash) to ensure a clean, non-redundant dataset.

3. Load (L)
Save processed faces in a structured directory ready for ML pipelines

⚡ Features
Fully automated batch processing: videos → frames → face crops → deduped dataset
Supports multiple platforms and video formats
Ready-to-use dataset for anime face recognition or generative tasks

💡 Usage
Populate links.txt with video URLs.
Run yt-dlp to download all videos.
Execute the frame extraction script to generate frames from videos.
Run the face detection and cropping scripts to prepare dataset.


## Dataset

Full dataset is hosted on Kaggle due to GitHub file size limits:

Kaggle Dataset Link:
https://www.kaggle.com/datasets/vithikasurve/shinchancharacterfaces

This repo contains:
- dataset generation pipeline
- scraping scripts
- face detection & cropping code
- duplicate removal logic

Use the deduplication script to remove redundant frames.

Dataset is ready for ML training or public release.
