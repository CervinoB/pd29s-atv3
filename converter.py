import cv2
import dlib

# Caminhos dos arquivos
image_path = "marlon.jpg"  # Substitua pelo nome da sua imagem
model_path = "shape_predictor_68_face_landmarks.dat"  # Modelo pré-treinado
output_txt = image_path + ".txt"

# Carregar a imagem
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Carregar o detector de faces e o preditor de landmarks
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_path)

# Detectar faces
faces = detector(gray)

# Processar cada face detectada
with open(output_txt, "w") as file:
    for face in faces:
        # Obter landmarks faciais
        landmarks = predictor(gray, face)

        # Salvar coordenadas no arquivo .txt
        for n in range(0, 68):  # Existem 68 landmarks no modelo
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            file.write(f"{x} {y}\n")

print(f"Coordenadas salvas no arquivo: {output_txt}")