import aiofiles
import aiohttp
import asyncio
import zipfile
import os
import shutil
import IP2Location

database = None

async def get_database():
  global database
  if database is None:
    try:
      database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB11.IPV6.BIN"))
    except ValueError as e:
      print("Database doesn't exist. Downloading...")
      await download_database()
      database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB11.IPV6.BIN"))
  return database

async def download_database():
  zip_destination = './temp/data.zip'
  extraction_folder = './temp'
  extracted_file = './temp/IP2LOCATION-LITE-DB11.IPV6.BIN'
  final_destination = './data/IP2LOCATION-LITE-DB11.IPV6.BIN'
  
  if os.path.exists(final_destination):
    await asyncio.to_thread(os.removedirs, extraction_folder)
  os.makedirs(extraction_folder, exist_ok=True)
  await download_zip_file(get_download_url(), zip_destination)
  await unzip_file(zip_destination, extraction_folder)
  await move_file(extracted_file, final_destination)
  await asyncio.to_thread(os.removedirs, extraction_folder)

def get_download_url():
  token = os.getenv("IP2LOCATION_DOWNLOAD_TOKEN")
  file = "DB11LITEBINIPV6"
  return f"https://www.ip2location.com/download/?token={token}&file={file}"

async def download_zip_file(url, destination):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                async with aiofiles.open(destination, 'wb') as f:
                    await f.write(content)
                print(f"Downloaded zip file from {url} to {destination}")
            else:
                print(f"Failed to download zip file from {url}")

async def unzip_file(zip_file_path, extract_folder):
    def extract_sync():
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        print(f"Unzipped {zip_file_path} to {extract_folder}")

    await asyncio.to_thread(extract_sync)
    print("Unzipping completed.")

async def move_file(source_path, destination_path):
    if os.path.isfile(destination_path):
        await asyncio.to_thread(os.remove, destination_path)
    await asyncio.to_thread(shutil.move, source_path, destination_path)
    print(f"Moved {source_path} to {destination_path}")