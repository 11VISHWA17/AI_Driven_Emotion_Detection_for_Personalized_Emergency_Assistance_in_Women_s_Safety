
from app.facial_emotion import detect_facial_emotion
from app.speech_emotion import detect_speech_emotion
from app.fusion_model import detect_distress
from app.alert_system import send_alert

def main():
    print("AI Driven Women Safety System Started")

    face_emotion = detect_facial_emotion()
    print("Facial Emotion:", face_emotion)

    speech_emotion = detect_speech_emotion()

    distress = detect_distress(face_emotion, speech_emotion)

    if distress:
        send_alert()
    else:
        print("User is Safe. No Alert Needed.")

if __name__ == "__main__":
    main()
