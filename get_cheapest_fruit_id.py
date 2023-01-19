def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    s=[]
    for i in data.split('\n')[1:-1]:
        s.append(float(i.split(',')[1]))
    return max(s)
p=open('fruits.csv')
print(get_cheapest_fruit_id(p.read()))