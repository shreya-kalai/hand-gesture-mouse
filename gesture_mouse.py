import cv2
import pyautogui
import time
import hand_tracking
import pyttsx3  # Text-to-speech library
import openai
import os  # Helps interact with the OS
import fitz  # PyMuPDF for extracting text from PDFs
import pytesseract  # OCR for text extraction

# Set the path to Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize last action time
last_action_time = time.time()

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Open Webcam
cap = cv2.VideoCapture(0)

# Flag to control text extraction toggle
extracting = False  

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def explain_text(text_snippet):
    """Uses OpenAI to explain extracted text."""
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Explain this text in simple terms:"},
            {"role": "user", "content": text_snippet}
        ]
    )

    return response.choices[0].message.content

def extract_text_from_screen():
    """Captures a screenshot and extracts text using OCR."""
    screenshot = pyautogui.screenshot()
    extracted_text = pytesseract.image_to_string(screenshot).strip()
    
    if extracted_text:
        print("\nExtracted Text:\n", extracted_text)
        speak("Text extracted successfully.")
        
        explanation = explain_text(extracted_text)
        print("\nAI Explanation:\n", explanation)
        speak(explanation)
    else:
        print("No text detected.")
        speak("No text found.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hand_landmarks = hand_tracking.detect_hands(frame)

    if hand_landmarks:
        fingers_up = hand_tracking.fingers_up(hand_landmarks)
        print(f"Fingers Up: {fingers_up}")

        # Gesture-Based Actions (Throttle with 0.5s delay)
        if time.time() - last_action_time > 0.5:

            if fingers_up == [1, 1, 0, 0, 0]:  # Move Mouse Right
                print("Performing Action: Move Mouse")
                pyautogui.moveRel(30, 0)
                last_action_time = time.time()
                speak("Moving Right")

            elif fingers_up == [0, 1, 1, 0, 0]:  # Click Mouse
                print("Performing Action: Click Mouse")
                pyautogui.click()
                speak("Clicking Mouse")
                last_action_time = time.time()

            elif fingers_up == [1, 1, 0, 0, 1]:  # Scroll Up
                pyautogui.scroll(100)
                speak("Scrolling Up")

            elif fingers_up == [1, 1, 1, 1, 1]:  # Scroll Down
                pyautogui.scroll(-100)
                speak("Scrolling Down")

            elif fingers_up == [0, 1, 1, 1, 0]:  # Right Click
                pyautogui.rightClick()
                last_action_time = time.time()
                speak("Right Click")

            elif fingers_up == [0, 1, 0, 0, 0]:  # Double Click
                pyautogui.doubleClick()
                last_action_time = time.time()
                speak("Double Clicking")

            elif fingers_up == [0, 1, 1, 1, 1]:  # Move Mouse Left
                pyautogui.moveRel(-30, 0)
                last_action_time = time.time()
                speak("Moving Left")

            elif fingers_up == [1, 0, 0, 0, 0]:  # Toggle Text Extraction
                
                extracting = not extracting  # Toggle flag

                if extracting:
                    print("Starting text extraction...")
                    speak("Starting text extraction")
                else:
                    print("Stopping text extraction...")
                    speak("Stopping text extraction")
                
                last_action_time = time.time()

    # If extraction is active, continuously extract text
    if extracting:
        extract_text_from_screen()

    # Show Camera Feed
    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
