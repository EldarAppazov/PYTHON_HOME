revenue = int(input('введите сумму выручки фирмы: '))
costs = int(input('введите сумму издержек фирмы: '))
if revenue > costs:
    print('компания вышла на прибыль в', (revenue-costs), 'руб')
    print('рентабельность компании составила', int((revenue-costs)/revenue*100), '%')
    staff = int(input('введите количество сотрудников: '))
    print('прибыль на каждого сотрудника составила', int((revenue-costs)/staff), 'руб')
else:
    print('компания понесла убытки на сумму', abs(revenue - costs), 'руб')