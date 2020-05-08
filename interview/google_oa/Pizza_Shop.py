# Pizza Shop https://leetcode.com/discuss/interview-question/356935/
# complexity?
# binary search?
# what if the customer is allowed to buy more than one pizza
def pizza_shop(pizzas, toppings, x):
    price = float('inf')
    # combinations of 0, 1, and 2 toppings
    # toppings = sorted(set([i + j for i in [0] + toppings for j in [0] + toppings]))
    top_combo = [0]
    # 切记: loop的时候不能改变iterator的内容, 以及加toppings[i]要在outer loop
    for i in range(len(toppings)):
        top_combo.append(toppings[i])
        for j in range(i+1, len(toppings)):
            top_combo.append(toppings[i] + toppings[j])
    top_combo = sorted(set(top_combo))
    
    # binary search
    for p in pizzas:
        start, end = 0, len(top_combo) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if p + top_combo[mid] <= x:
                start = mid
            else:
                end = mid
        # start==end or start+1==end
        if start + 1 < len(top_combo) and abs(p + top_combo[start] - x) > abs(p + top_combo[start + 1] - x):
            new_price = p + top_combo[start + 1]
        elif start - 1 >= 0 and abs(p + top_combo[start] - x) > abs(p + top_combo[start - 1] - x):
            new_price = p + top_combo[start - 1]
        else:
            new_price = p + top_combo[start]

        if abs(new_price - x) < abs(price - x):
            price = new_price
        if abs(new_price - x) == abs(price - x):
            price = min(price, new_price)

    return price

if __name__ == "__main__":
    print(pizza_shop([10, 14, 15], [], 13))
    # print(pizza_shop([800, 850, 900], [100, 150], 1000), 1000)
    # print(pizza_shop([850, 900], [200, 250], 1000), 1050)
    # print(pizza_shop([1100, 900], [200], 1000), 900) # prefer 900 (lower) over 1100 (higher)
    # print(pizza_shop([800, 800, 800, 800], [100], 1000), 900) # The customer may not order 2 same toppings to make it 1000. 