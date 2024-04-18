from datetime import datetime
import asyncio
from asyncio import Future
import requests
from requests import Response


async def check_status(url: str) -> dict[str, int | str]:
    start_time: datetime = datetime.now()
    response: Response = await asyncio.to_thread(requests.get, url, None)  # This allows us to turn any normal function that is synchronous to an asynchronous function.
    end_time: datetime = datetime.now()

    return {"website": url,
            "status": response.status_code,
            "start_time": f"{start_time:%Y-%m-%d %H:%M:%S}",
            "end_time": f"{end_time:%Y-%m-%d %H:%M:%S}"}


async def main() -> None:
    print("Fetching the results...")
    tasks: Future = asyncio.gather(
        check_status("https://www.google.com"),
        check_status("https://www.yahoo.com"),
        check_status("https://www.facebook.com"),
        check_status("https://www.instagram.com"),
        check_status("https:lol"),
        return_exceptions=True
    )
    results: list[dict] = await tasks
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
