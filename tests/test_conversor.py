from pytest import mark

from converso_webm.conversor import chose_file_webmovie, save_file


def test_escolhe_um_arquivo_diferente_de_web():
    file_name = chose_file_webmovie()
    file_save = save_file()
    if '.webm' in file_name and '.mp4' in file_save:
        valida = True
    else:
        valida = False
    assert valida == True
