# Fungsi untuk mengevaluasi kinerja siswa berdasarkan persentase 
def evaluate_performance(percentage):
    if percentage >=90:
        print("Excellent performance")
    elif percentage >=80: 
        print("very good performance")
    elif percentage >=70:
        print("Good performance")
    elif percentage >=60:
        print("Avarage performance")
    else:  
        print("Below avarage performance")

# Example usage:
percentage = float(input("enter the student's percentage :"))
Result = evaluate_performance(percentage)
print(Result)
