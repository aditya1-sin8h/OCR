import easyocr
import numpy as np
from PIL import Image
import io

def easyocr_ocr(image_file):
    # Open the image using PIL directly from the file-like object
    img = Image.open(image_file)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Initialize EasyOCR reader (Hindi and English language support)
    reader = easyocr.Reader(['en', 'hi'])  # Modify languages as needed
    result = reader.readtext(img_array, detail=0)  # Get text only, no bounding boxes

    if result:
        return {
            "status": "success",
            "extracted_text": '\n'.join(result)
        }
    else:
        return {
            "status": "error",
            "message": "Could not extract text from the image"
        }
