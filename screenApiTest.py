import screenapi

screenapi.create_screen("work","vim") 
screenapi.run_cmd_screen("work","vim","cd ~")
screenapi.run_cmd_screen("work", 0, "vim ")
screenapi.run_cmd_screen("work", 0, "i This really works makes your life easier")


screenapi.create_window("work", "testBench")
screenapi.run_cmd_screen("work", "testBench", "cd ~")


#This creates a  screen name work and two windows named "vim" and "testBench".
#Opens vim editor on the first window and cd to home directory on the both

