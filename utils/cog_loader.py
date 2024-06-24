import os

async def load_cogs(bot):
    base_path = os.path.dirname(os.path.abspath(__file__))
    cogs_path = os.path.join(base_path, '..', 'cogs')
    
    for folder in os.listdir(cogs_path):
        folder_path = os.path.join(cogs_path, folder)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith('.py') and filename != '__init__.py':
                    cog_name = f'cogs.{folder}.{filename[:-3]}'
                    try:
                        await bot.load_extension(cog_name)
                        print(f'Successfully loaded {cog_name}')
                    except Exception as e:
                        print(f'Failed to load {cog_name}: {e}')
