def convert_mileage():
    print("Mileage Converter: KM <-> Miles")
    
    while True:
        try:
            value = float(input("Enter the mileage value: "))
            unit = input("Enter the unit (KM or Miles): ").strip().lower()
            
            if unit == "km":
                converted_value = value * 0.621371
                print(f"{value} KM is approximately {converted_value:.2f} Miles.")
            elif unit == "miles":
                converted_value = value / 0.621371
                print(f"{value} Miles is approximately {converted_value:.2f} KM.")
            else:
                print("Invalid unit. Please enter 'KM' or 'Miles'.")
                continue
            
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    convert_mileage()
