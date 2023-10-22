#
# -*- coding: utf-8 -*-
#
# CatPkg - CatABMS Packaging System
#

try:
    params = ReadFF('exf/parameters.txt').split(' ')
except:
    Output("catpkg: error: can't find parameters")
try:
    repos = ReadFF('exf/catpkg_cache/repolist.txt').split('\n')
except:
    Output("catpkg: error: CatPkg can't find RepoList")

delete = []
repos2 = []
for xx in repos:
    if xx.startswith('catrep '):
        try:
            s = Get(xx[7:] + 'verify')
            if s != 'Catware Server OK':
                FailMsg(xx + ": Обнаружено неверное зеркало!!! Удаляю ")
                delete.append(xx)
            else:
                repos2.append(xx[7:])
        except Exception as e:
            Output('CatPkg: error: ' + str(e))

hd = False
codes = []
if params[0] == '-install':
    try:
        for xx in repos2:
            if params[1] + '.py' not in os.listdir("commands"):
                try:
                    app = Get(xx + 'package/' + params[1])
                    if app != 'not found':
                        codes.append(app)
                        Output('Пакет найден: зеркало ' + xx)
                    else:
                        Output('Пакет не найден: зеркало ' + xx)
                except Exception as e:
                    Output('cpkg: error: ' + str(e))
            else:
                ch = input('Пакет ' + params[1] + ' уже установлен. Вы желаете проверить обновления / переустановить пакет?\n[Y/N]: ')
                if ch.lower() == 'y':
                    try:
                        app = Get(xx + 'package/' + params[1])
                        if app != 'not found':
                            codes.append(app)
                            Output('Пакет найден: зеркало ' + xx)
                        else:
                            Output('Пакет не найден: зеркало ' + xx)
                    except Exception as e:
                        Output('cpkg: error: ' + str(e))
                else:
                    Output('Ладно.')
        if codes != []:
            for xx in codes:
                Output('Установка пакета...')
                writeTo(xx, 'commands/' + params[1] + '.py')
    except:
        Output('catpkg: error: нет зеркал')
        
try:
    for xx in delete:
        repos = repos.remove(xx)
    writeTo('\n'.join(repos), 'exf/catpkg_cache/repolist.txt') 
except Exception as e:
    Output('catpkg: error:' + str(e))
