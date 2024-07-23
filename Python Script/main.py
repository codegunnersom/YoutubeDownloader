def ytd():
        # Python Implementation


    import subprocess
    from pytubefix import YouTube
    from pytubefix.cli import on_progress
    import re

    


    link = input("Enter Youtube Video link : ")

    try:
        link_str = str(link)
    except:
        TypeError 
        print("Invalid Link")        
    if "https://www.youtube.com" in link_str:
            print("valid Link")
            
    else:
            print("Please Enter a 'https://www.youtube.com' link.")
        


    # Prompt to choose the resolution


    yt = YouTube(link_str, on_progress_callback = on_progress)

    ####################################################################

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



    print("resolutions available :")
    for i in res_list:
        print(i)
        global res
    res = input("Please Enter Resolution : ")
    res = str(res)



    # Getting a list of All bit rates 

    yt = YouTube(link_str, on_progress_callback = on_progress)

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
        

    # Prompt to choose the Audio Bitrate

    print("resolutions available :")
    for i in bit_list:
        print(i)
        global bit
    bit = input("Please Enter Bitrate : ")
    bit = str(bit)

    



    from pytubefix import YouTube
    from pytubefix.cli import on_progress
    import re


    # Getting ITAG value for a specific chosen resolution

    fil_file_info = yt.streams.filter(resolution=res)
    fil_file_info_str = str(fil_file_info)

    with open('Video_itag.txt','w',encoding='utf-8') as file2:
        file2.write(fil_file_info_str)

    with open('Video_itag.txt','r',encoding='utf-8') as file2:
        content = file2.read()

    print(f"For Specified res {res} ")

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
        i = str(i)
        j = i.strip()
        j = str(j)
        k = int(j)
        i = int(i)
        itag_list.append(k)
        itag_list.remove(i)

    #################################################################


    #Getting the Exact Video Stream for the specified resolution using hte get_by_itag function
    #input the itag_list first element, itag_list contains the itag value for the streams of desired resolution
    high_Res_yt_video = yt.streams.get_by_itag(itag_list[0])

    #Downloading the Video using PyTubeFix Download Function, with specified outputpath and filename. 
    high_Res_yt_video.download(output_path='/Users/somendrasaini/Desktop/yt-dnldr/Python Script',filename='video.mp4')



        


    from pytubefix import YouTube
    from pytubefix.cli import on_progress
    import re



    # Getting ITAG value for a specific chosen bitrate

    bit_itag = yt.streams.filter(abr=bit)
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
    high_Res_yt_audio.download(output_path='/Users/somendrasaini/Desktop/yt-dnldr/Python Script',filename='audio', mp3=True)




    # Combining Video and saving using ffmpeg
    
    cmd = 'ffmpeg -y -i "audio.mp3"  -i "video.mp4" -filter:a aresample=async=1 -c:a flac -c:v copy output.mp4'
    subprocess.call(cmd, shell=True)
    print('Mixing Done')   


ytd()



