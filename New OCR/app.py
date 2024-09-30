import streamlit as st
from file1 import easyocr_ocr
from PIL import Image

st.title("Hindi-English OCR with Keyword Search (EasyOCR)")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Rewind the file uploader to use it for OCR
    uploaded_file.seek(0)  # Reset the file pointer

    # Perform OCR using EasyOCR
    ocr_output = easyocr_ocr(uploaded_file)  # Pass the file object directly

    # Check for errors in OCR processing
    if ocr_output["status"] == "success":
        extracted_text = ocr_output["extracted_text"]
        
        # Display extracted text in plain text and JSON format
        st.text_area("Extracted Text", extracted_text, height=200)
        st.json(ocr_output)
        
        # Search functionality
        keyword = st.text_input("Search within the extracted text")
        if keyword:
            st.write("Search Results:")
            # Perform keyword search
            results = [line for line in extracted_text.split('\n') if keyword.lower() in line.lower()]
            if results:
                for result in results:
                    st.write(result)
            else:
                st.write("No matching results found.")
    else:
        st.error(f"Error: {ocr_output['message']}")
