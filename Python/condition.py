is_vip = True
loyality_score = 82
purchase_amount = 99
is_matinee = False
is_restricted = False
chacha_vidhayak_hai = True

if chacha_vidhayak_hai or ((is_vip or loyality_score>=80) and (purchase_amount>=100 or is_matinee) and not is_restricted) :
    print("You can get a VIP ticket")
else:
    print("You can't get the VIP ticket")