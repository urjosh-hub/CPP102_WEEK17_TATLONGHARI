def get_initial_readings():
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def add_reading(readings):
    text = input("Enter new reading: ")
    
    if len(text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
        return
  
    if not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
        return
           
    value = int(text)
    if value < 0 or value > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return
        
    readings.append(value)
    print("\nReading added successfully.")


def classify_reading(reading, warning_limit=59, critical_limit=79):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    total = 0
    for reading in readings:
        total += reading
    return total


def compute_average(readings):
    if len(readings) == 0:
        return 0.0
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    if len(readings) == 0:
        return 0
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    if len(readings) == 0:
        return 0
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, category):
    count = 0
    for reading in readings:
        if classify_reading(reading) == category:
            count += 1
    return count


def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED SYSTEM OVERHEATING"
    elif warning_count >= 1:
        return "WARNING HEAVY WORK LOAD"
    else:
        return "NORMAL LIGHT WORKLOAD"


def display_readings(readings):
    print("\nCURRENT READINGS")
    print("----------------")
    index = 1
    for reading in readings:
        print(f"Reading {index}: {reading} °C")
        index += 1


def display_classifications(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(f"{reading} °C -> {classify_reading(reading)}")


def display_summary(readings):
    total_elements = len(readings)
    if total_elements == 0:
        print("\nNo database tracking metrics context currently stored.")
        return

    total_sum = compute_total(readings)
    avg_temp = compute_average(readings)
    min_temp = find_minimum(readings)
    max_temp = find_maximum(readings)
    normal_c = count_category(readings, "NORMAL")
    warning_c = count_category(readings, "WARNING")
    critical_c = count_category(readings, "CRITICAL")
    normal_pct = (normal_c / total_elements) * 100
    warning_pct = (warning_c / total_elements) * 100
    critical_pct = (critical_c / total_elements) * 100
    status = determine_overall_status(warning_c, critical_c)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {total_elements}")
    print(f"Total of readings   : {total_sum}")
    print(f"Average temperature : {avg_temp:.2f} °C")
    print(f"Minimum temperature : {min_temp} °C")
    print(f"Maximum temperature : {max_temp} °C")
    print("")
    print(f"NORMAL   : {normal_c} ({normal_pct:.2f}%)")
    print(f"WARNING  : {warning_c} ({warning_pct:.2f}%)")
    print(f"CRITICAL : {critical_c} ({critical_pct:.2f}%)")
    print("")
    print(f"Overall Status: {status}")


def display_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    readings = get_initial_readings()
    
    while True:
        display_menu()
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            display_classifications(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
