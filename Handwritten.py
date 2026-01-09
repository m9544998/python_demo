import pywhatkit as pw

txt=""" python is an interpreted high-level general-purpose programming language.
Its design philosophy  code readability with its use of significant indentation.
its help programer to make easy program soved all the problem of programer ."""



pw.text_to_handwriting(txt,"handwritten.png",[0,0,138])
print("end")
