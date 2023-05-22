def captchaPredict(binary_img):

    import PIL
    import cv2
    import numpy as np

    captcha = binary_img
    captcha[captcha == 255] = 1
    cptY ,cptX = captcha.shape


    integers = {
        0 : [cv2.imread("0.png"),cv2.imread("0-2.png"),cv2.imread("0-3.png"),cv2.imread("0-4.png"),cv2.imread("0-5.png")],
        1 : [cv2.imread("1.png"),cv2.imread("1-2.png"),cv2.imread("1-3.png"),cv2.imread("1-4.png")],
        2 : [cv2.imread("2.png"),cv2.imread("2-2.png"),cv2.imread("2-3.png"),cv2.imread("2-4.png"),cv2.imread("2-5.png"),cv2.imread("2-6.png")],
        3 : [cv2.imread("3.png"),cv2.imread("3-2.png"),cv2.imread("3-3.png"),cv2.imread("3-4.png"),cv2.imread("3-5.png"),cv2.imread("3-6.png"),cv2.imread("3-7.png"),cv2.imread("3-8.png")],
        4 : [cv2.imread("4.png"),cv2.imread("4-2.png"),cv2.imread("4-3.png"),cv2.imread("4-4.png"),cv2.imread("4-5.png"),cv2.imread("4-6.png"),cv2.imread("4-7.png")],
        5 : [cv2.imread("5.png"),cv2.imread("5-2.png")],
        6 : [cv2.imread("6.png"),cv2.imread("6-2.png"),cv2.imread("6-3.png"),cv2.imread("6-4.png"),cv2.imread("6-5.png"),cv2.imread("6-6.png"),cv2.imread("6-7.png")],
        7 : [cv2.imread("7.png"),cv2.imread("7-2.png"),cv2.imread("7-3.png"),cv2.imread("7-4.png"),cv2.imread("7-5.png")],
        8 : [cv2.imread("8.png"),cv2.imread("8-2.png"),cv2.imread("8-3.png"),cv2.imread("8-4.png"),cv2.imread("8-5.png"),cv2.imread("8-6.png"),cv2.imread("8-7.png")],
        9 : [cv2.imread("9.png"),cv2.imread("9-2.png"),cv2.imread("9-3.png"),cv2.imread("9-4.png"),cv2.imread("9-5.png"),cv2.imread("9-6.png"),cv2.imread("9-7.png")],
    }

    #print(integers)
    #Find number of integers that are read from images
    imgCount = 0
    for key in integers:
        for i in range(len(integers[key])):
            imgCount += 1

    #Turn all uint8 data to binary
    for key in integers:
        for i in range(len(integers[key])):
            integers[key][i][integers[key][i] == 255] = 1

    integers.values()
    accPointsLeft = np.zeros((len(integers),10))
    accPointsRight = np.zeros((len(integers),10))

    lcropLx, lcropTy, lcropRx, lcropBy, rcropLx, rcropTy, rcropRx, rcropBy = 0,0,0,0,0,0,0,0

    for key in integers:
        for i in range(len(integers[key])):
            maxAccVal = 0
            img = integers[key][i]
            imgY = len(img)
            imgX = len(img[0])

            for y in range(cptY - imgY):
                for x in range(cptX//2 - imgX):
                    control = captcha[y:imgY + y,x:imgX + x]
                    arr1 = np.array(img)[:,:,0]
                    arr2 = np.array(control)
                    intersection = np.where(arr1 == arr2,arr1 == 1,arr2 == 1)
                    newAccPoint = 100*np.sum(intersection)//(np.sum(arr1))
                    if  newAccPoint > maxAccVal:
                        maxAccVal = newAccPoint
                        lcropLx, lcropTy, lcropRx, lcropBy = x, y, x+imgX, y+imgY
            accPointsLeft[key][i] = maxAccVal



    for key in integers:
        for i in range(len(integers[key])):
            maxAccVal = 0
            img = integers[key][i]
            imgY = len(img)
            imgX = len(img[0])

            for y in range(cptY - imgY):
                for x in range(cptX//2,cptX - imgX):
                    control = captcha[y:imgY + y,x:imgX + x]
                    arr1 = np.array(img)[:,:,0]
                    arr2 = np.array(control)
                    intersection = np.where(arr1 == arr2,arr1 == 1,arr2 == 1)
                    newAccPoint = 100*np.sum(intersection)//(np.sum(arr1))
                    if  newAccPoint > maxAccVal:
                        maxAccVal = newAccPoint
                        rcropLx, rcropTy, rcropRx, rcropBy = x, y, x+imgX, y+imgY
            accPointsRight[key][i] = maxAccVal


    cropLx = np.min([rcropLx,lcropLx])
    cropTy = np.min([rcropTy,lcropTy])
    cropRx = np.max([rcropRx,lcropRx])
    cropBy = np.max([rcropBy,lcropBy])

    #print(cropLx,cropTy,cropRx,cropBy)

    black = np.zeros((cptY ,cptX))
    black[cropTy:cropBy,cropLx:cropRx] = captcha[cropTy:cropBy,cropLx:cropRx]

    captcha = black
    captcha[0:cptY,lcropRx:rcropLx] = 0

    captcha[captcha == 1] = 255

    blackAndWhiteImage = cv2.imwrite("captchatesseract.png",captcha)
    """
    cv2.imshow('Example - Show image in window',captcha)
    cv2.waitKey(0)
    """
    captcha[captcha == 255] = 1

    for key in integers:
        for i in range(len(integers[key])):
            maxAccVal = 0
            img = integers[key][i]
            imgY = len(img)
            imgX = len(img[1])

            for y in range(cptY - imgY):
                for x in range((rcropLx+lcropRx)//2 - imgX):
                    control = captcha[y:imgY + y, x:imgX + x]
                    arr1 = np.array(img)[:,:,0]
                    arr2 = np.array(control)
                    intersection = arr1[np.where(arr1 == arr2)]
                    newAccPoint = 100*np.sum(intersection)//(np.sum(arr1))
                    if newAccPoint > maxAccVal:
                        maxAccVal = newAccPoint
            accPointsLeft[key][i] = maxAccVal

    for key in integers:
        for i in range(len(integers[key])):
            maxAccVal = 0
            img = integers[key][i]
            imgY = len(img)
            imgX = len(img[1])

            for y in range(cptY - imgY):
                for x in range((rcropLx+lcropRx)//2, cptX - imgX):
                    control = captcha[y:imgY + y, x:imgX + x]
                    arr1 = np.array(img)[:,:,0]
                    arr2 = np.array(control)
                    intersection = arr1[np.where(arr1 == arr2)]
                    newAccPoint = 100*np.sum(intersection)//(np.sum(arr1))
                    if newAccPoint > maxAccVal:
                        maxAccVal = newAccPoint
            accPointsRight[key][i] = maxAccVal



    predictL = np.zeros((len(accPointsLeft),2))
    predictR = np.zeros((len(accPointsRight),2))



    for i in range(len(accPointsLeft)):
        predictL[i][0] = np.max(accPointsLeft[i])
        predictL[i][1] = i
        predictR[i][0] = np.max(accPointsRight[i])
        predictR[i][1] = i

    predictL = predictL.astype(np.int64)
    predictR = predictR.astype(np.int64)
    predictL = predictL.tolist()
    predictR = predictR.tolist()



    predict = np.zeros(((len(predictL)*len(predictR)),2))

    count = 0
    for first in range(len(predictL)):
        for second in range(len(predictR)):
            predict[count][0] = predictL[first][0] + predictR[second][0]
            predict[count][1] = str(predictL[first][1]) + str(predictR[second][1])
            count += 1

    def Sort(sub_li):
        return (sorted(sub_li, key=lambda x: x[0]))

    predict = Sort(predict)

    _3predict = [int(predict[len(predict)-1][1]),int(predict[len(predict)-2][1]),int(predict[len(predict)-3][1])]

    return _3predict

