def compare_videos(file1, file2):
    # Mở file video ở chế độ nhị phân
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        data1 = f1.read()
        data2 = f2.read()

    # So sánh dữ liệu nhị phân
    if data1 == data2:
        print("Hai video giống nhau.")
    else:
        print("Hai video khác nhau.")

video_path_1 = 'output_video.mp4'
video_path_2 = 'reconstructed_video2.mp4'

compare_videos(video_path_1, video_path_2)
