def sum_of_elements(sum_of_elements, exclude_negative=False):
    first_list = sum_of_elements.split(" ")
    user_question = input("Uzum eq bacarel bacasakan arjeqnery: ")
    end_sum = 0
    if user_question == "no":
        exclude_negative = True
    if exclude_negative == False:
        for i in first_list:
            if int(i) > 0:
                end_sum += int(i)
    else:
        for i in first_list:
            end_sum += int(i)
    print(end_sum)
    return end_sum
