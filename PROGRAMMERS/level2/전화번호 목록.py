def solution(phone_book):
    phone = {}
    for phone_number in phone_book:
        phone[phone_number] = 1

    for num in phone_book:
        temp = ''
        for i in num:
            temp += i
            if temp in phone and temp != num:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
