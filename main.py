import numpy as np
import cv2
import time
TECLA_ESC_ASCII = 27

def onChange(value):
    pass

img = cv2.imread("Imagem/imglimiar.jpg", 0)
copyimg = img.copy()

tituloJanela = "Ajuste do limiar"
cv2.namedWindow(tituloJanela)

cv2.createTrackbar("Limiar", tituloJanela, 0, 255, onChange)
inicio_limiar = 0
atualizar_limiar = False
marcador_tempo = 0
while True:
     valor_limiar =  cv2.getTrackbarPos("Limiar", tituloJanela)
     limiar_adp = cv2.adaptiveThreshold(img, valor_limiar, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
     # valor do trackbar foi alterado pelo usuario
     if inicio_limiar != valor_limiar:
         atualizar_limiar = True
         marcador_tempo = time.time()
         inicio_limiar = valor_limiar
    # atualiza o limiar depois de 1 segundo que o usuario mexeu no trackbar
     if atualizar_limiar == True and time.time() - marcador_tempo > 1:
         #atualiza o limiar da imagem
         copyimg = img.copy()

         #altura, largura, canais_de_cor = img.shape

     #para cada informaçao de cor de cada pixel atualiza o limiar

         for y in range(img.shape[0]):
             for x in range(img.shape[1]):
                     copyimg[y][x]= copyimg[y][x] + valor_limiar

         atualizar_limiar = False

     cv2.imshow(tituloJanela, copyimg)

     teclaPressionada = cv2.waitKey(1) & 0xFF
     if teclaPressionada == TECLA_ESC_ASCII:
        break
cv2.destroyAllWindows()



