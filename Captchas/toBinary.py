def toBinary(cptchimage):

    import cv2
    import PIL
    import numpy as np

    img = cptchimage

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
    blackAndWhiteImage = ~blackAndWhiteImage

    nb_blobs, im_with_separated_blobs, stats, _ = cv2.connectedComponentsWithStats(blackAndWhiteImage)
    sizes = stats[:, -1]
    nb_blobs -= 1

    for blob in range(nb_blobs):
        if sizes[blob] <= 200:
            blackAndWhiteImage[im_with_separated_blobs == blob] = 0


    #blackAndWhiteImage = cv2.imwrite("binaryCap35.png",blackAndWhiteImage)

    return blackAndWhiteImage


