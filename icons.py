from PIL import Image
from PIL import ImageDraw

ci_size = 320


def cross(name, fg_color):
    ci_bg = '#000'
    ci_fg = fg_color
    ci_border = ci_size / 32
    ci_ih = ci_size - (2 * ci_border)
    ci_iw = ci_ih / 3
    ci_ip0 = ci_border
    ci_ip1 = ci_border + ci_iw
    ci_ip2 = ci_size - ci_border - 1
    ci_ip3 = ci_size - ci_border - ci_iw - 1

    rect_hor = [(ci_ip0, ci_ip1), (ci_ip2, ci_ip3)]
    rect_ver = [(ci_ip1, ci_ip0), (ci_ip3, ci_ip2)]

    ci = Image.new('RGB', (ci_size, ci_size), ci_bg)
    cid = ImageDraw.Draw(ci)
    cid.rectangle(rect_hor, outline=ci_fg, fill=ci_fg)
    cid.rectangle(rect_ver, outline=ci_fg, fill=ci_fg)
    ci.save(name + '.png')


def green_cross():
    cross('cross', '#0F0')


def ambar_cross():
    cross('ambar', '#F80')


def br_flag():
    br_size = ci_size
    br_outer = '#16B83E'
    br_middle = '#FFE11F'
    br_inner = '#1651B8'
    br_is = 2

    br = Image.new('RGB', (br_size, br_size), br_outer)
    brd = ImageDraw.Draw(br)

    brd.polygon([(0, br_size), (br_size, 0), (br_size, br_size)],
            outline=br_middle, fill=br_middle)

    brd.ellipse((br_size - br_size / br_is, br_size - br_size / br_is,
            br_size + br_size / br_is, br_size + br_size / br_is),
            outline=br_inner, fill=br_inner)

    br.save('br.png')


green_cross()
ambar_cross()
br_flag()
