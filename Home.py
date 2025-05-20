import base64
import streamlit as st

st.set_page_config(page_title='Disease Detection',page_icon='🧊',initial_sidebar_state="collapsed")
@st.cache_data
def get_img_as_base64(file):
    with open(file,"rb") as f:
        data=f.read()
    return base64.b64encode(data).decode()
get_img_as_base64("dna9.jpg")



st.markdown(
    """
    <style>
    /* Set font family and size */
    .my-text {
        
        font-family: 'Arial';
        font-weight: 800;
        font-size: 75px;
        
    }

    
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Set font family and size */
    .text-container {
    position: relative;
        width: 1000px;
        height: 150px;
        left: -20%;
    }

    
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Set font family and size */
    .element-container.st-emotion-cache-1vae0mb.e1f1d6gn4 {
    
        left: 50%;
    }

    
    </style>
    """,
    unsafe_allow_html=True
)


# Text content with custom class
st.markdown('<div class="text-container"><span class="my-text">WE START WHERE THE WORLD STOPS.</span></div>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Position the button */
    .button-container {
        position: relative;
        top: 70%;
        left: 70%;
        transform: translate(-90%, -50%);
    }
    </style>
    """,
    unsafe_allow_html=True
)
button_clicked = st.button(label="Get started", key="custom_button", )
button_container = st.markdown(
    f'<div class="button-container"></div>',
    unsafe_allow_html=True
)
if button_clicked:
    st.switch_page("pages/Dementia Predictor.py")

st.markdown(
    """
    <style>
    /* Position the button */
    .row-widget.stButton{
        position: absolute;
        top: 120%;
        left: 90%;
        transform: translate(-50%, 400%);
        
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Position the button */
    .my-text{
        position: relative;
        top: 10%;
        left: 5%;
        transform: translate(-50%, -200%);
        
        
    }
    </style>
    """,
    unsafe_allow_html=True
)
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .main {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: local;
    opacity: 0.7;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('dna9.jpg')
st.markdown(
    """
    <style>
    /* Position the button */
    .st-emotion-cache-19rxjzo.ef3psqc12{
        position: relative;
        height: 40px;
        width: 240px;
        top: 50%;
        left: -10%;
        background-color: #172130;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.subheader("GET YOUR CT SCANS ANALYSED")
# st.markdown(
#     """
#     <style>
#     .container {
#         position: relative;
#         border: 1px solid #ddd;
#         border-radius: 5px;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#         padding: 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Content inside the bordered container
# st.markdown("<div class='container'>This is a bordered container.</div>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Position the button */
    .st-emotion-cache-10trblm.e1nzilvr1{
        position: relative;
        left: 20%;
        font-style: 'Arial';
        font-weight: 800;
        
        
        
        
        
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Position the button */
    .eyeqlp51.st-emotion-cache-1pbsqtx.ex0cdmw0{
        visibility: hidden;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .st-emotion-cache-1avcm0n.ezrtsby2{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background-color: #000000;
        border-bottom: 1px solid #e9ecef;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom navigation bar with text
