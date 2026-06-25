












# import tempfile
# import whisper
# import streamlit as st
# import os
# import base64
# from pydub import AudioSegment
# import numpy as np
# import hashlib
# import io

# # ---------------------------
# # Streamlit Page Config
# # ---------------------------
# st.set_page_config(page_title="Audio-Translator", layout="wide")

# # --- CSS to push right column to edge ---
# st.markdown(
#     """
#     <style>
#     [data-testid="stHorizontalBlock"] > div:last-child {
#         padding-right: 0rem !important;
#         margin-right: 0rem !important;
#     }
#     audio {
#         width: 100% !important;  /* full-width player */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --- Sidebar ---
# with st.sidebar:
#     logo_path = ("/Users/chintu-05/projects/streamlit_projects/TechOptima_logo.png")
#     if os.path.exists(logo_path):
#         st.image(logo_path, width=280)
#     st.title("🎤 Hindi Audio → English Translator")
#     st.markdown("---")
#     st.info("""
#      Upload Hindi audio
#      Get English transcription instantly
#     """)

# # --- Layout ---
# left_col, right_col = st.columns([3, 1])

# # Initialize session state
# def _ensure_state():
#     defaults = {
#         "current_audio_path": None,
#         "transcription_results": {},
#         "last_file_id": None,
#         "processing_complete": False,
#         "file_content_hash": None,
#     }
#     for k, v in defaults.items():
#         if k not in st.session_state:
#             st.session_state[k] = v

# _ensure_state()

# # -----------------------------------
# # Helpers
# # -----------------------------------
# def get_file_content_hash(uploaded_file):
#     """Get hash based on actual file content"""
#     if uploaded_file is not None:
#         # Reset file pointer to beginning
#         uploaded_file.seek(0)
#         file_bytes = uploaded_file.read()
#         # Reset pointer again for future reads
#         uploaded_file.seek(0)
#         # Create hash from content
#         return hashlib.sha256(file_bytes).hexdigest()
#     return None

# def validate_audio_content(audio_path, min_duration_ms=100):
#     try:
#         if not os.path.exists(audio_path):
#             return False, "Audio file does not exist"
#         if os.path.getsize(audio_path) == 0:
#             return False, "Audio file is empty"
#         audio = AudioSegment.from_file(audio_path)
#         if len(audio) < min_duration_ms:
#             return False, f"Audio too short (less than {min_duration_ms}ms)"
#         audio_data = np.array(audio.get_array_of_samples())
#         if np.all(audio_data == 0):
#             return False, "Audio contains only silence"
#         return True, "Audio is valid"
#     except Exception as e:
#         return False, f"Error validating audio: {str(e)}"

# def split_audio(audio_path, chunk_length_ms=60000):
#     try:
#         is_valid, message = validate_audio_content(audio_path)
#         if not is_valid:
#             st.error(f"Invalid audio file: {message}")
#             return []
        
#         audio = AudioSegment.from_file(audio_path)
#         if len(audio) == 0:
#             st.error("Audio file has no content")
#             return []
        
#         audio = audio.set_frame_rate(16000).set_channels(1)
#         chunks = []
        
#         for i in range(0, len(audio), chunk_length_ms):
#             chunk = audio[i:i + chunk_length_ms]
#             if len(chunk) < 1000:
#                 continue
            
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
#                 try:
#                     chunk.export(
#                         tmp_wav.name,
#                         format="wav",
#                         parameters=["-ar", "16000", "-ac", "1", "-sample_fmt", "s16"]
#                     )
#                     is_valid, _ = validate_audio_content(tmp_wav.name)
#                     if is_valid:
#                         chunks.append(tmp_wav.name)
#                     else:
#                         try:
#                             os.unlink(tmp_wav.name)
#                         except:
#                             pass
#                 except Exception as e:
#                     st.error(f"Error creating audio chunk: {str(e)}")
#                     try:
#                         os.unlink(tmp_wav.name)
#                     except:
#                         pass
        
#         return chunks
#     except Exception as e:
#         st.error(f"Error splitting audio: {str(e)}")
#         return []

# def safe_transcribe(model, audio_path, **kwargs):
#     try:
#         is_valid, message = validate_audio_content(audio_path)
#         if not is_valid:
#             st.error(f"Cannot transcribe: {message}")
#             return None
#         result = model.transcribe(audio_path, **kwargs)
#         return result
#     except Exception as e:
#         st.error(f"Transcription error: {str(e)}")
#         return None

