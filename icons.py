from PIL import Image
from PIL import ImageDraw

# green cross
ci_size = 160
ci_bg = '#000'
ci_fg = '#0F0'
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
ci.save('cross.png')


# br colors
br_size = ci_size
br_outer = '#16B83E'
br_middle = '#FFE11F'
br_inner = '#1651B8'
br_step = br_size / 16
br_mtl = 3 * br_step
br_mbr = br_size - 3 * br_step
br_itl = 5 * br_step
br_ibr = br_size - 5 * br_step

rect_middle = [(br_mtl, br_mtl), (br_mbr, br_mbr)]
rect_inner = [(br_itl, br_itl), (br_ibr, br_ibr)]

br = Image.new('RGB', (br_size, br_size), br_outer)
brd = ImageDraw.Draw(br)
brd.rectangle(rect_middle, outline=br_middle, fill=br_middle)
brd.rectangle(rect_inner, outline=br_inner, fill=br_inner)
br.save('br.png')
