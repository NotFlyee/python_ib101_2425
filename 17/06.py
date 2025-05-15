translated_text = None

def translate(text: str):
    global translated_text
    temp = ''
    for char in text:
        if char.lower() not in 'аеёиоуыэюя.!?,:;-()"':
            temp += char
    translated_text = ' '.join(temp.split())


translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
