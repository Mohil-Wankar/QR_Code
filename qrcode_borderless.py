import segno
#'as' is used to make "alias" name
img = segno.make_qr("https://github.com/Mohil-Wankar")
img.save("Mohil_Wankar_Github_borderless.png",
         scale = 5,
         border = 0)
