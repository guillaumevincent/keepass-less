def split_entry(entry):
    entries = entry.split(':')
    if len(entries) == 3:
        return entries[0], entries[1], int(entries[2])
    return entries[0], entries[1], 10
