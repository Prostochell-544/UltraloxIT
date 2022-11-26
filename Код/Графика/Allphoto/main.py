from moviepy.editor import *
import os
from PIL import Image, ImageDraw, ImageFont


def creator(_text, _color_bg, _color_text, n):
    im = Image.new('RGB', (400, 400), color=('#FAACAC'))
    font = ImageFont.truetype('C:/Windows/Fonts/comic.ttf', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (50, 150),
        _text,
        font=font,
        fill='#1C0606')
    im.save('C:/Users/student/Documents/142/pythonProjectPhoto/' + str(n) + '.jpg')


text = ['Аллах смотри в сердца наши',
        'Кагда ты говоришь,\nслова должны быть твои \n лучше молчания',
        'Воистину аллах любит \nдоброту твоего сердцпа' ]
color_bg = ['#00B87D', '#CC00BB', '#0800CC', '#0099CC', '#CCC900', '#CC0000', '#0077CC', '#4B00CC', '#8B00CC',
            '#CC0088']
color_text = ['#000000']

for i in range(0, 2):
    creator(text[i], color_text[0], color_bg[i], i)

directory = 'C:/Users/student/Documents/142/pythonProjectPhoto'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set_duration(2) for m in images]

final_clip = concatenate_videoclips(clips, method='compose')
final_clip.write_videofile('LokheedMartin.mp4', fps=24)
