
from pytubefix import YouTube
from pytubefix.cli import on_progress
from mypackage import get_res
from get_res import res_fun
from mypackage import link_get
from link_get import link_inp
import re



def video_dnld():

    yt = YouTube(link_get.link_inp(), on_progress_callback = on_progress)

    ####################################################################

    def get_res_list():
            # Getting a list of All resolution 

        import re
        all_res = yt.streams
        all_res_str = str(all_res)


        with open('allres.txt', 'w', encoding= 'utf-8') as file:
            file.write(all_res_str)

        with open('allres.txt','r', encoding = 'utf-8') as  file:
            content2 = file.read()

        matches = re.findall(r'res="[^"]*"', content2)

        global res_list 
        res_var_list = []

        for i in matches:
            res_var = re.findall(r'"([^"]*)"', i)
            for j in res_var:
                res_var_list.append(j)
     
        res_list = []

        for i in res_var_list:
            if i not in res_list:
                res_list.append(i)

        return res_list






    #################################################################


    # Getting ITAG value for a specific chosen resolution

    fil_file_info = yt.streams.filter(resolution=get_res.res_fun())
    fil_file_info_str = str(fil_file_info)

    with open('Video_itag.txt','w',encoding='utf-8') as file2:
        file2.write(fil_file_info_str)

    with open('Video_itag.txt','r',encoding='utf-8') as file2:
        content = file2.read()

    print(f"For Specified res 1080p ")

    matches_itag = re.findall(r'itag="[^"]*"', content)



    #################################################################


    #Getting a list of itag values for the specified resolution. 

    global itag_list 
    res_itag_list = []

    for i in matches_itag:
        res_itag = re.findall(r'"([^"]*)"', i)
        for j in res_itag:
            res_itag_list.append(j)
     
    itag_list = []

    for i in res_itag_list:
        if i not in itag_list:
          itag_list.append(i)

    print(itag_list)



    #Converting Itag list from STR to INT

    for i in itag_list :
        j = i.strip()
        j = str(j)
        k = int(j)
        itag_list.append(k)
        itag_list.remove(i)


    #################################################################


    #Getting the Exact Video Stream for the specified resolution using hte get_by_itag function
    #input the itag_list first element, itag_list contains the itag value for the streams of desired resolution
    high_Res_yt_video = yt.streams.get_by_itag(itag_list[0])

    #Downloading the Video using PyTubeFix Download Function, with specified outputpath and filename. 
    high_Res_yt_video.download(output_path='/Users/somendrasaini/Desktop/yt-dnldr',filename='video.mp4')