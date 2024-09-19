import logging
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger1demo(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

# Create an empty file
file = open("hello_world.txt", "w")
file.close()

# Open the file in write mode and write "Hello, World!"
with open("hello_world.txt", "w") as file:
    file.write("Hello, World!")

print("File created and text written successfully.")
