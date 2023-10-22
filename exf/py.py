try:
    exec(ReadFF("exf/parameters.txt"))
    print('ok')
except Exception as err:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
