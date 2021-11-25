#Librerias usadas <---------
from cv2 import CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY, RETR_EXTERNAL, GaussianBlur, cv2
import numpy as np

#------------------------------------------------#

#Funciones <------------
vargaus = 3
varkernle = 3
original = cv2.imread("D:/Proyectos python/ejercicio_monedas/monedascontorno/monedas.jpg")
gris = cv2.cvtColor(original,COLOR_BGR2GRAY)
gaus = GaussianBlur(gris,(vargaus,varkernle),0)
cany = cv2.Canny(gaus,60,100)

kernel = np.ones((varkernle,varkernle),np.uint8)

cierre = cv2.morphologyEx(cany,cv2.MORPH_CLOSE,kernel)

contornos,jerarquias = cv2.findContours(cierre,RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
#Imprimir resultados
print("Monedas encontradas: {} ".format(len(contornos)))
#Dibujar contornos 
cv2.drawContours(original,contornos,-1,(181, 56, 34),2)


#Resultados <----------
cv2.imshow("grises",gris) 
cv2.imshow("Modelado Gaus", gaus)
cv2.imshow("Modelado cany", cany)
cv2.imshow("Resultados",original)


cv2.waitKey(0)