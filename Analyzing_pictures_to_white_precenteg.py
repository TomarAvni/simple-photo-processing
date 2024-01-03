import cv2
import numpy as np
import os


class ImageAnalyzer:
    """
    Analyzes images to calculate the percentage of white pixels.

    Args:
        image_path (str): The path to the image file.
        threshold (int, optional): The threshold for binarization. Defaults to 200.
    """

    def __init__(self, image_path, threshold=200):
        self.image_path = image_path
        self.threshold = threshold

    def analyze_white_percentage(self):
        """
        Analyzes the image and calculates the percentage of white pixels.

        Returns:
            float: The percentage of white pixels in the image.
        """

        img = cv2.imread(self.image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, self.threshold, 255, cv2.THRESH_BINARY)

        white_pixels = np.sum(thresh == 255)
        total_pixels = gray.size
        white_percentage = (white_pixels / total_pixels) * 100

        return white_percentage


def collect_file_paths(folder_path):
    """
    Collects all file paths within a folder recursively.

    Args:
        folder_path (str): The path to the folder to scan.

    Returns:
        list: A list of all file paths within the folder.
    """

    file_paths = []
    for root, directories, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


if __name__ == "__main__":
    folder_to_scan = "path/to/your/folder"  # Replace with the actual folder path
    file_paths = collect_file_paths(folder_to_scan)

    for image_path in file_paths:
        analyzer = ImageAnalyzer(image_path)
        white_percentage = analyzer.analyze_white_percentage()
        print(f"Percentage of white in {image_path}: {white_percentage:.2f}%")  # Formatted output
