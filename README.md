# YouTube Comment Reporter Bot

This open-source project automates the process of reporting inappropriate comments on YouTube videos based on a list of keywords. The bot reads video URLs from a text document, navigates to each video, and reports comments containing any of the specified keywords.

## Features

- Automated login to YouTube.
- Reporting comments based on a predefined list of keywords.
- Processes multiple videos specified in a text document.
- Keeps track of the number of comments reported and saves the count to a text file.

## Prerequisites

- Python 3.6 or higher
- Google Chrome browser
- ChromeDriver

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/youtube-comment-reporter-bot.git
   cd youtube-comment-reporter-bot

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

3. **Install Required Packages**

   ```bash
   pip install selenium
   pip install webdriver-manager

4. **Download ChromeDriver**

   Download the ChromeDriver from [here](https://developer.chrome.com/docs/chromedriver/get-started) and place it in a known directory. Make sure to match the version with your installed Chrome browser.

5. **Create Required Text Documents**

   - `credentials.txt`: Place your YouTube email and password in this file, each on a new line.
     ```
     your-email@gmail.com
     your-password
     ```

   - `keywords.txt`: List of keywords to look for in comments, one per line.
     ```
     keyword1
     keyword2
     ```

   - `video_urls.txt`: List of YouTube video URLs to process, one per line.
     ```
     https://www.youtube.com/watch?v=dQw4w9WgXcQ
     https://www.youtube.com/watch?v=another_video_id
     ```

   - `chromedriverpath.txt`: The full path to your downloaded `chromedriver` executable.
     ```
     /path/to/chromedriver
     ```

## Usage

1. **Activate the Virtual Environment**

   ```bash
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`


2. **Run the Script**

   ```bash
   python main.py

The script will log in to YouTube, process each video URL from video_urls.txt, and report comments containing any keywords from keywords.txt. The total count of reported comments will be saved to count.txt.

## Example `credentials.txt`

```
your-email@gmail.com
your-password
```


## Example `keywords.txt`

```
spam
scam
abuse
```


## Example `video_urls.txt`

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=another_video_id
```


## Example `chromedriverpath.txt`

```
/Users/yourusername/Downloads/chromedriver
```


## Notes

- Ensure your Chrome browser and ChromeDriver versions match.
- The bot waits for manual entry of 2-factor authentication code if required.
- The bot includes a wait time to ensure all comments load before processing.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.


---

By following the instructions in this README, you should be able to set up and run the YouTube Comment Reporter Bot successfully. If you encounter any issues or have questions, feel free to open an issue on GitHub.
