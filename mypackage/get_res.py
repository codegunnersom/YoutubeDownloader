# Prompt to choose the resolution
import video_code

def res_fun():
      print("resolutions available :")
      for i in video_code.video_dnld.get_res_list():
            print(i)
      global res
      res = input("Please Enter Resolution")
      res = str(res)
      return res