# YouTube Transcript Summarizer with Google Generative AI

This project allows you to extract transcripts from YouTube videos and generate concise summaries using Google's Generative AI, specifically the **gemini-1.5-flash** model. It leverages AI-powered language capabilities to convert lengthy video transcripts into succinct summaries.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Overview

The YouTube Transcript Summarizer provides an easy way to condense video content by summarizing its transcript. Using Google's advanced generative AI model, it processes the transcript to give you the most relevant points, making it easier to grasp the essence of the video without watching the whole thing.

## Features

- **Extracts transcripts** from YouTube videos using their URLs.
- **Cleans and processes** the transcript to remove timestamps for a cleaner output.
- Uses **Google's Generative AI (gemini-1.5-flash)** model to generate concise summaries.
- Simple and configurable for generating human-like summaries in plain text.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Python 3.7 or higher:** [Download Python](https://www.python.org/downloads/)
2. **pip (Python package manager):** This usually comes with Python installations.
3. **Google Generative AI API Key:** Sign up for an account and obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).

## Installation

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/sakethanne/video_summarization.git
cd video_summarization
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Set Up Google API Key

```bash
export API_KEY='your-google-generative-ai-api-key'
```

### 4. Run the file

```bash
python Summarize_video.py
```

This will open a terminal where you can enter the URL of the YouTube video you want to summarize.
