def berakna_total(varor, discount_code=None):
    discount = 0.0
    if discount_code == 'RABATT10':
        discount = 0.10
    total = 0
    for namn, pris, momssats in varor:
        pris_efter_rabatt = pris * (1 - discount)
        total += pris_efter_rabatt * (1 + momssats)
    return round(total, 2)
