# Open a file to read 
file = open("han.txt", "r+", encoding="utf-8")
text = file.read()
print(text)
file.close()

# Open a file to append
file = open("han.txt", "a+")
file.write (" Introduction to Artifical Intelligence");
file.close()
file = open("han.txt", "r+")
string = file.read();
print(string)
file.close()

# File Position
fo = open("han.txt", "r+")
str = fo.read(10);
print("ReadSting: ", str)
# Check current position
position = fo.tell();
print("currentposition:",position)
position = fo.seek(0,0);
str = fo.read(10);
print("Again Read String: ",str)
fo.close()

# Rename File
import os
os.rename("han.txt","hanzala.txt")

# Remove File
os.remove("hanzala.txt")