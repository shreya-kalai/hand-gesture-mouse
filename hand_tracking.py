import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def detect_hands(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        return result.multi_hand_landmarks[0]  # Return first hand detected

    return None  # No hand detected

def fingers_up(hand_landmarks):
    if not hand_landmarks:
        return None  # No hand detected

    fingers = [0] * 5  # Initialize all fingers as down

    # Thumb
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
        fingers[0] = 1

    # Other Fingers
    tip_ids = [8, 12, 16, 20]
    for i, tip_id in enumerate(tip_ids):
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            fingers[i + 1] = 1

    return fingers
