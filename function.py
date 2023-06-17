from re import match, sub


def normalize(f: str) -> str:
    f = sub(r"x([^\d])", r"x1\1", f.lower()).replace('^', '**').replace('y', 'x2').replace('z', 'x3').replace(")(", ")*(")
    f = sub(r"(\d)([a-z])", r"\1*\2", f)
    return f

class Function:
    def __init__(self, func: str) -> None:
        self.formula, self.function = func.split("=")
        self.function = normalize(self.function)


print(normalize("20x1+10x*50-(10y+10X)(10z+10X)^(15+x)"))