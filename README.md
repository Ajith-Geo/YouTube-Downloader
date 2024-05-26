# YouTube Downloader (Ver 0.3)

This documentation provides details on how to use a simple YouTube video downloader (BETA Version) built using Python's `pytube` library and `tkinter` for the GUI. This tool allows users to download YouTube videos by entering the video URL. Once the project is mature enough, I will do a stable release.

NOTE: Not all video downloads are supported as there are many exceptional cases which are to be handled.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [downloader Function](#downloader-function)
  - [user_input Function](#user_input-function)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/) `Python >= 3.7`
2. Clone the `Youtube-Downloader` repository or download the latest source-code.zip from the releases section.
3. If the zip file was downloaded, Extract the zip folder and navigate into the extracted folder (follow this step only if the zip file was downloaded from the releases section. Else, skip to step 4)  
4. Open Terminal from the `Youtube-Downloader` folder.
5. Execute the below command in the Terminal to install the libraries required:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `hello.py` script.
2. Enter the YouTube video URL into the input field when the GUI pops up.
3. Click the "Download" button.
4. The video will be downloaded to `C:/Users/<user-name>/Downloads` with the filename `ytdownload.mp4`. (replace the `<user-name>` with your `username` according to your system)

## Code Explanation

### downloader Function

This function takes a YouTube video URL, fetches the video stream with a specific `itag`, and downloads it.

```python
def downloader(url):
    yt = YouTube(url=url)
    print("Download started")
    stream = yt.streams.get_by_itag(itag=278)
    stream.download(filename="ytdownload.mp4", output_path="C:/Users/<user-name>/Downloads")
    print("Download done")
```
### user_input Function

This function retrieves the URL entered by the user in the input field and calls the `downloader` function to download the video.

```python
def user_input():
    url = text_inp.get()
    downloader(url=url)
```
## Known Issues

- **Fixed Low-Resolution Stream**: The script currently downloads a fixed low-resolution stream (itag=278). You can modify the `itag` value in the `downloader` function to download different resolutions.
- **Hardcoded Download Path**: The download path is set to the `Downloads` folder in the user's home directory. Consider adding an option for the user to specify the download path.
- **Error Handling**: The script does not currently handle errors that may occur during the download process, such as invalid URLs or network issues. Adding error handling would improve the robustness of the application.
- **GUI Enhancements**: The current GUI is very basic. Enhancements such as progress indicators, better layout management, and more user-friendly messages would improve the user experience.

## Contributing
If you have suggestions or improvements, feel free to contribute. You can fork the repository, make your changes, and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
