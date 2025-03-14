import re

def normalize_phone(phone_number: str) -> str:
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
    
    if cleaned_number.startswith('+'):
        if cleaned_number.startswith('+380'):
            return cleaned_number
        return cleaned_number
    else:
        if cleaned_number.startswith('380'):
            return '+' + cleaned_number
        return '+38' + cleaned_number


# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     " +38(050)123-32-34",
#     " 0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11 ",
# ]
# sanitized_numbers = []

# for num in raw_numbers:
#     sanitized_numbers.append(normalize_phone(num))

# print(sanitized_numbers)
