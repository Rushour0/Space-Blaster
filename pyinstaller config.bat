copy "D:\Projects\Space Blaster\fonts\" D:\Projects\Game\
copy "D:\Projects\Space Blaster\music\" D:\Projects\Game\
copy "D:\Projects\Space Blaster\img\" D:\Projects\Game\
cd D:\Projects\Game\
pyinstaller --noconfirm --onefile --windowed --icon "D:/Projects/Space Blaster/img/spaceship.ico" --name "Space Blaster" --paths "D:/Projects/Space Blaster/img" --paths "D:/Projects/Space Blaster/music" --paths "D:/Projects/Space Blaster/src" --paths "D:/Projects/Space Blaster/fonts" --add-data "D:/Projects/Space Blaster/fonts;fonts/" --add-data "D:/Projects/Space Blaster/img;img/" --add-data "D:/Projects/Space Blaster/music;music/"  "D:/Projects/Space Blaster/Space Blaster.py"