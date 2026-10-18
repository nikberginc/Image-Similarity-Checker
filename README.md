# Image Similarity Checker 🖼️

**Completed:** January 30, 2026

Image Similarity Checker is a Python command-line application designed to identify identical and visually similar images by comparing their visual characteristics.

The program uses **OpenCV**, **difference hashing (dHash)**, **average hashing (aHash)**, and **Hamming distance** to calculate a similarity percentage between a reference image and other images in a selected folder.

I originally started this project with a different goal, but later repurposed it into an image similarity detection tool. The project allowed me to experiment with image processing, binary representations, custom algorithms, and working with multiple Python modules.

## Features

- **Image similarity detection:** Compare a reference image against multiple images in a selected folder.
- **Difference hashing (dHash):** Analyze brightness differences between neighboring pixels.
- **Average hashing (aHash):** Compare individual pixel brightness against the image's average brightness.
- **Combined similarity calculation:** Use both hashing algorithms to calculate an overall similarity score.
- **Image classification:** Categorize images as identical, very similar, similar, or different.
- **Automatic image organization:** Optionally copy identical and very similar images into dedicated folders.
- **Multiple image formats:** Supports PNG, JPG, JPEG, and BMP files.
- **Execution time measurement:** Display how long the comparison process takes.
- **Modular structure:** Separate image processing, comparison, file management, and output functionality into individual Python modules.

## Requirements

- Python 3
- OpenCV
- NumPy (used internally by OpenCV)

Install the required libraries:

```bash
python -m pip install opencv-python numpy
```

The program also uses Python's built-in `os`, `time`, and `shutil` modules.

**Note:** The optional image organization feature uses the Windows `USERPROFILE` environment variable to locate the Documents directory.

## Installation

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Install the required libraries.
4. Keep all six Python files in the same directory.
5. Open a terminal in the project's directory.
6. Run:

   ```bash
   python Main-Comparesment.py
   ```

## How to Use

### 1. Choose Whether to Organize Images

When the program starts, it asks whether you want to create folders for identical and very similar images.

Enter `YES` to enable automatic organization.

Otherwise, enter a non-empty response such as `NO` to continue without creating folders.

### 2. Select the Reference Image

Enter the complete path to the image you want to compare against other images.

Example:

```text
C:/Users/YourName/Pictures/reference.jpg
```

The program uses this image as the reference for calculating similarity.

### 3. Select the Comparison Folder

Enter the path to the folder containing the images you want to analyze.

Example:

```text
C:/Users/YourName/Pictures/Photos
```

The program searches the selected folder for supported image formats and compares each image against the reference.

Only files directly inside the selected folder are processed. Subfolders are not scanned.

### 4. View the Results

After processing the images, the program prints their filenames and similarity percentages in the terminal.

**Illustrative output:**

```text
Name: image1.jpg - - Similarety: 100.0
Name: image2.jpg - - Similarety: 96.9
Name: image3.png - - Similarety: 85.2
Name: image4.jpg - - Similarety: 43.8

Program took: 125 ms to complete!
```

The scores and execution time above are illustrative and depend on the images and computer.

The program internally categorizes images according to their calculated similarity.

## Similarity Classification

The application uses four categories:

| Similarity | Category |
|---|---|
| 96–100% | Identical |
| 80–95.9% | Very Similar |
| 60–79.9% | Similar |
| Below 60% | Different |

These classifications are based on perceptual image hashes rather than exact file equality.

An image categorized as *Identical* is not necessarily pixel-for-pixel identical to the reference image.

## How It Works

### 1. Image Loading and Processing

The application uses OpenCV to load each image in grayscale.

```python
image_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
```

Grayscale processing reduces the image to brightness values, allowing the algorithm to compare visual structure without directly analyzing color information.

### 2. Difference Hashing (dHash)

The first algorithm generates a difference hash.

The image is resized to **9 × 8 pixels**.

```python
image = cv2.resize(image_cv, (9, 8))
```

Each pixel is compared with the pixel immediately to its right.

- If the left pixel is brighter, the algorithm stores `1`.
- Otherwise, it stores `0`.

```python
if row[x] > row[x + 1]:
    binary_d.append(1)
else:
    binary_d.append(0)
```

With eight comparisons per row across eight rows, the result is a **64-bit binary fingerprint**.

This fingerprint describes the image's horizontal brightness transitions.

### 3. Average Hashing (aHash)

The second algorithm generates an average hash.

The image is resized to **8 × 8 pixels**, giving 64 grayscale pixel values.

```python
image = cv2.resize(image_cv, (8, 8))
```