# def cleanup_previous_audio():
#     if st.session_state.current_audio_path and os.path.exists(st.session_state.current_audio_path):
#         try:
#             os.unlink(st.session_state.current_audio_path)
#         except:
#             pass
#     st.session_state.current_audio_path = None

# def cleanup_temp_files():
#     import glob
#     temp_files = glob.glob("/tmp/tmp*.wav")
#     for temp_file in temp_files:
#         try:
#             os.unlink(temp_file)
#         except:
#             pass

# def reset_transcription_state():
#     """Reset all transcription-related state"""
#     st.session_state.transcription_results = {}
#     st.session_state.processing_complete = False

# def process_uploaded_file(uploaded_file):
#     """Process uploaded file and return audio path"""
#     try:
#         # Reset file pointer and read bytes
#         uploaded_file.seek(0)
#         file_bytes = uploaded_file.read()
        
#         if len(file_bytes) == 0:
#             st.error("Uploaded file is empty")
#             return None
        
#         # Create temporary file with original extension
#         orig_suffix = os.path.splitext(uploaded_file.name)[1] or ".bin"
#         with tempfile.NamedTemporaryFile(delete=False, suffix=orig_suffix) as tmp_in:
#             tmp_in.write(file_bytes)
#             tmp_in.flush()
#             src_path = tmp_in.name
        
#         # Convert to WAV format
#         try:
#             original_audio = AudioSegment.from_file(src_path)
#             duration_sec = len(original_audio) / 1000.0
            
#             if duration_sec < 0.1:
#                 st.error("Audio file is too short. Please upload at least 100ms of content.")
#                 os.unlink(src_path)
#                 return None
            
#             # Create WAV file
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
#                 original_audio = original_audio.set_frame_rate(16000).set_channels(1)
#                 original_audio.export(
#                     tmp_wav.name,
#                     format="wav",
#                     parameters=["-ar", "16000", "-ac", "1", "-sample_fmt", "s16"]
#                 )
                
#                 is_valid, message = validate_audio_content(tmp_wav.name)
#                 if is_valid:
#                     # Clean up source file
#                     try:
#                         os.unlink(src_path)
#                     except:
#                         pass
#                     return tmp_wav.name
#                 else:
#                     st.error(f"Converted audio is invalid: {message}")
#                     try:
#                         os.unlink(tmp_wav.name)
#                         os.unlink(src_path)
#                     except:
#                         pass
#                     return None
        
#         except Exception as e:
#             st.error(f"Error processing audio: {str(e)}")
#             try:
#                 os.unlink(src_path)
#             except:
#                 pass
#             return None
            
#     except Exception as e:
#         st.error(f"Error reading uploaded file: {str(e)}")
#         return None

# # -----------------------------------
# # File Upload Section
# # -----------------------------------
# with left_col:
#     st.header("Upload Audio File")
    
#     # File uploader
#     audio_file = st.file_uploader(
#         "Upload a Hindi audio file",
#         type=["mp3", "wav", "m4a", "ogg"],
#         key="audio_uploader"
#     )
    
#     # Process file upload
#     if audio_file is not None:
#         # Get content hash to detect actual file changes
#         current_hash = get_file_content_hash(audio_file)
        
#         # Check if this is a different file
#         is_new_file = current_hash != st.session_state.file_content_hash
        
#         if is_new_file:
#             # Clean up previous state
#             cleanup_previous_audio()
#             reset_transcription_state()
            
#             # Show processing indicator
#             with st.spinner("Processing uploaded audio..."):
#                 audio_path = process_uploaded_file(audio_file)
                
#                 if audio_path:
#                     # Update session state with new file
#                     st.session_state.current_audio_path = audio_path
#                     st.session_state.file_content_hash = current_hash
#                     st.session_state.last_file_id = f"{audio_file.name}_{audio_file.size}_{current_hash[:8]}"
                    
#                     st.success(" Audio loaded successfully!")
#                     st.audio(audio_path, format="audio/wav")
#                 else:
#                     # Failed to process
#                     st.session_state.current_audio_path = None
#                     st.session_state.file_content_hash = None
#                     st.session_state.last_file_id = None
        
#         else:
#             # Same file - show existing results
#             if st.session_state.current_audio_path and os.path.exists(st.session_state.current_audio_path):
#                 st.info("ℹ️ Same file detected. Showing previous results.")
#                 st.audio(st.session_state.current_audio_path, format="audio/wav")
                
