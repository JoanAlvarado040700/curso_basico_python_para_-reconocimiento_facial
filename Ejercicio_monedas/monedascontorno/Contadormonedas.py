from cv2 import COLOR_BGR2GRAY, Canny, GaussianBlur, cv2, imshow

#Funciones

vargaus = 3
varkernle = 3
original = cv2.imread("D:/Proyectos python/ejercicio_monedas/monedascontorno/monedas.jpg")
gris = cv2.cvtColor(original,COLOR_BGR2GRAY)
gaus = GaussianBlur(gris,(vargaus,varkernle),10)
cany = cv2.Canny(gaus,60,100)



#Resultados <----------

#cv2.imshow("grises",gris) | 
cv2.imshow("Modelado Gaus", gaus)
cv2.imshow("Modelado cany", cany)

cv2.imshow("Original",original)


cv2.waitKey(0)