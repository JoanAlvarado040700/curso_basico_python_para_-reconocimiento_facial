
from cv2 import CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY, RETR_LIST, THRESH_BINARY, cv2

#funciones
imagen = cv2.imread('D:/Proyectos python/ejercicio_monedas/monedascontorno/contorno.jpg')
gris = cv2.cvtColor(imagen,COLOR_BGR2GRAY)
_,umbral = cv2.threshold(gris,100,255,THRESH_BINARY) 
contorno, jerarquia = cv2.findContours(umbral,RETR_LIST,CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(255, 255, 255),2)


#Mostrar en pantalla
#cv2.imshow('Esta es la pantalla',gris)  #imagen escalado a grises
#cv2.imshow('Imagen umbreal',umbral)     #Imagen aplicando el umbral
cv2.imshow("imagen original",imagen)    #imagen original


cv2.waitKey(0)
cv2.destroyAllWindows()
