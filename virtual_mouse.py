import pyautogui

def control_mouse(fingers_up, hand_landmarks):
    if not hand_landmarks or len(hand_landmarks) < 9:  # ✅ Ensure landmarks are valid
        return  # Exit function if no valid hand detected

    screen_width, screen_height = pyautogui.size()

    index_finger_x = hand_landmarks[8].x * screen_width
    index_finger_y = hand_landmarks[8].y * screen_height

    if fingers_up[1] == 1 and fingers_up[2] == 0:  # Moving the mouse
        pyautogui.moveTo(index_finger_x, index_finger_y)

    if fingers_up[1] == 1 and fingers_up[2] == 1:  # Clicking
        pyautogui.click()
