import speedtest


while True:
    test = speedtest.Speedtest()

    down = test.download()
    rsDown = round(down)
    fDown = int(rsDown / 1e+6)

    upload = test.upload()
    rsUp = round(upload)
    fUp = int(rsUp / 1e+6)
    print(f'Download: {fDown} mb/s')
    print(f'Upload: {fUp} mb/s')