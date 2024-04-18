from datetime import datetime
import asyncio
from asyncio import Future


async def fetch_data(input_date: int, *, delay: int, fails: bool) -> dict:
    print("Fetching data...OwO")
    # Times the code
    start_tine: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_tine: datetime = datetime.now()
    if fails:
        raise Exception("Something went wrong")

    print("Data fetched!")
    return {"input": input_date, "start": f"{start_tine:%H:%M:%S}", "end": f"{end_tine:%H:%M:%S}"}


async def main() -> None:
    # A future represents an eventual result of an asynchronous operation.
    # So just here we know that the results don't exist yet, but they will eventually. We're creating a promise in the future that something will come back.
    tasks: Future = asyncio.gather(
        fetch_data(1, delay=1, fails=False),
        fetch_data(2, delay=2, fails=False),
        fetch_data(3, delay=1, fails=True),
        return_exceptions=True
    )
    
    results: list[dict] = await tasks
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
