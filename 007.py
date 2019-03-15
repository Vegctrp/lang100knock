from string import Template

def string_template(x,y,z):
    str=Template("$hour時の$targetは$value")
    return str.substitute(hour=x, target=y, value=z)

x=12
y="気温"
z=22.4

print(string_template(x,y,z))