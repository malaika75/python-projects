class Temperature:
    @staticmethod
    def converter(c):
        return (c * 9/5)  + 32
    

convert1 = Temperature.converter(20)
print(f"farenheit temperature is {convert1}")