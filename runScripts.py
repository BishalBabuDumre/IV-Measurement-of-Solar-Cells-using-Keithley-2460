import os
import time

def run_script(script_name):
    try:
        # Run the script
        exit_code = os.system(f'python {script_name}')
        if exit_code == 0:
            print(f"Script {script_name} ran successfully.")
        else:
            print(f"Script {script_name} failed with exit code {exit_code}.")
    except Exception as e:
        print(f"Error running {script_name}: {e}")

run_script('forward.py')
time.sleep(5)
run_script('trigger.py')
print("Forward Trigger Initiated")
time.sleep(20)#Delaying next step by 20 secs.
run_script('dataForward.py')
run_script('reverse.py')
time.sleep(5)
run_script('trigger.py')
print("Reverse Trigger Initiated")
time.sleep(20)
run_script('dataReverse.py')
print("Measurement Complete")
