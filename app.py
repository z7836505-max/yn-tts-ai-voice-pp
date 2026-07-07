import streamlit as st
from elevenlabs import generate, save, set_api_key

# Secrets ထဲက API Key ကို ခေါ်သုံးခြင်း
try:
    api_key = st.secrets["ELEVENLABS_API_KEY"]
    set_api_key(api_key)
except:
    st.error("API Key မတွေ့ရှိပါ။ Secrets ထဲတွင် ထည့်သွင်းပေးပါ။")

st.title("AI Voice Generator (Pro)")

text = st.text_area("စာသားရိုက်ထည့်ပါ", placeholder="ဒီမှာ စာရိုက်ပါ...")
voice = st.selectbox("အသံရွေးချယ်ပါ", ["အမျိုးသမီး (Bella)", "အမျိုးသား (Adam)"])

if st.button("အသံဖိုင်ထုတ်မည်"):
    if not text.strip():
        st.warning("ကျေးဇူးပြု၍ စာရိုက်ပေးပါ")
    else:
        # ElevenLabs Voice ID များ
        voice_id = "EXAVITQu4vr4xnSDxMaL" if voice == "အမျိုးသမီး (Bella)" else "pNInz6obpgDQGcFmaJgB"
        
        with st.spinner('အသံဖိုင် ထုတ်နေပါသည်...'):
            try:
                # အသံဖိုင်ထုတ်ခြင်း
                audio = generate(
                    text=text,
                    voice=voice_id,
                    model="eleven_multilingual_v2"
                )
                save(audio, "output.mp3")
                
                # အသံဖွင့်ပြခြင်း
                st.audio("output.mp3")
                
                # ဒေါင်းလုဒ်ခလုတ်
                with open("output.mp3", "rb") as file:
                    st.download_button(
                        label="📥 MP3 ဖိုင် ဒေါင်းလုဒ်ဆွဲရန်",
                        data=file,
                        file_name="AI_Voice.mp3",
                        mime="audio/mp3"
                    )
            except Exception as e:
                st.error(f"အမှားဖြစ်ပေါ်သည်: {e}")
