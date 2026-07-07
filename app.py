import streamlit as st
from gtts import gTTS
import os

st.title("AI Voice Generator")

# စာသားရိုက်ရန်နေရာ
text = st.text_area("စာသားရိုက်ထည့်ပါ", placeholder="ဒီမှာ စာရိုက်ပါ...")

# အသံရွေးချယ်ရန် Dropdown (လက်ရှိတွင် မြန်မာဘာသာစကားဖြင့် အသံထွက်မည်)
voice = st.selectbox("အသံအမျိုးအစားရွေးပါ", ["အမျိုးသား (အေးဆေး)", "အမျိုးသမီး (ကြည်လင်)"])

if st.button("အသံဖိုင်ထုတ်မည်"):
    if not text.strip():
        st.warning("ကျေးဇူးပြု၍ စာရိုက်ပေးပါ")
    else:
        # အသံဖိုင်ထုတ်ခြင်း
        tts = gTTS(text=text, lang='my')
        filename = "output.mp3"
        tts.save(filename)
        
        # Website ပေါ်တွင် အသံဖွင့်ပြခြင်း
        st.audio(filename)
        
        # ဒေါင်းလုဒ်ဆွဲရန် ခလုတ်
        with open(filename, "rb") as file:
            st.download_button(
                label="MP3 ဖိုင် ဒေါင်းလုဒ်ဆွဲရန်",
                data=file,
                file_name="AI_Voice.mp3",
                mime="audio/mp3"
            )
