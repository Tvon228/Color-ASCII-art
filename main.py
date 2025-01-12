import cv2
import os

# Символы для ASCII-арта
string = " `.,-':<>;+!*/?%&98#"
coef = 255 / (len(string) - 1)

# Проверяем наличие изображения
image_path = r'c:\Users\patsy\AppData\Local\Packages\MicrosoftWindows.Client.Core_cw5n1h2txyewy\TempState\ScreenClip\{32350D84-0BB4-4731-8AD0-E0308DB55EB2}.png'
output_path = 'output/color_ascii_art.html'

if not os.path.exists(image_path):
    raise FileNotFoundError("Изображение не найдено. Проверьте путь.")

# Создаём папку output, если её нет
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Чтение изображения
image = cv2.imread(image_path)
height, width, channels = image.shape

# Преобразуем изображение в оттенки серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Генерация цветного ASCII-арта
with open(output_path, "w", encoding="utf-8") as file:
    # Начало HTML-документа
    file.write("<html><body style='background-color:black; font-family:monospace; white-space:pre; line-height:10px;'>\n")
    
    for y in range(0, height, 8):  # Увеличенный шаг для уменьшения размера арта
        for x in range(0, width, 4):
            # Яркость пикселя для выбора символа
            brightness = gray_image[y, x]
            char = string[len(string) - int(brightness / coef) - 1]

            # Цвет пикселя
            b, g, r = image[y, x]

            # Формируем HTML с цветным символом
            file.write(f"<span style='color:rgb({r},{g},{b});'>{char}</span>")
        file.write("<br>\n")  # Новый ряд
    
    # Конец HTML-документа
    file.write("</body></html>")

print(f"Цветной ASCII-арт сохранён в файл: {output_path}")
