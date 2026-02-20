import streamlit as st
from pytubefix import YouTube
import os


st.set_page_config(page_title="Free Yt Converter No Ads", page_icon="🟥")

st.title("Youtube To Mp3/Mp4 Converter")
st.markdown("Enter A link to convert and download. No api key needed.")

url = st.text_input("Youtube URL:", placeholder="https://www.youtube.com/watch?v=...")
format_type = st.radio("Convert to:", ["MP3 (Audio)", "MP4 (Video)"])

if st.button("Convert & Prepare To Download"):
    if not url:
        st.error("Please Enter A vaild URL")
    else:
        try:   
            with st.spinner("Processing... "):# Might need to add a warning if it takes a while!
                yt = YouTube(url)
                st.image(yt.thumbnail_url, width =300)
                st.subheader(yt.title)
                if format_type == "MP3 (Audio)":
                    stream = yt.streams.get_audio_only()
                    temp_file = stream.download() #
                    base, ext = os.path.splitext(temp_file) #
                    out_file = base + '.mp3' #
                    if os.path.exists(out_file): os.remove(out_file) #
                    os.rename(temp_file, out_file) #
                    mime_type = "audio/mpeg"
                    file_ext = "mp3"
                else:
                    stream = yt.streams.get_highest_resolution()
                    out_file = stream.download()
                    mime_type = "video/mp4"
                    file_ext = "mp4"
                
                with open(out_file, "rb") as f:
                    file_bytes = f.read()
                
                os.remove(out_file) #

                st.success("Ready!")
                st.download_button(
                    label=f"Download {file_ext.upper()}",
                    data=file_bytes,
                    file_name=f"{yt.title}.{file_ext}",
                    mime=mime_type
                )
                    
                    
            
        except Exception as e:
            st.error(f"Something Went Wrong{e}")
st.divider()
st.caption("Made By Connor S | https://github.com/ConnorSawaya/TTS-And-Translator")
