# Synchronous, tasks are performed one at a time in the order they are called,
# Each task must finish before the next one can begin.

# Asynchronous, different tasks can start process and finish in overlapping periods of time.

# For example, imagine a task that submits many HTTP requests.
# In the synchronous World, these HTTP requests must be completed one at a time
# In the asynchronous World, each request can start and be set aside while waiting for a response.
# During this waiting period different tasks can step forward and use the Computing resources.
# This nonlinear approach saves one of the most valuables resources around, time.

# A subroutine is a block of code that can be called as needed,
# When a subroutine is called, control of the program is transferred to that subroutine.
# When its work is done control is returned back to the main program and execution continues from where it left off.
# Subroutine cannot be paused and resumed, they run until done.

# A coroutine is a special kind of function that can have its executions paused and resumed.
# This is possible because they maintain their state between pauses.
# Coroutine are perfect for tasks that need to wait for something (Hello I/O Operations, DB Queries, HTTP Requests)

import time
import asyncio


async def brewcoffee():
    print("Start brewcoffee()")
    await asyncio.sleep(3)
    print("End brewcoffee()")
    return "Coffee ready"


async def toastbagel():
    print("Start toastbagel()")
    await asyncio.sleep(2)
    print("End toastbagel()")
    return "Toastbagel ready"


async def main():
    start_time = time.time()

    batch = asyncio.gather(brewcoffee(), toastbagel())  # Coroutine
    result_coffee, result_bagel = await batch  # Return values of the coroutine
    # coffee_task = asyncio.create_task(brewcoffee())
    # toast_task = asyncio.create_task(toastbagel())
    #
    # result_coffee = await coffee_task
    # result_bagel = await toast_task

    end_time = time.time()
    elasped_time = end_time - start_time

    print(f"Result of brewcoffee is: {result_coffee}")
    print(f"Result of toastbagel is: {result_bagel}")
    print(f"Total execution time: {elasped_time:.2} seconds")


if __name__ == "__main__":
    asyncio.run(main())

# Any function that has an await keyword must be declared async.
