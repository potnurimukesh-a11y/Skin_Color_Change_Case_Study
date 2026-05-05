Color Transformation Case Study (Image Processing in Python)

📌 Overview

This project is a case study focused on modifying color characteristics of an image using Python.
It applies pixel-level transformations to adjust color intensity based on specific RGB conditions.

The program selectively modifies pixels that satisfy certain color thresholds, demonstrating how image appearance can be altered programmatically.

---

🎯 Objectives

- To understand pixel-level image manipulation
- To apply conditional color transformations
- To explore RGB-based filtering techniques
- To analyze how color intensity affects image appearance

---

⚙️ Features

- Loads and processes an image
- Applies conditional logic on RGB values
- Adjusts pixel intensity dynamically
- Enhances or modifies selected regions of the image
- Displays both original and processed images

---

🛠️ Technologies Used

- Python
- Pillow (PIL)
- Custom "SimpleImage" library

---

🧠 Concepts Applied

- Image processing fundamentals
- RGB color model
- Conditional filtering
- Pixel manipulation
- Iteration over image data

---

📂 Project Structure

Skin_Color_Change_Case_Study/
│
├── trumph_change.py        # Main program (color transformation logic)
├── simpleimage.py          # Image handling utility
├── images/                 # Input images
├── README.md

---

▶️ How It Works

- The image is loaded using "SimpleImage"
- Each pixel is analyzed based on RGB values
- A condition is applied:
  - If red channel satisfies specific thresholds compared to green and blue
- Selected pixels are modified by scaling RGB values
- The processed image is displayed

---

▶️ How to Run

1. Install required library:

pip install pillow

2. Run the program:

python trumph_change.py

---

📷 Output

- Displays the original image
- Displays the processed image with adjusted color tones

---

📚 Example Logic

- If a pixel meets the condition:
  - Reduce red, green, and blue values proportionally
- This creates a visible tonal adjustment in selected regions

---

📚 Conclusion

This project demonstrates how conditional logic and pixel manipulation can be used to transform image colors. It highlights the importance of understanding RGB channels in digital image processing.

---

👨‍🏫 Acknowledgement

This case study was developed based on concepts and guidance provided during classroom sessions by the instructor.
