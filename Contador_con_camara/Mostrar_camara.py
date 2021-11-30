import cv2 as cv


captura = cv.VideoCapture(0)
if not captura.isOpened():
    print("No se encontro una camara")
    exit()
while True:
    _,Camara = captura.read()
  #  grises = cv.cvtColor(Camara,cv.COLOR_BGR2GRAY)
   # _,umbral = cv.threshold(grises,100,255,cv.THRESH_BINARY)
   # contorno, jerarquia = cv.findContours(umbral,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
   # cv.drawContours(Camara,contorno,-1,(255, 0, 0),1)
    cv.imshow("Camara en vivo",Camara)
    
    if cv.waitKey(1) == ord("q"):
        break
captura.release()
cv.destroyAllWindows()

def suma(n,n2):
    n +n2

suma(19,1)

