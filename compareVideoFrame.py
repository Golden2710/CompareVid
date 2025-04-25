import cv2
import numpy as np

def compare_videos_frame_by_frame(video1_path, video2_path):
    cap1 = cv2.VideoCapture(video1_path)
    cap2 = cv2.VideoCapture(video2_path)
    
    frame_count = 0
    diff_count = 0
    
    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        
        if not ret1 or not ret2:
            break
            
        # Tính toán sự khác biệt giữa các frame
        difference = cv2.absdiff(frame1, frame2)
        non_zero = np.count_nonzero(difference)
        
        if non_zero > 0:
            diff_count += 1
            diff_percent = non_zero / (frame1.size) * 100
            print(f"Frame {frame_count} khác nhau: {diff_percent:.2f}%")
        
        frame_count += 1
    
    cap1.release()
    cap2.release()
    
    if diff_count == 0:
        print("Tất cả frame giống hệt nhau")
    else:
        print(f"{diff_count}/{frame_count} frame có sự khác biệt")

compare_videos_frame_by_frame('output_video.mp4', 'reconstructed_video2.mp4')
