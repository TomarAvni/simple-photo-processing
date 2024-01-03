# simple-photo-processing

Here's a comprehensive README for your GitHub repository:

# Image White Percentage Analyzer

This Python project analyzes images to calculate the percentage of white pixels. It's useful for tasks such as:

Quantifying white space in document scans
Evaluating image quality based on brightness
Identifying images with excessive white areas
And more!
## Installation

Clone the repository:

Bash
git clone [https://github.com/your-username/image-white-percentage-analyzer.git](https://github.com/TomarAvni/simple-photo-processing)

Install dependencies:

Bash
pip install -r requirements.txt

## Usage

Edit the folder_to_scan variable in the main.py file to specify the path to your image folder.

Run the script:

Bash
python main.py

The script will print the percentage of white pixels for each image in the folder.

## Example Output

Percentage of white in image1.jpg: 25.68%
Percentage of white in image2.png: 87.44%
Percentage of white in image3.tif: 12.15%
## Customization

Adjust the threshold parameter in the ImageAnalyzer class to fine-tune the binarization process.
Modify the collect_file_paths function to filter file types or include subdirectories.
## Contributing

We welcome contributions! Please feel free to fork the repository and submit pull requests.
