import os

def ratio():
    orig = os.path.getsize('file.txt')
    comp = os.path.getsize('compressed_file.txt')

# print("Original Size :", orig, "bytes")
# print("Compressed Size :", comp, "bytes")
# print("Compression Ratio :", comp/orig)

    return orig,comp