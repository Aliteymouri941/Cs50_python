a = {
    "gif":"image/gif",
     "jpg":"image/jpg",
     "jpeg":"image/jpeg",
     "png":"image/png",
     "pdf":"application/pdf",
     "txt":"text/plain",
     "zip":"application/zip"
     }
b=input("File name:").strip().lower()

if b.rfind(".") != -1:
    index=int(b.rindex(".")) +1
    c = b[index:]
    if c not in a:
        print("application/octet-stream")
    else:
        print(a[c])