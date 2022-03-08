import ffmpeg

def download(url, dst):
    print("Downloading " + dst)
    stream = ffmpeg.input(url)
    stream = ffmpeg.output(stream, dst)
    ffmpeg.run(stream)

mode = input("Select mode [u] URL [f] File: ")
if (mode == "u"):
    while True:
        url = input("Enter URL [q] Quit: ")

        if (url == "q"):
            break

        dst = input("Enter destination: ")
        download(url, dst)
elif (mode == "f"):
    while True:
        path = input("Enter file path [q] Quit: ")
        if (path == "q"):
            break

        try:
            file = open(path, "r")
            content = file.read()
            file.close()
            
            lines = content.split("\n")
            num = 0
            for line in lines:
                num += 1
                elements = line.split(" ")
                if len(elements) != 2:
                    print("Discarded line " + num)
                    continue

                url = elements[0]
                dst = elements[1]
                download(url, dst)
        except:
            print("File not found")