



link_str = 'https://www.youtube.com/watch?v=CIf6VJH4dZk'

from pytubefix import YouTube
from pytubefix.cli import on_progress
import re

from mypackage import link_get
from mypackage import get_bit
from link_get import link_inp
from get_bit import bit_fun


def audio_dnld():
    ####################################################################


    # Getting a list of All resolution 

    yt = YouTube(link_get.link_inp(), on_progress_callback = on_progress)

    def get_bit_list():
        all_bit = yt.streams.filter(type="audio")
        all_bit_str = str(all_bit)


        with open('allbit.txt', 'w', encoding= 'utf-8') as file:
            file.write(all_bit_str)

        with open('allbit.txt','r', encoding = 'utf-8') as  file:
            content2 = file.read()

        matches = re.findall(r'abr="[^"]*"', content2)

 
        bit_var_list = []

        for i in matches:
            bit_var = re.findall(r'"([^"]*)"', i)
            for j in bit_var:
                bit_var_list.append(j)

        global bit_list     
        bit_list = []

        for i in bit_var_list:
            if i not in bit_list:
                bit_list.append(i)


        print("A list of all the bit rates available")
        return bit_list



    #################################################################


    # Getting ITAG value for a specific chosen resolution

    bit_itag = yt.streams.filter(abr=get_bit.bit_fun())
    bit_itag_str = str(bit_itag)

    with open('Bit_itag.txt','w',encoding='utf-8') as file2:
        file2.write(bit_itag_str)

    with open('Bit_itag.txt','r',encoding='utf-8') as file2:
        content = file2.read()



    matches_itag = re.findall(r'itag="[^"]*"', content)



    #################################################################


    #Getting a list of itag values for the specified Bitrate. 

 
    bit_itag_list = []

    for i in matches_itag:
        bit_itag = re.findall(r'"([^"]*)"', i)
        for j in bit_itag:
            bit_itag_list.append(j)
     
    global itag_list_bit
    itag_list_bit = []

    for i in bit_itag_list:
        if i not in itag_list_bit:
            itag_list_bit.append(i)


    print("Itag list for 128kbps")          
    print(itag_list_bit)



    #Converting Itag list from STR to INT

    for i in itag_list_bit :
        j = i.strip()
        j = str(j)
        k = int(j)
        itag_list_bit.append(k)
        itag_list_bit.remove(i)


    #################################################################


    high_Res_yt_audio = yt.streams.get_by_itag(itag_list_bit[0])
    high_Res_yt_audio.download(output_path='/Users/somendrasaini/Desktop/yt-dnldr',filename='audio', mp3=True)