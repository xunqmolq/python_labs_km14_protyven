format_tuple = (37.863, 'Brent', 3, 62.887, 1, 11)
string1 = ("The price of {1} crude oil fell to $ {0} per barrel, setting a {2}-month anti-record. The current price is only {3}% of last year's {1} oil price on the same day ({4}.{5})")
format_string = (
    f"The price of {format_tuple[1]} "
    f"crude oil fell to ${round(format_tuple[0],2)} "
    f"per barrel, setting a {format_tuple[2]}-month anti-record. "
    f"The current price is only {round(format_tuple[3],2)}% of last year's {format_tuple[1]} "
    f"oil price on the same day ({str(format_tuple[4]).zfill(2)}.{format_tuple[5]})"
)
print (format_string)