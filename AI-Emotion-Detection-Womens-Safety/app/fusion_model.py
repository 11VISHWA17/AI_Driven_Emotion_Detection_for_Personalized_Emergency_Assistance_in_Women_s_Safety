
def detect_distress(face_emotion, speech_emotion):
    distress_emotions = ['Fear', 'Angry', 'Sad']

    if face_emotion in distress_emotions or speech_emotion in distress_emotions:
        return True
    return False
