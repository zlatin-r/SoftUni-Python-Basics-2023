time_period = int(input())

doctors = 7
treated_patients = 0
untried_patients = 0

for day in range(1, time_period + 1):
    patient = int(input())
    if day % 3 == 0:
        if untried_patients > treated_patients:
            doctors += 1
    if patient <= doctors:
        treated_patients += patient
    elif patient > doctors:
        untried_patients += patient - doctors
        treated_patients += doctors

print(f"Treated patients: {treated_patients}.\n"
      f"Untreated patients: {untried_patients}.")
