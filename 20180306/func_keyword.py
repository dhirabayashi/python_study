def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print('**********')


parrot(1000)
parrot(voltage=100, action='VOOM')
parrot(action='VOOM', voltage=100)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#parrot() TypeError: parrot() missing 1 required positional argument: 'voltage'
#parrot(voltage=5.0, 'dead') SyntaxError: positional argument follows keyword argument
#parrot(110, voltage=220) TypeError: parrot() got multiple values for argument 'voltage'
#parrot(actor='John Cleese') TypeError: parrot() got an unexpected keyword argument 'actor'
