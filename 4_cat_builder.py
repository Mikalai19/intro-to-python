def cat_builder(name, color, toys):
    output = {
    }
    output["name"] = name
    output["color"] = color
    output["toys"] = toys
    return output


cat1 = cat_builder("Garfield", "golden", ["scratching-post", "yarn"])
print(cat1)
cat2 = cat_builder("Whisker", "rainbow", ["poptarts"])
print(cat2)
