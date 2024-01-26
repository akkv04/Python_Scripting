import subprocess
import os

#subprocess.run:- runs normal process, output = result.stdout
result=subprocess.run(['echo','Hello World'],capture_output=True, text=True)
print(f"output is {result.stdout}")
print(f"error code is {result.returncode}")
print(f"error is {result.stderr}")

#shell=True to run the process
result=subprocess.run('ls -lrt',shell=True)

#this will give the output into the console, if we want to use stdout, returncode, error, we have to add
#capture_output=True, text=True as in first case

#Handling Input -- input='' - both the below cases works
#result=subprocess.run(['grep','Python'],input='Hello\nPython\nWorld',capture_output=True,text=True)
result=subprocess.run('grep Python',shell=True, input='Hello\nPython\nWOrld',capture_output=True,text=True)

print(f"grep result is {result.stdout}")
print(f"grep error is {result.returncode}")



#Communicating with Processes:subprocess.Popen()
#subprocess.run - it just runs the process and we will have to wait for it to get executed
#subprocess.Popen - it allows more fine grain handle and we can interact with output
#communicate() is used to communicate with the process

print("executing subprocess.popen example")
process=subprocess.Popen('grep Python',shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE, text=True)
input_text='Hello\n\nWorld'
output,error_code=process.communicate(input=input_text)
print(f"output is {output}")
print(f"error is {error_code}")


#exception handling in subprocess
try:
    subprocess.run(['echo hello'],shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error:", e)


#Handling environment variables
my_env={'ENVIRONMENT_VARIABLE':'env variable'}
process=subprocess.run('echo $ENVIRONMENT_VARIABLE',shell=True, env=my_env, capture_output=True, text=True)
print(process.stdout)

#Redirecting Output/Error:
with open('output.txt','w') as out_file, open('error.txt','w') as error_file:
    result=subprocess.run('echo Hello', shell=True, stdout=out_file, stderr=error_file)

with open('output.txt','r') as out:
    content=out.read()
    print(f"content of output text file is {content}")

#timeout
try:
    result = subprocess.run('sleep 5', shell=True, timeout=3, check=True)
except subprocess.TimeoutExpired as e:
    print("Timeout occurred:", e)
