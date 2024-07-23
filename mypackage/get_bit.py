# Prompt to choose the Audio Bitrate

import audio_code


def bit_fun():
      print("resolutions available :")
      for i in audio_code.audio_dnld.get_bit_list():
            print(i)
      global bit
      bit = input("Please Enter Bitrate")
      bit = str(bit)
      return bit