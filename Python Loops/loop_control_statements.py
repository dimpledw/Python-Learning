# Advanced For Loop
# Break Statements - It stops the loop immediately 

names = ['John','Maria', '', 'Kumari']
for name in names:
    if name == '':
        print("Empty Value Detected")
        break
    print(f"Name - {name}")

# Continue Statement - It skips one loop cycle without stopping the loop
# Use continue to skip bad or empty data without stopping the whole loop

names = ['John','Maria', '', 'Kumari']
for name in names:
    if name == '':
        continue
    print(f"Name - {name}")

# Pass Statement - It is a placeholder where nothing happens - For now, just keep going and do nothing

names = ['John','Maria', '', 'Kumari']
for name in names:
    if name == '':
        print("Empty Value Detected")
        pass # todo: Handle Empty Value
    print(f"Name - {name}")


