from tkinter import filedialog

import ffmpeg


def chose_file_webmovie():
    file_path = filedialog.askopenfilename(
        defaultextension=['webm'], filetypes=[('WebMovie', 'webm')]
    )
    return file_path


def save_file():
    file_name = filedialog.asksaveasfilename(
        defaultextension='mp4', filetypes=[('MP4 File', 'mp4')]
    )

    return file_name


def converte_file():
    """
    >>> converte_file()
    'ok'
    """
    file_web = chose_file_webmovie()
    video = ffmpeg.input(filename=file_web)
    video_out = video.output(save_file()).run()

    return 'ok'
