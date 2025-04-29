import streamlit as st
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import random
from io import BytesIO

# Page config
st.set_page_config(page_title="Image Processing Lab", layout="wide")


# Custom CSS for Medical Image Processing Simulation
st.markdown("""
    <style>
    /* Global Styles */
    body {
        font-family: 'Arial', sans-serif;
        background-color:rgb(177, 205, 65);
        color: #333;
    }

    /* Sidebar Styles */
    [data-testid="stSidebar"] {
        background-color:rgb(52, 69, 130);
        color: white;
        padding-top: 20px;
        padding-left: 20px;
        padding-right: 20px;
    }

    /* Sidebar navigation tabs */
    .stSidebarMenu>div {
        padding: 18px 35px;
        background-color: #2d3b56;
        color: #ffffff;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
        border-radius: 6px;
    }

    .stSidebarMenu>div:hover {
        background-color: #3f4d72;
        transform: scale(1.05);
    }

    .stSidebarMenu>div[data-selected="true"] {
        background-color: #4c5c82;
    }

    /* Main content padding */
    .main-content {
        padding: 25px 30px;
        text-align: center;
    }

    /* Header Styling */
    .header {
        font-size: 38px;
        font-weight: 600;
        color:rgb(88, 147, 174);
        margin-bottom: 25px;
    }

    .subheader {
        font-size: 28px;
        font-weight: 500;
        color: #005b8c;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 22px;
        font-weight: bold;
        color: #336e8e;
        margin-bottom: 20px;
    }

    /* Footer Section - Centered properly */
    .footer {
        position: fixed;
        bottom: 0;
        width: 60%;
        padding: 10px;
        text-align: center;
        background-color: transparent;
        color: #666;
        font-size: 14px;
    }

    /* Button Hover Effects */
    .stButton>button:hover {
        background-color: #006db3;
        transition: all 0.3s;
    }

    /* Download Button Special Hover Effects */
    div.stDownloadButton > button {
        background-color:rgb(181, 220, 121);
        color: white;
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        transition: background-color 0.3s, box-shadow 0.3s;
        margin-top: 10px;
    }

    div.stDownloadButton > button:hover {
        background-color: #45a049;
        box-shadow: 0 0 10px #45a049, 0 0 20px #45a049;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed by: ABHISHEK KUMAR JHA, SUJAY BALACHANDAR, ASHWIN EV, MASHEER M, KIRDHIHESH S.G</div>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Image Processing Lab")
menu_options = {
    "Home": "home",
    "Theory": "theory",
    "Simulation": "simulation",
    "Applications": "applications",
    "Trivia": "trivia",
    "Discussion": "discussion",
    "References": "references"
}

# Initialize session state
if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = "home"

# Sidebar radio (No checkboxes)
selected_label = st.sidebar.radio("Select a Section", list(menu_options.keys()))
st.session_state.selected_tab = menu_options[selected_label]

# ---------------------------------------
# Home Tab
# ---------------------------------------
if st.session_state.selected_tab == "home":
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.header("Image Processing Lab")
    st.markdown("""
        The **Image Processing Lab** focuses on exploring the theoretical and practical aspects of medical image transformations.
        We work with techniques like DCT, FFT, and their applications in medical fields.
    """)
    st.image("Medical Image Processing.jpeg", caption="Medical Image Processing", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------
# Theory Tab
# ---------------------------------------
elif st.session_state.selected_tab == "theory":
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.header("Theory of Image Processing Transforms")

    st.markdown("**Aim:** To understand the various transforms and their role in medical image processing.")
    
    st.markdown("**Objectives:**")
    st.markdown("""
    - To explore the **Discrete Cosine Transform (DCT)** and its compression utility.
    - To study the **Fast Fourier Transform (FFT)** and its frequency analysis.
    - To analyze the **Inverse Transforms** and their significance in image reconstruction.
    """)

    st.markdown("**Theory:**")
    st.markdown("""
    The **Discrete Cosine Transform (DCT)** is a mathematical technique used to transform spatial domain data (such as pixel values in an image) into frequency domain data. It is widely used in image compression algorithms, particularly in medical imaging, because it helps separate important image features from less significant ones. By converting an image into its frequency components, DCT allows for efficient data compression, reducing file size without significant loss of important image information. This is particularly valuable for transmitting large medical images, where reducing data size without compromising detail is crucial.

    The **Fast Fourier Transform (FFT)** is a more general approach to analyzing an image’s frequency components. It decomposes an image into its sine and cosine components, providing insights into patterns, noise, and periodic features within the image. This is essential for enhancing image quality, as FFT can be used for noise reduction, image sharpening, and feature extraction in medical imaging, such as detecting tumors or other abnormalities.

    After processing or compressing an image in the frequency domain using DCT or FFT, the **Inverse Discrete Cosine Transform (IDCT)** and **Inverse Fast Fourier Transform (IFFT)** are used to reconstruct the image back into the spatial domain. These processes are critical for returning the image to a viewable format after modification, compression, or enhancement. The ability to accurately reconstruct the image ensures that the modifications do not result in significant data loss, maintaining the image's integrity for clinical or diagnostic purposes.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------
# Simulation Tab
# ---------------------------------------
def convert_image(img_array, format='JPEG'):
    output = BytesIO()
    img_pil = Image.fromarray(np.uint8(img_array))
    img_pil.save(output, format=format)
    return output.getvalue()

if st.session_state.selected_tab == "simulation":  # Change 'elif' to 'if'
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.header("Medical Image Processing Simulation")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = np.array(img)

        # Convert to grayscale if the image is colored
        if len(img.shape) == 3:  
            img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  
        else:
            img_gray = img

        # Apply DCT, IDCT, FFT, IFFT
        dct_img = cv2.dct(np.float32(img_gray))
        idct_img = cv2.idct(dct_img)
        fft_img = np.fft.fft2(img_gray)
        ifft_img = np.fft.ifft2(fft_img)

        # Display results
        fig, axs = plt.subplots(2, 3, figsize=(12, 8))  # 2 rows, 3 columns for 6 boxes
        axs[0, 0].imshow(img)
        axs[0, 0].set_title('Original Image')
        axs[0, 0].axis('off')

        axs[0, 1].imshow(img_gray, cmap='gray')
        axs[0, 1].set_title('Grayscale Image')
        axs[0, 1].axis('off')

        axs[0, 2].imshow(np.log(np.abs(dct_img)), cmap='gray')
        axs[0, 2].set_title('DCT')
        axs[0, 2].axis('off')

        axs[1, 0].imshow(idct_img, cmap='gray')
        axs[1, 0].set_title('IDCT')
        axs[1, 0].axis('off')

        axs[1, 1].imshow(np.log(np.abs(fft_img)), cmap='gray')
        axs[1, 1].set_title('FFT')
        axs[1, 1].axis('off')

        axs[1, 2].imshow(np.abs(ifft_img), cmap='gray')
        axs[1, 2].set_title('IFFT')
        axs[1, 2].axis('off')

        # Hide remaining empty subplots
        for ax in axs.flat:
            ax.set_xticks([]) 
            ax.set_yticks([])

        st.pyplot(fig)
        st.markdown('<p style="font-size:18px;">The images above show the original image, its grayscale version, and the result of applying DCT, IDCT, FFT, and IFFT transformations.</p>', unsafe_allow_html=True)

        # Option to download transformed images
        st.download_button(label="Download Original Image", data=convert_image(img), file_name="original_image.jpeg", mime="image/jpeg")
        st.download_button(label="Download DCT Image", data=convert_image(np.log(np.abs(dct_img))), file_name="dct_image.jpeg", mime="image/jpeg")
        st.download_button(label="Download FFT Image", data=convert_image(np.log(np.abs(fft_img))), file_name="fft_image.jpeg", mime="image/jpeg")
        
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------
# Applications Tab
# ---------------------------------------
elif st.session_state.selected_tab == "applications":
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.header("Applications of Image Processing in Medicine")
    
    # Columns for better alignment
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        Medical image processing plays a pivotal role in diagnostics and treatment. Below are some key applications:
        
        - **Medical Imaging Techniques (CT, MRI, X-rays):** These transformations are used to enhance medical images for better clarity, assisting radiologists in diagnosing conditions. For instance, through image enhancement techniques like contrast adjustment, medical imaging becomes sharper and more accurate.
        
        - **Image Compression:** DCT and FFT are used in compressing images while retaining critical information for diagnostic purposes. For example, MRI scans can be compressed to reduce storage space and transmission times, essential for large-scale hospitals and healthcare systems.
        
        - **Image Enhancement:** Through Fourier analysis, medical images can be enhanced by removing noise or improving contrast, vital for clearer interpretations in diagnostics. This enhancement is crucial in detecting subtle features in medical images, such as early signs of cancer or neurological conditions.
        
        - **3D Imaging & Visualization:** Advanced techniques allow for the reconstruction of 3D models from 2D CT/MRI scans, which assists in planning surgeries or understanding complex anatomy.
        """)

    with col2:
        st.image("https://c8.alamy.com/comp/D7MWDF/chest-anatomy-3d-ct-scan-D7MWDF.jpg", caption="CT Scan", use_container_width=True)
        st.image("https://www.researchgate.net/profile/Basant-Kumar-7/publication/261048930/figure/fig2/AS:392395146448899@1470565701385/Original-and-compressed-MRI-images-a-original-image-and-compressed-images-with_Q640.jpg", caption="Image Compression Example", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------
# Discussion Tab
# ---------------------------------------
elif st.session_state.selected_tab == "discussion":
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.header("Discussion")
    
    st.markdown("""
    Let's discuss how **DCT** and **FFT** are reshaping medical imaging and their applications in improving diagnostic accuracy.

    - **Share your experience**: Have you used any of these transformations in your research or practical work?
    - **Challenges**: What challenges have you encountered while working with medical images, especially in terms of compression, enhancement, or noise removal?
    - **Future of Medical Imaging**: With AI’s influence on medical image analysis, how do you see the role of DCT/FFT evolving in the next few years?
    
    Feel free to share your thoughts and insights on how image processing can advance healthcare, improve diagnostics, and enhance patient outcomes.
    """)

    # Adding a text input for deeper engagement
    user_input = st.text_area("Share your thoughts or experiences related to image processing in medicine.", "")
    
    if user_input:
        st.success("Thank you for sharing your thoughts!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------
# Trivia Tab with Quiz Section
# ---------------------------------------
elif st.session_state.selected_tab == "trivia":
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.header("Image Processing Trivia & Quiz")

    trivia = [
        "1. The first digital image was created in 1957 by Russell Kirsch.",
        "2. The DCT is commonly used in JPEG image compression.",
        "3. The FFT algorithm was introduced by Cooley and Tukey in 1965."
    ]
    
    for item in trivia:
        st.markdown(f"**{item}**")
    
    st.markdown("### Quiz Time!")
    st.markdown("""
    **Question:** What transform is commonly used in medical image compression?
    """)
    
    answer = st.radio("Choose one", ["DCT", "FFT", "IDCT", "Wavelet Transform"])
    
    if answer == "DCT":
        st.success("✅ Correct! DCT is commonly used in medical image compression.")
    else:
        st.error("❌ Incorrect. The correct answer is DCT.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------
# References Tab
# ---------------------------------------
elif st.session_state.selected_tab == "references":
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.header("References")

    st.markdown("""
    Here are some important references related to the concepts of medical image processing, DCT, and FFT:

    1. **Ahmed, N., Natarajan, T., & Rao, K. R. (1974).** Discrete Cosine Transform. IEEE Transactions on Computers, 23(1), 90-93.
    2. **Cooley, J. W., & Tukey, J. W. (1965).** An algorithm for the machine calculation of complex Fourier series. Mathematics of Computation, 19(90), 297-301.
    3. **Gonzalez, R. C., & Woods, R. E. (2008).** Digital Image Processing (3rd ed.). Pearson Prentice Hall.
    4. **Jain, A. K. (1989).** Fundamentals of Digital Image Processing. Prentice-Hall.
    5. **Rangayyan, R. M. (2004).** Biomedical Image Analysis. CRC Press.
    6. **Shapiro, J. M., & Wakin, M. B. (2009).** Medical Image Compression and Restoration using Wavelet Transforms. IEEE Transactions on Image Processing, 18(7), 1479-1488.
    7. **Wang, Z., & Bovik, A. C. (2009).** Modern Image Quality Assessment. Synthesis Lectures on Image, Video, and Multimedia Processing, 1(1), 1-156.
    8. **Zhang, Y., & Liu, S. (2011).** Image Compression Algorithms in Medical Imaging. Journal of Medical Imaging and Health Informatics, 1(1), 1-10.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)
