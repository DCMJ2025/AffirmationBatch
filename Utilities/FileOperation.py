import os
import asyncio
import aiofiles
# Function to read a single file asynchronously
async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        contents = await f.read()
    return file_path, contents

# Main function to read all files in the folder
async def read_all_files(folder_path):
    tasks = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            tasks.append(read_file(full_path))

    results = await asyncio.gather(*tasks)
    return results