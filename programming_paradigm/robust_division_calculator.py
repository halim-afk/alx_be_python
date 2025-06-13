def safe_divide(numerator, denominator):
    try:
        # محاولة تنفيذ القسمة
        result = float(numerator) / float(denominator) 
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        # معالجة خطأ القسمة على صفر
        print("Error: Cannot divide by zero.")

    except ValueError:
        # معالجة خطأ إدخال غير رقمي
        print("Error: Please enter numeric values only.")


    