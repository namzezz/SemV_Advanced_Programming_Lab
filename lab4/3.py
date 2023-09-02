import os

#get all environment variables
env_variables=os.environ

#print all the environment variables
for key,value in env_variables.items():
    print(f"{key}:{value}")