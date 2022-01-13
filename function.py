def my_car(model="volvo", color="Red", name):
    msg = "{} has a good {} that has a {} color"
    msg = msg.format(model, color, name)
    print(msg)

    my_car('Mick')