#                 # Display cached results if available
#                 if st.session_state.transcription_results:
#                     hindi_text = st.session_state.transcription_results.get("hindi", "")
#                     english_text = st.session_state.transcription_results.get("english", "")
                    
#                     if hindi_text.strip():
#                         st.subheader(" Hindi Transcription")
#                         st.write(hindi_text.strip())
                    
#                     if english_text.strip():
#                         st.subheader(" English Translation")  
#                         st.write(english_text.strip())
    
#     else:
#         # No file uploaded - clear state
#         if st.session_state.current_audio_path:
#             cleanup_previous_audio()
#             reset_transcription_state()
#             st.session_state.file_content_hash = None
#             st.session_state.last_file_id = None

# # -----------------------------------
# # Transcription Section
# # -----------------------------------
# if (st.session_state.current_audio_path and 
#     os.path.exists(st.session_state.current_audio_path) and 
#     not st.session_state.processing_complete):
    
#     status_placeholder = st.empty()
#     status_placeholder.info(" Loading model and preparing transcription...")
    
#     @st.cache_resource
#     def load_whisper_model():
#         try:
#             return whisper.load_model("large-v3")
#         except Exception as e:
#             st.error(f"Error loading Whisper model: {str(e)}")
#             return None
    
#     model = load_whisper_model()
    
#     if model is None:
#         st.error("Failed to load Whisper model. Please try again.")
#     else:
#         try:
#             status_placeholder.info(" Splitting audio into chunks...")
#             chunks = split_audio(st.session_state.current_audio_path, chunk_length_ms=60000)
            
#             if not chunks:
#                 st.error("No valid audio chunks created. Please check your audio file.")
#             else:
#                 hindi_text = ""
#                 english_text = ""
                
#                 for i, chunk_path in enumerate(chunks):
#                     status_placeholder.info(f" Transcribing ...")
                    
#                     # Hindi transcription
#                     result_hi = safe_transcribe(model, chunk_path, language="hi", fp16=False)
#                     if result_hi:
#                         hindi_text += result_hi["text"] + " "
                    
#                     # English translation
#                     result_en = safe_transcribe(model, chunk_path, task="translate", fp16=False)
#                     if result_en:
#                         english_text += result_en["text"] + " "
                    
#                     # Clean up chunk
#                     try:
#                         os.unlink(chunk_path)
#                     except:
#                         pass
                
#                 # Store results and mark as complete
#                 st.session_state.transcription_results = {
#                     "hindi": hindi_text.strip(),
#                     "english": english_text.strip()
#                 }
#                 st.session_state.processing_complete = True
                
#                 status_placeholder.success(" Transcription complete!")
                
#                 # Display results
#                 with left_col:
#                     if hindi_text.strip():
#                         st.subheader(" Hindi Transcription")
#                         st.write(hindi_text.strip())
#                     else:
#                         st.warning("No Hindi transcription generated.")
                    
#                     if english_text.strip():
#                         st.subheader(" English Translation")
#                         st.write(english_text.strip())
#                     else:
#                         st.warning("No English translation generated.")
                        
#         except Exception as e:
#             st.error(f"Error during transcription process: {str(e)}")

# # -----------------------------------
# # Instructions (Right Column)
# # -----------------------------------
# with right_col:
#     st.markdown("###  About The Tool")
#     st.markdown("""
#     This tool transcribes **Hindi audio** into text and
#     provides instant **English translation**.
#     Useful for **education, research, and content creation**.
#     """)
    
#     st.markdown("###  Target Personas")
#     st.markdown("""
#     - Students & Researchers
#     - Professionals
#     - Content Creators
#     - General Users
#     """)
    
#     st.markdown("###  Download Sample Files")
#     sample_zip_path = "./sample audio files.zip"
#     if os.path.exists(sample_zip_path):
#         try:
#             with open(sample_zip_path, "rb") as f:
#                 st.download_button(
#                     label="📥 Download Sample ZIP file",
#                     data=f,
#                     file_name="sample_files.zip",
#                     mime="application/zip",
#                 )
#         except Exception as e:
#             st.error(f"Error loading sample files: {str(e)}")
#     else:
#         st.warning("⚠️ Sample ZIP file not found.")

# # Clean up temporary files on app restart
# cleanup_temp_files()
