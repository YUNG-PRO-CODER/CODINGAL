import os

#checks
if os.path.exists('all-notes.txt'):
    print('nah.txt already exists - overwriting')
else:
    print('nah.txt not found - creating now')

#merges
content = ''
with open('tha.txt', 'r') as f:
    content += '--- XPERIMENT ---\n'
    content += f.read() + '\n'
with open('ath.txt', 'r') as f:
    content += '--- I AM MUSIC ---\n'
    content += f.read() + '\n'

#gives output
with open('all-notes.txt', 'w') as out:
    out.write(content)
print('Saved to all-notes.txt')
