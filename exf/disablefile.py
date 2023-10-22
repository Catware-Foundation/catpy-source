handle = ReadFF(parameters_)
handle = handle.split("\n")
handle = '#' + "\n#".join(handle) + f'\n\nOutput("File «{parameters_}» is disabled by exf/disablefile.py. Hi from Catware👋🏻")' 
writeTo(handle, parameters_)
Output('disable successfull')
