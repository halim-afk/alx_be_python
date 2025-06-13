# تعريف دالة القسمة الآمنة
def safe_divide(numerator, denominator):
    try:
        # محاولة تحويل المُدخلات إلى أعداد عشرية (float)
        numerator = float(numerator)
        denominator = float(denominator)

        # محاولة تنفيذ عملية القسمة
        result = numerator / denominator

        # إرجاع النتيجة بصيغة مناسبة
        return f"The result of the division is {result:.1f}"

    except ZeroDivisionError:
        # إذا حاول المستخدم القسمة على صفر
        return "Error: Cannot divide by zero."

    except ValueError:
        # إذا أدخل المستخدم قيمة غير رقمية
        return "Error: Please enter numeric values only."



    