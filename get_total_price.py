def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    s=0
    for i in data.split('\n')[1:-1]:
        s+=float(i.split(',')[1])
    return s
p=open('fruits.csv')
print(get_total_price(p.read()))
    

    