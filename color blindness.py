# для работы кода, понадобиться три модуля: OpenCv, NumPy, Pandas.
# pip install OpenCv
# pip install NumPy
# pip install Pandas

# импортируем необходимые нам библиотеки
import numpy as np # numpy импортируется как np
import pandas as pd # pandas импортируется как pd
import cv2 # OpenCv импортируется как cv2

# выбираем картинку которую будем использовать
img = cv2.imread("C:/Users/evgen/OneDrive/Рабочий стол/evgeniymosk2/photocolors.png")

# теперь нужно научить машину определять цвета с помощью трех цветов К-ный.З-ный.С-ний.
# для этого будем использовать формат RGB в качестве точек данных 
# воспользуемся csv файлом, который я нашел на github
# https://github.com/codebrainz/color-names/blob/master/output/colors.csv
# Метод read_csv помогает программе управлять csv файлами, например читать

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("C:/Users/evgen/OneDrive/Рабочий стол/evgeniymosk2/colors.csv", names=index, header=None)

# для бесперебойно работы приложения обьявляем глобальную переменную
clicked = False
r = g = b = xpos = ypos = 0


# распознавание цвета будет после двойного клика по области картинки, вернется название цвета и значение RGB
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

# эта функция помогает распознать двойной клик мышкой
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# с OpenCV открываем изображение в новом окне
cv2.namedWindow("new color blindness")

# вызываем функцию распознавания двойного клика мышью
cv2.setMouseCallback("new color blindness", mouse_click)

# открываем окно запуска через цикла whil
while(1):
    cv2.imshow("new color blindness",img)
    if (clicked):
   
        # изображение, начальная точка, конечная точка, цвет, толщина. -1 заполняет весь прямоугольник
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        # создаем текстовую строку для отображения (имя цвета и значения RGB)
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        # цвет, толщина, тип линии
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        # на светлом фоне будет черный текст
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    # с помощью клавиши Esc прекращаем работу цикла и закрываем окно
    if cv2.waitKey(Esc) & 0xFF ==27:
        break
cv2.destroyAllWindows()