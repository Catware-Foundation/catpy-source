import platform

print("System :", platform.system())
print("Node :", platform.node())
print("Platform :", platform.platform())
print("Processor Architecture :", platform.machine())
print("Python Build :", platform.python_build()[0])
print("Python Compiler :", platform.python_compiler())
print("Python Implementation :", platform.python_implementation())
print("Python Version :", platform.python_version())
print("Release :", platform.release())
print("Version :", platform.uname())