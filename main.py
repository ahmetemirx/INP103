def aday_kontrol_et(yas, not_):
    if 20 <= yas <= 50 and not_ > 80:
        return "einstellen"
    else:
        return "abstellen"
aday_1_yas = 25
aday_1_not = 85
aday_2_yas = 17
aday_2_not = 90
aday_3_yas = 30
aday_3_not = 75
print(aday_kontrol_et(aday_1_yas, aday_1_not))  
print(aday_kontrol_et(aday_2_yas, aday_2_not))  
print(aday_kontrol_et(aday_3_yas, aday_3_not))  