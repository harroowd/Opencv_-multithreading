import cv2
import torch
import time


class CamStream:

    def __init__(self, ip, name):
        self.ip = ip
        self.name = name

    def run_cam(self):
        vs = cv2.VideoCapture(self.ip)
        while True:
            ret, frame = vs.read()
            if ret:
                frame = cv2.resize(frame, (700, 500))
                frame = cv2.flip(frame, 2)
                cv2.imshow(f'{self.name}', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print(f'{self.name} reconnect')
                time.sleep(15)
                vs.release()
                vs = cv2.VideoCapture(self.ip)
        vs.release()
        cv2.destroyAllWindows()

# path
ip1 = 0


cam1 = torch.multiprocessing.Process(target=CamStream(ip1, 'cam1').run_cam)
cam2 = torch.multiprocessing.Process(target=CamStream(ip1, 'cam2').run_cam)
cam3 = torch.multiprocessing.Process(target=CamStream(ip1, 'cam3').run_cam)
cam4 = torch.multiprocessing.Process(target=CamStream(ip1, 'cam4').run_cam)
print("start")
[x.start() for x in [cam1, cam2, cam3, cam4]]
