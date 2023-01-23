import os
import glob
import subprocess
#import folder from Desktop

#input_file_type = input('Input file type: ')
output_file_type = 'mp4'

#
# video_list_103ab = ['/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/103AB/Thursday_PM/SC1TK06.mov',


video_list_107ab = ['/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/107AB/Saturday_AM/SC1TK13.mov']

video_list_108ab = ['/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/108AB/Thursday_AM/SC1TK13.mov']

video_list_109ab = ['/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Thursday_PM/SC1TK05.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Thursday_PM/SC1TK06.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Thursday_PM/SC1TK07.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Thursday_PM/SC1TK08.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Friday_AM/SC1TK10.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Friday_PM/SC1TK11.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Friday_PM/SC1TK12.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Friday_PM/SC1TK13.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Saturday_AM/SC1TK15.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Saturday_PM/SC1TK16.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/109AB/Saturday_PM/SC1TK17.mov',
              ]

video_list_201 = ['/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_AM/SC1TK6_1.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_AM/SC1TK6_2.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK08.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK09.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK10_1.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK10_2.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK11_1.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK11_2.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK12_1.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK12_2.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK13_1.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Thursday_PM/SC1TK13_2.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Friday_AM/SC1TK14_1.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Friday_AM/SC1TK14_2.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Friday_AM/SC1TK15_1.mov',
            '/Volumes/HMXArch2/2023/US_Soccer_Coaches_2023/RAW/201/Friday_AM/SC1TK15_2.mov',
              ]

# video_list = ['/Volumes/HMX_store_3/2023/January/Soccer_coaches_meeting_rooms_RAW/Raw_HMXArch1/113C/Thursday_PM/SC1TK4.mov']

#print(video_list[0][-11:-4])

#path = r'/Users/tylermorton/Desktop/video_folder'
#input_files = glob.glob(os.path.join(path, f"*.{input_file_type}"))

#output_files = [os.path.basename(x) for x in glob.glob(f'/Users/tylermorton/Desktop/video_folder/*.{input_file_type}')]

#print(input_files)
#print(output_files[1][0:-4])
#
# x = 0
# for i in video_list_103ab:
#     print(video_list_103ab[x])
#     os.system(f"ffmpeg -i {video_list_103ab[x]} -c:v libx264 -crf 20 -c:a aac -b:a 128k /Volumes/San_1/US_Soccer_Coaches_2023/Renders/103AB/render_{video_list_103ab[x][-10:-4]}.{output_file_type}")
#     x += 1
#
x = 0
for i in video_list_107ab:
    print(video_list_107ab[x])
    os.system(f"ffmpeg -i {video_list_107ab[x]} -c:v libx264 -crf 20 -c:a aac -b:a 128k /Volumes/San_1/US_Soccer_Coaches_2023/Renders/107AB/render_{video_list_107ab[x][-10:-4]}.{output_file_type}")
    x += 1

x = 0
for i in video_list_108ab:
    print(video_list_108ab[x])
    os.system(f"ffmpeg -i {video_list_108ab[x]} -c:v libx264 -crf 20 -c:a aac -b:a 128k /Volumes/San_1/US_Soccer_Coaches_2023/Renders/108AB/render_{video_list_108ab[x][-10:-4]}.{output_file_type}")
    x += 1

x = 0
for i in video_list_109ab:
    print(video_list_109ab[x])
    os.system(f"ffmpeg -i {video_list_109ab[x]} -c:v libx264 -crf 20 -c:a aac -b:a 128k /Volumes/San_1/US_Soccer_Coaches_2023/Renders/109AB/render_{video_list_109ab[x][-10:-4]}.{output_file_type}")
    x += 1

x = 0
for i in video_list_201:
    print(video_list_201[x])
    os.system(f"ffmpeg -i {video_list_201[x]} -c:v libx264 -crf 20 -c:a aac -b:a 128k /Volumes/San_1/US_Soccer_Coaches_2023/Renders/201/render_{video_list_201[x][-10:-4]}.{output_file_type}")
    x += 1
