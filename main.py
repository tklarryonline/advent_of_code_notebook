import importlib

if __name__ == '__main__':
    for day in range(25):
        try:
            day_module = importlib.import_module(f'aoc.day{day:02}')

            print(f'# Day {day:02}')
            getattr(day_module, 'run')()
        except ModuleNotFoundError:
            continue
