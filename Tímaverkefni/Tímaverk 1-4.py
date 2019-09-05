weight_str = input("Weight (kg): ")
height_str = input("Height (cm): ")

weight_float = float(weight_str)
height_float = float(height_str)
height_meter = height_float / 100

bmi = weight_float / height_meter**2

print("BMI is: ", bmi)
