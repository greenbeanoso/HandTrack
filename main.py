import cv2
import numpy as np
PoinPos = []
# 讀取圖像，並檢查是否成功讀取
INimg = cv2.imread('test.jpg')
if INimg is None:
    print("圖像讀取失敗，請確認檔案路徑是否正確。")
else:
    print("圖像成功讀取！")
trainCount = 0
# 將圖像進行縮放
INimg = cv2.resize(INimg, (0, 0), fx=0.2, fy=0.2)
showPosimg = INimg.copy()
def main():
    def DoSubdivs(Timg, num):
        w = Timg.shape[1]  # 圖像寬度
        h = Timg.shape[0]  # 圖像高度
        Wsize = w // num  # 每個區塊的寬度
        Hsize = h // num  # 每個區塊的高度

        for i in range(0, w, Wsize):
            for j in range(0, h, Hsize):
                
                if (i // Wsize + j // Hsize) % 2 == 0:
                    Timg[j:j+Hsize, i:i+Wsize] = [255, 255, 255]  # 白色區塊
                else:
                    Timg[j:j+Hsize, i:i+Wsize] = [0, 0, 0]  # 黑色區塊

        return Timg
    def brighten(Aimg,Bimg,value=1):
        # 將圖像轉為 int32，防止溢出
        Aimg = Aimg.astype(np.int32)
        Bimg = Bimg.astype(np.int32)

        # 所有通道一起加，然後進行範圍限制
        Aimg += Bimg//value
        Aimg = np.clip(Aimg, 0, 255)

        # 最後轉回 uint8
        return Aimg.astype(np.uint8)
    def Update(img, br, bb, bg, cA, cB,subdivs):
        img_copy = img.copy()

        # 調整顏色通道，使用滑桿返回的值作為比例
        img_copy[:, :, 0] = np.clip(img_copy[:, :, 0] * (1 - bb / 255), 0, 255)  # 藍色通道
        img_copy[:, :, 1] = np.clip(img_copy[:, :, 1] * (1 - bg / 255), 0, 255)  # 綠色通道
        img_copy[:, :, 2] = np.clip(img_copy[:, :, 2] * (1 - br / 255), 0, 255)  # 紅色通道

        # 執行 Canny 邊緣檢測
        edges = cv2.Canny(img_copy, cA, cB)
        
        # 將單通道的 Canny 邊緣圖轉為三通道，以便與原圖像疊加
        edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # 顯示結果圖像
        cv2.imshow('canny', edges)
        cv2.imshow('rgb+canny', brighten(img_copy, edges_colored))
        cv2.imshow('original+canny', brighten(img, edges_colored))
        cv2.imshow('subdivs', brighten(img, DoSubdivs(brighten(img_copy, edges_colored), subdivs),2))
    def TrackUpdate(val):
        br = cv2.getTrackbarPos('R', 'trackbar')
        bg = cv2.getTrackbarPos('G', 'trackbar')
        bb = cv2.getTrackbarPos('B', 'trackbar')
        cA = cv2.getTrackbarPos('CannyA', 'trackbar')
        cB = cv2.getTrackbarPos('CannyB', 'trackbar')
        subdivs = cv2.getTrackbarPos('subdivs', 'trackbar') +1
        Update(INimg, br, bb, bg,cA,cB,subdivs)
    # 創建一個視窗
    cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

    cv2.createTrackbar('R', 'trackbar', 0, 255, TrackUpdate)
    cv2.createTrackbar('G', 'trackbar', 0, 255, TrackUpdate)
    cv2.createTrackbar('B', 'trackbar', 0, 255, TrackUpdate)
    cv2.createTrackbar('CannyA', 'trackbar', 50, 500, TrackUpdate)
    cv2.createTrackbar('CannyB', 'trackbar', 50, 500, TrackUpdate)
    cv2.createTrackbar('subdivs', 'trackbar', 5, 50, TrackUpdate)
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('j'):  
            break
        

    # 銷毀所有視窗
    cv2.destroyAllWindows()

    # def RigTracker(img):
    #     img_copy[:, :,  0] = 
    cv2.imshow("getpos",showPosimg)
    # 定義滑鼠回調函數，參數是事件類型、x座標、y座標、標誌、額外參數
    def click_event(event, x, y, flags, param):
        # 判斷滑鼠事件是否是點擊左鍵
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"點擊位置: ({x}, {y})")  # 輸出座標
            # 在圖像上畫出點擊的點 (畫紅色的小圓)
            PoinPos.append((x, y))
            cv2.circle(showPosimg, (x, y), 3, (0, 0, 255), -1)
            cv2.imshow("getpos", showPosimg)
    cv2.setMouseCallback("getpos", click_event)
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('j'):  
            break
    if len(PoinPos) == 0:
        main()
    RavgColor, GavgColor, BavgColor = 0, 0, 0
    userlist = []
    def inlist(event, x, y, flags, param):
        # 判斷滑鼠事件是否是點擊左鍵
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.destroyWindow("num" + str(i))
    print(PoinPos)
    print(INimg.shape)
    for j in range(len(PoinPos)):
        x, y = PoinPos[j]
        print(INimg[x][y])
        RavgColor += INimg[x][y][2]
        GavgColor += INimg[x][y][1]
        BavgColor += INimg[x][y][0]
    RavgColor /= len(PoinPos)
    GavgColor /= len(PoinPos)
    BavgColor /= len(PoinPos)

    while len(userlist)<=17:
        Chromosomes = []
        AiImg = []
        for i in range(20):
            Chromosomes.append()
            AiImg.append()
            cv2.imshow("num"+str(i), AiImg[i])
            cv2.setMouseCallback("getpos", inlist(i))
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('j'):  
            break
    main()
    
main()