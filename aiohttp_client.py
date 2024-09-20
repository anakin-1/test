import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # print(data)
                return data
            else:
                print(f"Failed to fetch data: {response.status}")
