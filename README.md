# YouTube Downloader

This documentation provides details on how to use a simple YouTube video downloader built using Python's `pytube` library and `tkinter` for the GUI. This tool allows users to download YouTube videos by entering the video URL.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [downloader Function](#downloader-function)
  - [user_input Function](#user_input-function)
  - [GUI Setup](#gui-setup)
- [Running the Application](#running-the-application)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/). ![Static Badge](https://img.shields.io/badge/Python-3.7-blue)

2. Install the required libraries using pip:

    ```bash
    pip install pytube
    ```

## Usage

1. Run the `hello.py` script.
2. Enter the YouTube video URL into the input field when the GUI pops up.
3. Click the "Download" button.
4. The video will be downloaded to `C:/Users/masge/Downloads` with the filename `messi.mp4`. (set the download path according to your system)

## Code Explanation

### downloader Function

This function takes a YouTube video URL, fetches the video stream with a specific `itag`, and downloads it.

```python
def downloader(url):
    yt = YouTube(url=url)
    print("Download started")
    stream = yt.streams.get_by_itag(itag=278)
    stream.download(filename="messi.mp4", output_path="C:/Users/masge/Downloads")
    print("Download done")
```
## Contributing
If you have suggestions or improvements, feel free to contribute. You can fork the repository, make your changes, and create a pull request.
