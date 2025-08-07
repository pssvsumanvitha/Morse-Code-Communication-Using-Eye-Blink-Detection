import cv2
import mediapipe as mp
import time

# Morse code dictionary
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C',
    '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

# Variables
morse_code = ''
translated_text = ''
blink_start = None
last_blink = time.time()

# Webcam
cap = cv2.VideoCapture(0)

# Eye aspect ratio function
def get_eye_aspect_ratio(landmarks, w, h):
    left = landmarks[159]
    right = landmarks[145]
    vertical = abs((left.y - right.y) * h)
    return vertical

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            ear = get_eye_aspect_ratio(landmarks.landmark, w, h)

            if ear < 5:  # Eye closed
                if blink_start is None:
                    blink_start = time.time()
            else:
                if blink_start:
                    duration = time.time() - blink_start
                    if duration < 0.4:
                        morse_code += '.'
                    else:
                        morse_code += '-'
                    blink_start = None
                    last_blink = time.time()

    # Detect space between blinks (for translating a character)
    idle = time.time() - last_blink
    if morse_code and idle > 2:
        char = morse_dict.get(morse_code, '?')
        translated_text += char + ' '
        morse_code = ''

    # ---------- DRAW ON SCREEN ----------
    cv2.putText(frame, f"Morse: {morse_code}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f"Text: {translated_text}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Blink Morse Code Translator", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
