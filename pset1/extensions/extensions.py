fn = input("File name: ")

fn = fn.strip().lower()
ext = fn[-3:]
ext4 = fn[-4:]

if ext4 == "jpeg" or ext == "jpg":
    out = "image/jpeg"
elif ext == "gif":
    out = "image/gif"
elif ext == "png":
    out = "image/png"
elif ext == "pdf":
    out = "application/pdf"
elif ext == "txt":
    out = "text/plain"
elif ext == "zip":
    out = "application/zip"
else:
    out = "application/octet-stream"

print(out)
