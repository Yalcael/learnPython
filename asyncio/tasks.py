import asyncio
from asyncio import Task
from datetime import datetime


async def fetch_data(input_date: int, *, delay: int) -> dict:
    print("Fetching data...")

    # Times the code
    start_tine: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_tine: datetime = datetime.now()

    print("Data fetched!")
    return {"input": input_date, "start": f"{start_tine:%H:%M:%S}", "end": f"{end_tine:%H:%M:%S}"}


async def main() -> None:
    task: Task[dict] = asyncio.create_task(fetch_data(5, delay=2))

    try:
        data: dict = await asyncio.wait_for(task, timeout=3)
        print(data)
    except asyncio.TimeoutError:
        print("Task timed out!")


if __name__ == "__main__":
    asyncio.run(main())
