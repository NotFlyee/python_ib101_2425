def solve(*coefficients):
    def larger_root(a: float, b: float, c: float, discriminant: float):
        return (-b + discriminant ** 0.5) / (2 * a)

    def smaller_root(a: float, b: float, c: float, discriminant: float):
        return (-b - discriminant ** 0.5) / (2 * a)

    def discriminant(a: float, b: float, c: float):
        return b ** 2 - 4 * a * c

    if not 0 <= len(coefficients) <= 3 or len(coefficients) == 1:
        return []
    if len(coefficients) == 3:
        _discriminant = discriminant(*coefficients)
        smaller = smaller_root(*coefficients, _discriminant)
        larger = larger_root(*coefficients, _discriminant) 
        if _discriminant < 0:
            return []
        return [smaller, larger] if _discriminant > 0 else [smaller]
    elif len(coefficients) == 2:
        b, c = coefficients
        return [-c / b]
    
def main():
    coefficients = [int(i) for i in input().split()]
    print(*solve(*coefficients))
