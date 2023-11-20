# import cv2 
# import mediapipe as mp
# import pydirectinput

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# IMAGE_FILES = []
# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#     static_image_mode=True,
#     max_num_hands=2,
#     min_detection_confidence=0.5) as hands:
#     # for idx, file in enumerate(IMAGE_FILES):
#     #     image = cv2.flip(cv2.imread(file), 1)
#     #     #results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     #     print('Handedness:', results.multi_handedness)
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print('ignored')
#             continue

#         image.flags.writeable = False
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = hands.process(image)

#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         height, width, _ = image.shape
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 #print(hand_landmarks.landmark[9].x,  hand_landmarks.landmark[9].y)
#                 pydirectinput.moveTo(int((1 - hand_landmarks.landmark[9].x) * 1920),
#                                      int(hand_landmarks.landmark[9].y * 1080))
#                 if hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and hand_landmarks.landmark[12].y > \
#                     hand_landmarks.landmark[11].y and hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y:
#                     pydirectinput.mouseDown()
#                 else:
#                     pydirectinput.mouseUp()
#                 mp_drawing.draw_landmarks(
#                     image,
#                     hand_landmarks,
#                     mp_hands.HAND_CONNECTIONS,
#                     mp_drawing_styles.get_default_hand_landmarks_style(),
#                     mp_drawing_styles.get_default_hand_connections_style()
#                 )
#         cv2.imshow('mediapipe hands', cv2.flip(image, 1))
#         if cv2.waitKey(5) & 0xFF == 27:
#             break
# cap.release()
import cv2
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print('ignored')
            continue
        
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        height, width, _ = image.shape
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x = int((1 - hand_landmarks.landmark[9].x) * width)
                y = int(hand_landmarks.landmark[9].y * height)
                pyautogui.moveTo(x, y)

                if (hand_landmarks.landmark[8].y > hand_landmarks.landmark[7].y and
                        hand_landmarks.landmark[12].y > hand_landmarks.landmark[11].y and
                        hand_landmarks.landmark[16].y > hand_landmarks.landmark[15].y):
                    pyautogui.mouseDown()
                else:
                    pyautogui.mouseUp()

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
        cv2.imshow('mediapipe hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
