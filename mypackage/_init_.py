# Define the __all__ variable
__all__ = ["video_code.py", "audio_code.py", "ffmpeg_proc.py","link_get.py","get_bit.py","get_res.py"]

# Import the submodules
from . import video_code
from . import audio_code
from . import ffmpeg_proc
from . import link_get
from . import get_bit
from . import get_res