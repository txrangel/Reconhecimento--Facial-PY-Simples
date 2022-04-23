import cv2

xml_haar_cascade = 'haarcascade_frontalface_alt2.xml'


# Pegando o classificador de faces
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

#Iniciado a webcam
capture = cv2.VideoCapture(0)

#Decidindo o tamanho do video
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#loop para detectar o video
while not cv2.waitKey(20) & 0xFF == ord("a"):
    #captura o video colorido
    ret, frame_colorido = capture.read()

    #transforma o video colorido em escala de cinza
    frame_cinza = cv2.cvtColor(frame_colorido, cv2.COLOR_BGR2GRAY)

    #detecta a face usando o video em escala de cinza
    faces = faceClassifier.detectMultiScale(frame_cinza)

    #cria o quadrado em volta da face
    for x, y, w, h in faces:
        cv2.rectangle(frame_colorido, (x, y), (x+w,y+h), (0,255,0), 2)

    #mostra o video na tela
    cv2.imshow('Colorido', frame_colorido)