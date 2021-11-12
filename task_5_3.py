tut = input("Введите имена учеников: ")
kla = input("Введите названия классов: ")

tutors = tut.split(' ')
klasses = kla.split(' ')

tln = len(tutors)
kln = len(klasses)

gen = ((tutors[i], "None") if kln <= i < tln and tln > kln else ("None", klasses[i]) if tln <= i < kln and tln < kln else (tutors[i], klasses[i]) for i in range(max(tln, kln)))
print(f'Ученики: {tutors}', '\n', f'Классы: {klasses}', '\n', type(gen), '\n', *gen)

#if tln == kln:
#    for i in range(tln):
#        print((tutors[i], klasses[i]))
#elif tln > kln:
#    for i in range(tln):
#        if i >= kln:
#            print((tutors[i], "None"))
#        else:
#            print((tutors[i], klasses[i]))
#elif kln > tln:
#    for i in range(kln):
#        if i >= tln:
#            print(("None", klasses[i]))
#        else:
#            print((tutors[i], klasses[i]))
