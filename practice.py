def greeter(str_tod, str_name):
    greeting_str = (f"Good {str_tod}, {str_name}")
    return greeting_str

def application():
    greeting = greeter("morning", "Claire")
    print(greeting)

    print(greeter("morning", "Claire"))

    print(f"{greeter('morning', 'Claire')} and {greeter('afternoon', 'Pascal')}")

application()