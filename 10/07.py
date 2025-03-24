n = int(input())
menu = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
for i in range(n):
    print(menu[i % 5])