The program calculates the average brightness:

```python
avrage_brightness = sum(int(pixel) for pixel in list_all_pixals) / 64
```

Each pixel is compared against that average.

- A pixel brighter than the average becomes `1`.
- A pixel equal to or darker than the average becomes `0`.

```python
if list_all_pixals[i] > avrage_brightness:
    binary_a.append(1)
else:
    binary_a.append(0)
```

This creates another 64-bit binary fingerprint describing the distribution of brightness within the image.

**Implementation note:** Pixel values are converted to Python integers before summation to prevent integer overflow during the average-brightness calculation.

### 4. Hamming Distance

After generating the two hashes for each image, the program compares them against the corresponding reference hashes.

The Hamming distance counts how many corresponding bits are different.

```python
distance_dHAsh = sum(
    a != b for a, b in zip(org_image_dHash, compared_image_dHash)
)

distance_aHAsh = sum(
    a != b for a, b in zip(org_image_aHash, compared_image_aHash)
)
```

The two distances are combined:

```python
distance = distance_aHAsh + distance_dHAsh
```

Since each hash contains 64 bits, the combined comparison contains **128 bits**.

### 5. Calculating the Similarity Percentage

The program converts the total Hamming distance into a percentage.

```python
similarity = round(
    (1 - distance / (
        len(compared_image_aHash) + len(compared_image_dHash)
    )) * 100,
    1
)
```

The calculation is equivalent to:

**Similarity = (1 − Different bits / 128) × 100**

For example, if two images have 16 different bits across both fingerprints:

```text
Similarity = (1 - 16 / 128) × 100
Similarity = 87.5%
```

The program would classify the image as **Very Similar**.

### 6. Automatic Image Organization

If the user enables image organization, the application creates folders in the Windows Documents directory.

```text
Documents/
└── Comperesment/
    ├── Identical/
    └── VerySimilar/
```

Images with similarity scores of at least 96% are copied into `Identical`.

Images with similarity scores from 80% up to but not including 96% are copied into `VerySimilar`.

The program uses Python's `shutil.copy()` method.

The original images remain in their original locations.

Images classified as `Similar` or `Different` are not automatically copied into separate folders.

### 7. Measuring Execution Time

The program records the time before and after image comparison.

```python
start_time = time.time()
```

After processing:

```python
end_time = time.time()
```

It calculates the elapsed duration and displays it in milliseconds.

This helps measure how long the image comparison process takes.

## Project Structure

The application consists of six Python modules:

```text
Image-Similarity-Checker/
├── Main-Comparesment.py
├── ConvertingHasingFunction.py
├── ImageGetter.py
├── Checker.py
├── Newfile_creation.py
├── AddImage.py
├── .gitignore
└── README.md
```

### Module Responsibilities

| File | Function |
|---|---|
| `Main-Comparesment.py` | Main application, user input, and result display |
| `ConvertingHasingFunction.py` | Generates dHash and aHash fingerprints |
| `ImageGetter.py` | Finds supported image files in the selected folder |
| `Checker.py` | Calculates similarity percentages and categorizes images |
| `Newfile_creation.py` | Creates folders for matching images |
| `AddImage.py` | Copies matching images into their destination folders |

## Known Limitations

- **Perceptual similarity is approximate:** Different images can produce similar hashes, resulting in false positives.
- **No exact file verification:** An image classified as identical is not necessarily an exact duplicate at the pixel or file level.
- **Limited transformations:** Large rotations, cropping, substantial edits, or major changes in image composition can significantly affect the similarity score.
- **Limited formats:** The application only detects files with lowercase `.png`, `.jpg`, `.jpeg`, and `.bmp` extensions.
- **No recursive scanning:** Images inside subfolders are not processed.
- **Limited error handling:** Invalid paths, unreadable images, and unsupported inputs can cause errors.
- **Empty initial input:** Pressing Enter without a response at the first prompt can produce an `IndexError`.
- **Potential file overwriting:** Matching images with identical filenames can overwrite existing copies in the destination folders.
- **Windows-specific organization:** The optional output-folder system depends on the Windows `USERPROFILE` environment variable.
- **No graphical interface:** The program operates entirely through the terminal.

## Development Note

This project originally began as an experiment with a different objective but was later repurposed into an image similarity detection tool.

During its development, I explored image processing using OpenCV, grayscale pixel values, binary hashing algorithms, Hamming distance, and modular Python project organization.

The program represents an experimental implementation of perceptual image comparison rather than a fully optimized or production-ready duplicate image detection system.



**Author:** [Nik Berginc](https://github.com/nikberginc)
