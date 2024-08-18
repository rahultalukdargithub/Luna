# 🌙 LUNA: AI-Powered IoT Personal Tutor

LUNA is an innovative AI-driven IoT system designed to act as a personal tutor for students. With an intuitive interface, LUNA allows students to ask questions across various subjects, adhering to strict content guidelines to ensure a safe and educational experience.

## 🚀 How It Works

LUNA is built on a cutting-edge NVIDIA-powered AI system, tailored specifically for handling educational queries.

1. **Question Input** 📝  
   Students enter their questions into LUNA’s user-friendly interface.

2. **Secure Communication** 🔒  
   The query is securely sent to our backend server using a WebSocket-based peer-to-peer (P2P) connection over WiFi, ensuring fast and reliable communication.

   ![WebSocket](https://img.shields.io/badge/WebSocket-000000?style=flat-square&logo=websocket) 
   ![WiFi](https://img.shields.io/badge/WiFi-000000?style=flat-square&logo=wifi)

3. **AI-Powered Response** 🤖  
   LUNA leverages the "llama3-8b-instruct" model, which has been carefully chosen for its ability to understand and respond accurately to a wide range of educational queries.

   ![NVIDIA](https://img.shields.io/badge/NVIDIA-AI-76B900?style=flat-square&logo=nvidia) 
   ![llama](https://img.shields.io/badge/llama3--8b-instruct-000000?style=flat-square&logo=data:image/svg+xml;base64,...) 
   ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python)

4. **Speech Recognition** 🎤  
   LUNA uses the Python SpeechRecognition module for processing spoken input.

   ![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-Python-3776AB?style=flat-square&logo=python)

5. **Text-to-Speech** 🔊  
   Deepgram is used to convert text to natural-sounding speech responses.

   ![Deepgram](https://img.shields.io/badge/Deepgram-Text_to_Speech-000000?style=flat-square&logo=deepgram)

6. **Content Safety** 🔍  
   Rigorous prompt engineering ensures that the responses are safe and appropriate for students.

   ![Prompt Engineering](https://img.shields.io/badge/Prompt_Engineering-FFD700?style=flat-square&logo=ai)

### 🌐 Current & Future Development

- **WebSocket P2P**: Currently, LUNA operates using WebSocket-based P2P connections for efficient communication.
- **MQTT Transition**: We plan to transition to the MQTT protocol for more efficient data packet transmission.
- **Advanced Capabilities**: We aim to integrate Retrieval-Augmented Generation (RAG) with LangChain to enhance memory and context understanding, making responses even more accurate and relevant.

   ![MQTT](https://img.shields.io/badge/MQTT-0082C9?style=flat-square&logo=mqtt) 
   ![LangChain](https://img.shields.io/badge/LangChain-RAG-FF0000?style=flat-square&logo=ai)

## 🌟 Future Vision

While LUNA’s primary focus is education, its underlying technology is versatile and adaptable to various other fields, expanding its potential use beyond just tutoring.
