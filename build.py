import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

executables=[cx_Freeze.Executable("DEV_v0.3.py")]

cx_Freeze.setup(name="Moles_v03",
                options={"build_exe":{"packages":["pygame","os","math","random"],
                                      "include_files":["mole.png","hole.png","stars.png"]}},
                executables=executables)
