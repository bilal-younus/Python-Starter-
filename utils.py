def find_max(lists):
    number = lists[0]
    for i in lists:
        if number < i:
            number = i
    print(number)

