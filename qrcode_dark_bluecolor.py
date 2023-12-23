import segno 
#'as' is used to make "alias" name
img = segno.make_qr("https://github.com/Mohil-Wankar")
img.save("Mohil_Wankar_Github_dark_blue.png",
         scale = 5,
         dark = "darkblue")

