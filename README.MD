# YouTube Playlist Downloader

## Introduction
This project provides a Python script for downloading all videos from a specified YouTube playlist. It also captures each video's title and description and saves them in a Markdown file. This tool is ideal for users who want to archive video content from YouTube for offline viewing and reference.

## Installation

### Prerequisites
You need Python installed on your machine (Python 3.6+ recommended). Additionally, you need the `pytube` library, which can be installed using pip.
```bash
pip install pytube
```

## Usage
This script requires two command-line arguments: the URL of the YouTube playlist you want to download and the path where you want the videos to be saved.

### Running the Script
Run the script from your terminal or command prompt by navigating to the script's directory and typing:

```bash
python downloader.py "your_playlist_url_here" "your_download_path_here"
```
Replace "your_playlist_url_here" with the actual URL of the YouTube playlist and "your_download_path_here" with the directory where you want the videos saved.

The videos will be downloaded to the specified path, and a Markdown file named video_descriptions.md containing the videos' titles and descriptions will be generated in the same folder.