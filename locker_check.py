for locker in range (1, 11):

    if locker == 5:
        print("Locker 5 is skipped.")
        continue

    if locker == 8:
        print("Alert! Threat detected at Locker 8. System Shutting Down!")
        break

    print("Locker", locker, "is safe.")
