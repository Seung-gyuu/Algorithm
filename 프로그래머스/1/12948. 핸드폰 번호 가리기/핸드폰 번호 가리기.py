def solution(phone_number):
    stars = '*' * (len(phone_number) - 4)
    nums = phone_number[-4:]
    return f'{stars}{nums}'