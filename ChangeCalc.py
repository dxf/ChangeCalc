from sys import exit
print('Change Calculator by Dafydd (GitHub: dxf)')
good = input('Insert total: £')
try:
    good = float(good)
except:
    print('Invalid amount!')
    exit()
good = good * 100
given = input('How much money did the customer give you? £')
try:
    given = float(given)
except:
    print('Invalid amount!')
    exit()
given = given * 100
change = given - good
fiftynote = 0
twentynote = 0
tennote = 0
fivenote = 0
twocoin = 0
onecoin = 0
fiftycoin = 0
twentycoin = 0
tencoin = 0
fivecoin = 0
onepcoin = 0
while True:
    change = change - 5000
    if change < 0:
        change = change + 5000
        break
    if change > 0:
        fiftynote += 1
    if change == 0:
        break
while True:
    change = change - 2000
    if change < 0:
        change = change + 2000
        break
    if change > 0:
        twentynote += 1
    if change == 0:
        break
while True:
    change = change - 1000
    if change < 0:
        change = change + 1000
        break
    if change > 0:
        tennote += 1
while True:
    change = change - 500
    if change < 0:
        change = change + 500
        break
    if change > 0:
        fivenote += 1
    if change == 0:
        break
while True:
    change = change - 200
    if change < 0:
        change = change + 200
        break
    if change > 0:
        twocoin += 1
    if change == 0:
        break
while True:
    change = change - 100
    if change < 0:
        change = change + 100
        break
    if change > 0:
        onecoin += 1
    if change == 0:
        break
while True:
    change = change - 50
    if change < 0:
        change = change + 50
        break
    if change > 0:
        fiftycoin += 1
    if change == 0:
        break
while True:
    change = change - 20
    if change < 0:
        change = change + 20
        break
    if change > 0:
        twentycoin += 1
    if change == 0:
        break
while True:
    change = change - 10
    if change < 0:
        change = change + 10
        break
    if change > 0:
        tencoin += 1
    if change == 0:
        break
while True:
    change = change - 5
    if change < 0:
        change = change + 5
        break
    if change > 0:
        fivecoin += 1
    if change == 0:
        break
while True:
    change = change - 1
    if change < 0:
        change = change + 1
        break
    if change > 0:
        onepcoin += 1
    if change == 0:
        break
print(f'Your change: {fiftynote}x £50\n{twentynote}x £20\n{tennote}x £10\n{fivenote}x £5\n{twocoin}x £2\n{onecoin}x £1\n{fiftycoin}x 50p\n{twentycoin}x 20p\n{tencoin}x 10p\n{fivecoin}x 5p\n{onepcoin}x 1p')
