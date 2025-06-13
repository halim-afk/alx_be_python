def safe_divide(numerator, denominator):
    try:
        # محاولة تنفيذ القسمة
        result = numerator / denominator
        print(f"The result of the division is {result:.1f}")
        return "Successful division."
    except ZeroDivisionError:
        # معالجة خطأ القسمة على صفر
        print("Error: Cannot divide by zero.")
        return "Division failed."
    except ValueError:
        # معالجة خطأ إدخال غير رقمي
        print("Error: Please enter numeric values only.")
        return "Division failed."
    except Exception as e:
        # معالجة أي أخطاء غير متوقعة
        print(f"An unexpected error occurred: {e}")
        return "Division failed."

# اختبار الدالة
print(safe_divide(6, 1))
