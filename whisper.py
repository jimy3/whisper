import whisper
from whisper.utils import get_writer
import os.path

#1. 将要转档的档案放到process目录下,可以是多个档案
#2. 初始化设定, 初次预设为small, 若要效果最好可调整为large但执行速度会变慢
#   调整为large后，第一次执行下载模型会很久且文件很大(GB)
#   model type内字串可调整，执行速度为下所示：
#   tiny-->base-->small-->medium-->large

# set model type and load model
model_type = 'small'
model = whisper.load_model(model_type)

#load file(mp3, mp4) from folder
process_directory = './data'
all_file_name = os.listdir(process_directory)
a_list = ['bat','txt', 'srt'] #排除目录下不需要执行的文档

for file_name in all_file_name:
    try:
        if(os.path.splitext(file_name)[1] not in a_list):
            result = model.transcribe(process_directory+'/'+file_name)
            # produice txt and srt files with timeline
            txt_writer = get_writer('txt', process_directory)
            txt_writer(result, file_name)
            srt_writer = get_writer('srt', process_directory)
            srt_writer(result, file_name)
    except:
        pass