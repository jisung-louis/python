with open("./day05/info.txt", "r") as file :
    for line in file :
        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi :
            result = "과체중"
        elif 18.5 <= bmi :
            result = "정상체중"
        else:
            result = "저체중"
        
        print('\n'.join([
            f"이름: {name}",
            f"몸무게: {weight}",
            f"키: {height}",
            f"BMI: {bmi}",
            f"결과: {result}"
        ]))
        print()