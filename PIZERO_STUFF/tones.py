

#python buzzer frequencies

tone = ['cL', 'cLS', 'dL', 'dLS', 'eL', 'fL', 'fLS', 'gL', 'gLS', 'aL', 'aLS', 'bL', 'c', 'cS', 'd', 'dS', 'e', 'f', 'fS', 'g', 'gS', 'a', 'aS', 'b', 'cH', 'cHS', 'dH', 'dHS', 'eH', 'fH', 'fHS', 'gH', 'gHS', 'aH', 'aHS', 'bH']
duration = ['129', '139', '146', '156', '163', '173', '185', '194', '207', '219', '228', '232', '261', '277', '294', '311', '329', '349', '370', '391', '415', '440', '455', '466', '523', '554', '587', '622', '659', '698', '740', '784', '830', '880', '910', '933']
tonePair = [['cL', '129'], ['cLS', '139'], ['dL', '146'], ['dLS', '156'], ['eL', '163'], ['fL', '173'], ['fLS', '185'], ['gL', '194'], ['gLS', '207'], ['aL', '219'], ['aLS', '228'], ['bL', '232'], ['c', '261'], ['cS', '277'], ['d', '294'], ['dS', '311'], ['e', '329'], ['f', '349'], ['fS', '370'], ['g', '391'], ['gS', '415'], ['a', '440'], ['aS', '455'], ['b', '466'], ['cH', '523'], ['cHS', '554'], ['dH', '587'], ['dHS', '622'], ['eH', '659'], ['fH', '698'], ['fHS', '740'], ['gH', '784'], ['gHS', '830'], ['aH', '880'], ['aHS', '910'], ['bH', '933']]

#freq = dict(zip(tone, duration))
freq = dict(tonePair)   #two ways, the same result
print(tonePair)
#print(freq)
