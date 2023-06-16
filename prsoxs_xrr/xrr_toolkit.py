import numpy as np
from uncertainties import unumpy, ufloat
from pathlib import Path
from tkinter import filedialog
from tkinter import *


# c = 299_792_458 * 10**10  # \AA s-2
# ħ = 6.582_119_569 * 10 ** (-16)  # eV s
hc = 12400  # ev \AA


class DotDic(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__  # type: ignore
    __delattr__ = dict.__delitem__  # type: ignore


def file_dialog() -> Path:
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    root.lift()
    root.focus_force()
    directory = Path(filedialog.askdirectory())
    return directory


def save_dialog() -> Path:
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    root.lift()
    root.focus_force()
    file_save_path = Path(filedialog.asksaveasfilename())
    return file_save_path if file_save_path else None  # type: ignore


def open_dialog() -> Path:
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    root.lift()
    root.focus_force()
    file_save_path = Path(filedialog.askopenfilename())
    return file_save_path if file_save_path else None  # type: ignore


def scattering_vector(energy, theta):
    global hc
    k = 2 * np.pi * energy / (hc)
    Q = 2 * k * np.sin(np.radians(theta))
    return Q


@np.vectorize
def is_valid_index(arr, index):
    if len(arr) == 0:
        return True
    i, j = index
    if i < 0 or i >= arr.shape[0]:
        return False
    if j < 0 or j >= arr.shape[1]:
        return False
    return True


def uaverage(uarray, axis=None, *arge, **kwargs):
    _w = 1 / (unumpy.std_devs(uarray) ** 2)
    return np.average(unumpy.nominal_values(uarray), axis=axis, weights=_w)


if __name__ == "__main__":
    A = {"A": 10, "B": 20}
    B = DotDic(A)
    print(A)
    print(B.A)
