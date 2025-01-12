import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
# from streamlit_option_menu import option_menu
from util import classify, set_background, on_change
# from streamlit_modal import Modal
# from streamlit_extras.switch_page_button import switch_page
import subprocess
import os
from google.oauth2 import id_token
from google.auth.transport import requests
# from brain import MRI
​
​
#Menu
selected = option_menu(None, ["Home", "Covid", "Brain", "About us" ],
                    icons=['house', 'lungs', "f5dc", "people"],
                    on_change=on_change, key='menu_4', orientation="horizontal")
​
if selected =="Home":
    #st.rerun() or st.experimental_rerun()
    print('Yes')
if selected == "Covid":
    subprocess.Popen(["streamlit", "run", "covid.py"])
    os._exit(0)
if selected == "Brain":
    MRI()
if selected == "About us":
    subprocess.Popen(["streamlit", "run", "aboutus.py"])
    os._exit(0)
​
def main():
​
    # modal = Modal(key="Demo Key", title="Welcome")
    # for col in st.columns(8):
    #     with col:
    #         open_modal = st.button(label='Log-in')
    #         if open_modal:
    #             with modal.container():
    #                 st.markdown('In order to archive the results we suggest you to log-in with your Google account! 🩺')
    #                 st.write('Please log-in with your Google account to proceed:')
    #                 sr=st.button('Log-in with Google', key='google_login')
    #                 if sr:
    #                     #Get the user's Google credentials
    #                     creds = st.get_credentials()
    #                     # Use the credentials to authenticate the user
    #                     auth = google.auth.get_credentials()
    #                     auth.refresh(Request())
    #                     # Now the user is authenticated, proceed with the rest of your app
    #                     st.write('You are now logged in with Google!')
​
​
    st.write("# Welcome to SmartDiag! 👋")
    #set_background('./bgs/.jpg')
​
    # sidebar for navigation, idk how to connect side bar to the pages
    #with st.sidebar:
​
        #selected = option_menu('Diseases Prediction System',
​
                          #['COVID19 Prediction',
                           #'Brain Tumor Prediction'],
                          #icons=['mask','heart'],
                          #menu_icon="cast",
                          #default_index=0,
                          #orientation="horizontal")
    st.markdown(
        """
        Diagnostics Report Analysis is an free app that we created in the hope of
        making the diagnostic process more easily available and maybe ease the pressure on the doctors all around the world!
​
        **👈 Select a diagnostic method from the sidebar** and get an accurate prediction for either COVID19 or Brain tumor.
        ### What's our goal 🎯?
        - Reduce waiting time for patientes and less stress for doctors.
        - Limiting the spread of illness like COVID
​
        ### Sources:
        - Dataset for COVID19 [Covid19 detection using Tensorflow from Chest Xray](https://www.kaggle.com/code/ankan1998/covid19-detection-using-tensorflow-from-chest-xray/notebook)
        - Dataset for Brain tumor's [MRI](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
    """
    """**About Us**

    Welcome to SmartDiag Tech!

    *Our Mission*
    At SmartDiag, we leverage AI to enhance medical diagnostic capabilities.We are driven by a vision where healthcare is empowered by cutting-edge technology, making diagnostics more accurate, accessible, and efficient for everyone.

    *Who We Are*
    Since our establishment in 2023, SmartDiag has been a pioneering force in the healthcare industry. With a commitment to innovation and excellence, we have consistently led the way in advancing diagnostic solutions through cutting-edge technology.
    
    *Meet Our Team*
    Our dedicated team brings a wealth of experience and skills to SmartDiag. Learn more about the individuals driving our mission [add our picture here!!].

    
    *Model Performance*
    "We have implemented the VGG16 model as the cornerstone of our diagnostic approach, utilizing its robust capabilities in analyzing medical images.
    Trained on a dataset comprising 7000 chest X-ray images and 3500 Brain MRI images, our model has demonstrated commendable accuracy in predicting results.

    *Ongoing Efforts and Future Goals*
    "As we continually strive for excellence, our commitment to enhancing performance remains unwavering. We envision expanding our dataset in the near future, a crucial step towards refining our model's predictive accuracy.
    The pursuit of a larger and more diverse dataset aligns with our mission to deliver even more precise diagnostic outcomes.and aslo it's our goal to use more
    information about our patient like gender, historical medical information, or symptoms of disease to have more accurate
    diagnosis and be an assistant for doctor to reduce making mistake in doctor's diagnosis!
    
    *more information about model*
    User-Friendly Explanation:
    "For those interested in the technical details, the VGG16 model, known for its depth and effectiveness, serves as the backbone of our diagnostic process.
    Its architecture allows for intricate feature extraction, enabling accurate predictions from medical images.
    [put image here!!!!]
    """

    )
​
​
    # selected2 = option_menu(None, ["Home", "Covid", "Tasks", 'Settings'],
    # icons=['house', 'cloud-upload', "lungs", 'gear'],
    # menu_icon="cast", default_index=0, orientation="horizontal")
    # selected2
​
​
    # #If Home button is selected
    # if selected2 == "Home":
    #     subprocess.Popen(["streamlit", "run", "main.py"])
    #     os._exit(0)
​
​
    # Get the user's profile picture
    #user_info = service.userinfo().get().execute()
    #profile_picture = user_info['picture']
​
    # Convert the profile picture to a base64 string
    #profile_picture_b64 = base64.b64encode(profile_picture['data'].encode('UTF-8')).decode('UTF-8')
​
    # Display the profile picture in the corner of the app
    #st.image(profile_picture_b64, width=100)
​
    # st.set_page_config(
    #     page_title="Diagnosis at Home",
    #     page_icon="👨‍⚕️",
    # )
​
​
​
​
​
​
​
​
#if __name__ == '__main__':
    #main()