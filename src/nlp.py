import os
import moviepy.editor as mp
import speech_recognition as sr
import csv
import cv2
from deepface import DeepFace

file_path = os.path.dirname(__file__)

def extract_audio(video_path, audio_output_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_output_path)
    print("Áudio extraído:", audio_output_path)
    return video

def detect_emotions_in_video(video_path, interval):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval)
    current_frame = 0

    emotion_intervals = []

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if current_frame % frame_interval == 0:
            faces = face_cascade.detectMultiScale(
                cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                face_roi = frame[y:y + h, x:x + w]
                emotion_result = DeepFace.analyze(
                    face_roi, actions=["emotion"], enforce_detection=False
                )

                if isinstance(emotion_result, list):
                    emotion_result = emotion_result[0]

                dominant_emotion = emotion_result.get("dominant_emotion", "Desconhecido")
                emotion_details = emotion_result.get("emotion", {})

                emotion_intervals.append({
                    'time': current_frame / fps,
                    'dominant_emotion': dominant_emotion,
                    'emotion_details': emotion_details
                })

                print(f"Frame {current_frame / fps:.2f} segundos: {dominant_emotion} - {emotion_details}")

        current_frame += 1

    cap.release()
    return emotion_intervals

def transcribe_audio_in_intervals(audio_path, recognizer, interval, duration, csv_writer):
    for start in range(0, duration, interval):
        with sr.AudioFile(audio_path) as source:
            audio_part = recognizer.record(source, offset=start, duration=interval)

            try:
                text = recognizer.recognize_google(audio_part, language='pt-BR')
                print(f"Transcrição ({start}-{start + interval} segundos): {text}")
            except sr.UnknownValueError:
                text = "Não foi possível transcrever"
            except sr.RequestError as e:
                text = f"Erro no reconhecimento: {e}"

        csv_writer.writerow([f"{start}-{start + interval} segundos", text])

def save_combined_data(emotion_intervals, csv_writer):
    for interval in emotion_intervals:
        time = interval['time']
        emotion = interval['dominant_emotion']
        details = ", ".join(f"{k}: {v:.2f}%" for k, v in interval['emotion_details'].items())

        print(f"Emoções ({time:.2f} segundos): {emotion} - {details}")
        csv_writer.writerow([f"{time} segundos", emotion, details])

def main():
    video_path = os.path.join(file_path, "../videos/entrevista.mp4")
    audio_path = os.path.join(file_path, "../videos/extracted_audio.wav")

    video = extract_audio(video_path, audio_path)
    duration = int(video.audio.duration)

    recognizer = sr.Recognizer()

    emotion_intervals = detect_emotions_in_video(video_path, 30)

    csv_directory = os.path.join(file_path, "../data/")
    csv_file_path = os.path.join(csv_directory, "transcription_and_emotions.csv")

    if not os.path.exists(csv_directory):
        os.makedirs(csv_directory)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Intervalo", "Transcrição", "Emoção dominante", "Detalhes das emoções"])

        transcribe_audio_in_intervals(audio_path, recognizer, 30, duration, csv_writer)

        save_combined_data(emotion_intervals, csv_writer)

if __name__ == "__main__":
    main()
