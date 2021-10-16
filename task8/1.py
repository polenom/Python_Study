import time, os


def plat_roulette():
    os.system('clear')
    import random
    x = random.randrange(1,7)
    print('BYE CRUEL WORLD' if x == 1 else 'YOU\'RE LUCKY')
    print('    ╭───╮')
    print('╭───┤ %s ├───╮' % ('⬤' if x == 1 else'◯'))
    print('| %s ├───┤ %s |' % ('⬤' if x == 6 else '◯','⬤' if x == 2 else '◯'))
    print('├───┤   ├───┤')
    print('| %s ├───┤ %s |' % ('⬤' if x == 5 else '◯', '⬤' if x == 3 else '◯'))
    print('╰───┤ %s ├───╯' %('⬤' if x == 4 else '◯'))
    print('    ╰───╯')
for i in range(10):
    plat_roulette()
    time.sleep(1)
