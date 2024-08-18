# Image to ASCII Converter

A simple GUI application for converting images to ASCII art. This tool supports color and black-and-white ASCII art and allows saving the result in the same directory as the source image or a specified directory.

## Features

- **Image to ASCII Conversion**: Converts images into ASCII art.
- **Color Mode**: Toggle color mode for colored ASCII output.
- **Custom Dimensions**: Specify width and height for the output image in color mode.
- **Background Color Option**: Choose between black or white background for colored ASCII art.
- **Flexible Save Locations**: Save output in the same directory as the source image or specify a different directory.

![robot-toy-security-issue-featured](https://github.com/user-attachments/assets/9d9a63d3-78b9-4ad6-82f6-c1fe3977d9f9)
![robot-toy-security-issue-featured_output(wbg)](https://github.com/user-attachments/assets/56c22450-8844-4f7a-b8a8-c671cd1e6d7e)
![robot-toy-security-issue-featured_output(bbg)](https://github.com/user-attachments/assets/fc08f0e8-2761-4694-b9a5-4025735036c6)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/image-to-ascii-converter.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd image-to-ascii-converter
    ```

3. **Install dependencies**:

    Make sure you have `Pillow` and `tkinter` installed. You can install the required Python packages using:

    ```bash
    pip install pillow
    ```

## Usage

1. **Run the application**:

    ```bash
    python src/gui.py
    ```

2. **Select an image file**:
   - Click "Browse" next to "Select Image File" to choose the image you want to convert.

3. **Select a save directory** (optional):
   - Click "Browse" next to "Select Save Directory" to choose where to save the output. If "Save in Source Directory" is checked, this field will be disabled.

4. **Configure settings**:
   - **Enable Color**: Check this box to generate colored ASCII art. Additional fields for width and height, and background color options, will appear.
   - **Width and Height**: Specify dimensions for the output image when color mode is enabled.
   - **Background Color**: Choose between black or white background for the colored ASCII art.

5. **Convert the image**:
   - Click "Convert" to start the conversion process. The ASCII art will be saved based on your chosen settings.
