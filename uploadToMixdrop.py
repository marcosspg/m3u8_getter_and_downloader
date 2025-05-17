# https://github.com/odysseusmax/uploads
import asyncio

import aiohttp

upload_url = "https://ul.mixdrop.co/api"
email = ""
key = ""

async def upload(path:str):
  async with aiohttp.ClientSession() as session:
    file_to_upload = path
    data = {
      'file': open(file_to_upload, 'rb'),
      'email': email,
      'key': key
    }
    r = await session.post(upload_url, data=data)
    return await r.json();
      

