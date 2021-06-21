cd D:\Projects\Game\
pyinstaller --noconfirm --onefile --windowed --icon "D:/Projects/Space Blaster/img/spaceship.ico" --name "Space Blaster" --paths "D:/Projects/Space Blaster/img" --paths "D:/Projects/Space Blaster/music" --paths "D:/Projects/Space Blaster/src" --paths "D:/Projects/Space Blaster/fonts" --add-data "D:/Projects/Space Blaster/fonts;fonts/" --add-data "D:/Projects/Space Blaster/img;img/" --add-data "D:/Projects/Space Blaster/music;music/"  "D:/Projects/Space Blaster/Space Blaster.py"

copy .\dist .\
move "Space Blaster.spec" .\dist
rmdir /q /s music,img,fonts,build,dist
mkdir fonts,music,img
copy "D:\Projects\Space Blaster\fonts\" D:\Projects\Game\fonts
copy "D:\Projects\Space Blaster\music\" D:\Projects\Game\music
copy "D:\Projects\Space Blaster\img\" D:\Projects\Game\img
tar -a -c -f ".\..\Space Blaster\GameFiles.zip" *

