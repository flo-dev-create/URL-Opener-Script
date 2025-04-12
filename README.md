# URL Opener Script

This Python script allows users to open a list of URLs from a text file in their preferred browser, with support for multiple browsers (Chrome, Firefox, Waterfox, Brave, Opera) and automatic operating system detection (Windows, Linux, macOS). Users can also customize browser paths if needed.

## Features

- **Automatic OS Detection**: Detects the operating system (Windows, Linux, macOS) and uses appropriate browser paths.
- **Browser Selection**: Choose from Chrome, Firefox, Waterfox, Brave, or Opera.
- **Customizable Paths**: Modify browser paths directly in the script if the default paths are incorrect.
- **Batch URL Opening**: Opens all URLs from a text file, one by one, with a delay between each.
- **Error Handling**: Handles missing files, invalid paths, and other common issues gracefully.

## Requirements

- Python 3.x
- A text file containing URLs (one URL per line)
- Installed browsers (Chrome, Firefox, Waterfox, Brave, or Opera)

## Installation

1. Clone this repository or download the script file:
   ```bash
   git clone https://github.com/your-username/url-opener-script.git
   cd url-opener-script
   ```

2. Ensure Python 3.x is installed on your system. You can check by running:
   ```bash
   python --version
   ```

3. Install any required Python libraries (if applicable). This script uses only standard libraries, so no additional installation is typically needed.

## Usage

1. Prepare a text file containing the URLs you want to open. Each URL should be on a separate line, for example:
   ```
   https://www.google.com
   https://www.mozilla.org
   https://www.waterfox.net
   ```

2. Run the script:
   ```bash
   python url_opener.py
   ```

3. Follow the interactive prompts:
   - Select your operating system (Windows, Linux, macOS).
   - Choose your preferred browser (Chrome, Firefox, Waterfox, Brave, Opera).
   - Enter the path to your text file containing the URLs.
   - Optionally, modify the browser path if the default path is incorrect.

4. The script will open each URL in a new tab of the selected browser, with a delay of 1 second between each.

## Example

Here’s an example of how the script works:

1. **Run the script**:
   ```bash
   python url_opener.py
   ```

2. **Select your OS**:
   ```
   Detected OS: Windows
   1. Windows
   2. Linux
   3. macOS
   0. Quit
   Your choice: 1
   ```

3. **Choose your browser**:
   ```
   1. Chrome
   2. Firefox
   3. Waterfox
   4. Brave
   5. Opera
   0. Back
   Your choice: 2
   ```

4. **Enter the path to your text file**:
   ```
   Enter the path to your file containing URLs: C:/path/to/urls.txt
   ```

5. **Modify browser path (optional)**:
   ```
   Default browser path: C:/Program Files/Mozilla Firefox/firefox.exe
   Do you want to modify this path? (y/N): N
   ```

6. **URLs are opened**:
   ```
   Opening 3 URLs...
   Opening URL 1/3
   Opening URL 2/3
   Opening URL 3/3
   All URLs have been opened successfully!
   ```

## Customization

- **Default Browser Paths**: You can modify the default browser paths in the script under the `chemins_navigateurs` dictionary.
- **Delay Between URLs**: Adjust the delay between opening URLs by changing the `time.sleep(1)` value in the script.

## Troubleshooting

- **Browser Not Found**: Ensure the browser is installed and the path is correct. You can manually specify the path during the script execution.
- **File Not Found**: Verify the file path to your text file containing URLs.
- **Invalid URLs**: Ensure the URLs in your file are properly formatted (e.g., starting with `http://` or `https://`).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the script.

## Author

- **Your Name** - [Your GitHub Profile](https://github.com/your-username)
