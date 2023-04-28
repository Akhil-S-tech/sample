list_1_to_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

list_for_tens = ['', '', 'Twenty', 'thirty',
                 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
num = int(input("Enter a Number: "))
output = ''
if num == 0:
    output = 'zero'
elif num <= 19:
    output = list_1_to_19[num]
elif num <= 99:
    output = list_for_tens[num//10] + ' '+list_1_to_19[num % 10]
elif num <= 999:
    output = list_1_to_19[num//100] + ' hundred and ' + \
        list_for_tens[(num % 100)//10] + ' ' + list_1_to_19[num % 10]
else:
    output = 'Invaild value'
print(output)
