# Package / Module Imports
import aiohttp
import aiofiles
import asyncio
import os

# 1. Choose A Path - You will need to change this to your desired directory:
path = '/Users/jamesaphoenix/Desktop/Imran_And_James/Python_For_SEO/6_downloading_multiple_images/all_images_async_event_loop'

try:
    os.mkdir('/Users/jamesaphoenix/Desktop/Imran_And_James/Python_For_SEO/6_downloading_multiple_images/all_images_async_event_loop')
except FileExistsError as e:
    print('The file path already exists!')

# 2. Changing directory into that specific path:
os.chdir('/Users/jamesaphoenix/Desktop/Imran_And_James/Python_For_SEO/6_downloading_multiple_images/all_images_async_event_loop')


# 3. Reading the URLs from the text file:
with open('images.txt', 'r') as f:
    image_urls = f.read().split('\n')

# 2. Creating the async functions:
async def fetch(session, url):
    async with session.get(url) as resp:
        # 1. Capturing the image file name like we did before:
        url_name = url.split('/')[-1]
        # 2. Only proceed further if the HTTP response is 200 (Ok)
        if resp.status == 200:
            async with aiofiles.open(url_name, mode='wb') as f:
                await f.write(await resp.read())
                await f.close()

async def main(image_urls:list):
    tasks = []
    headers = {
        "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    async with aiohttp.ClientSession(headers=headers) as session:
        for image in image_urls:
            tasks.append(await fetch(session, image))
    data = await asyncio.gather(*tasks)


# 3. Executing all of the asyncio tasks:
try:
    asyncio.run(main(image_urls))
except Exception as e:
    print(e)
