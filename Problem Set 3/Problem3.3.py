BPM = float(input(f"Enter BPM: "))
div = 60000/BPM
print(f"The length of a quarter note delay in milliseconds for ", BPM, "BPM is ", div, "ms") 