 🎨 Half-Tone Visual Cryptography

Visual cryptographic schemes (VCS) provide a unique way to encrypt images into multiple share images, ensuring that no single share image reveals any information about the original secret image. This project proposes a visual cryptography encryption framework that decomposes a color image into separate monochromatic images based on the CMY color space. The resulting halftoned share images preserve the visual nature and quality of the original image.

## Overview

Visual cryptography leverages human vision characteristics for decryption, eliminating the need for cryptographic knowledge. It ensures security by preventing hackers from gaining any insights into the secret image from individual cover images. While traditionally developed for binary images, visual cryptography has expanded to grayscale and colored images, as explored in this report.

## Steps to Run the Project:

### 1. Save All Files in the Same Directory

Ensure that all project files, including `CMY.py`, `Halftone.py`, `main.py`, and `output.py`, are saved in the same directory.

### 2. Run CMY.py

Execute the `CMY.py` file, which serves to decompose the color image into Cyan, Magenta, and Yellow components based on the CMY color space.

### 3. Run Halftone.py

Run the `Halftone.py` file, responsible for converting the decomposed monochromatic images into halftone representations.

### 4. Run main.py

Execute the `main.py` file, which carries out the visual cryptography encryption process for each decomposition.

### 5. Run output.py

Run the `output.py` file, which compiles the encrypted share images into a final composite image.

### 6. Final Image Generation

After completing the above steps, a final composite image containing the encrypted shares will be saved in the same directory.

## Note:

- Ensure that all dependencies required by the project are installed in your environment.
- Customize the project as needed and explore further extensions based on your requirements.

By following these steps, you can successfully run the Half-Tone Visual Cryptography project and generate encrypted share images. Enjoy exploring the fascinating world of visual cryptography!
