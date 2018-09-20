class choice_opt:
    a = "a"
    b = "b"
    c = "c"

def print_opt(opt):
    print("options: %s" % opt)

print_opt.choice_opt = choice_opt
