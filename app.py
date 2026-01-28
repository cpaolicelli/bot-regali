import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Gift Bot",
    page_icon="🎁",
    layout="wide"
)

# Custom CSS to center the header and text
st.markdown("""
<style>
    .main-header {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-text {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Header and Text
st.markdown('<div class="main-header">Gift Bot 🎁</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Welcome! Check out our assistant below.</div>', unsafe_allow_html=True)

# Landbot Integration
# The user provided code with "height: px", so we will set a default height of 500px to ensure visibility.
landbot_code = """
<script SameSite="None; Secure" type="module" src="https://cdn.landbot.io/landbot-3/landbot-3.0.0.mjs"></script>
<div id="myLandbot" style="width: 100%; height: 500px"></div>
<script type="module">
  var myLandbot = new Landbot.Container({
    container: '#myLandbot',
    configUrl: 'https://storage.googleapis.com/landbot.online/v3/H-3311190-SFATX0NBXX7S4HFF/index.json',
  });
</script>
"""

# Render the Landbot code
components.html(landbot_code, height=550, scrolling=True)
