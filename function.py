def my_car(name, model="volvo", color="Red"):
    msg = "{} has a good {} that has a {} color"
    msg = msg.format(model, color, name)
    print(msg)

    my_car('Mick')
