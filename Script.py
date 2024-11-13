class ScrtipLearnImage:
    header = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title></title>
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />
        <link
          href="https://fonts.googleapis.com/css?family=Sawarabi+Mincho"
          rel="stylesheet"
        />
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />
        <link
          rel="shortcut icon"
          type="image/x-icon"
          href="../../Home/Images/japanese-alphabet.png"
        />
        <link rel="stylesheet" type="text/css" href="../Config/Style/style.css"/>
    </head>
    <body id="Background">
        <div class="container">
            <div class="homeButton">
                <button
                  class="homeBtn"
                  type="button"
                  onclick="location.href='../../index.html'"
                >
                  <i class="fa fa-home" style="color: white; font-size: 2vh"></i> Home
                </button>
            </div>"""

    bodyFlashcard = """
            <div class="card">
                <div class="imgBx">
                    <img src="Images/.png"/>
                </div>
                <div class="content">
                    <div>
                        <p class="japan"></p>
                    </div>
                    <div>
                        <p class="romaji">//</p>
                    </div>
                    <div>
                        <p class="mean"></p>
                    </div>
                </div>
            </div>"""

    bodyEnd = """
        </div>
        <div class="footer">
        <img src="https://hitwebcounter.com/counter/counter.php?page=11583648&style=0006&nbdigits=7&type=page&initCount=0"
            title="Counter Widget" Alt="Visit counter For Websites"/>
        </div>
        <script src="../Config/Script/script.js"></script>
    </body>
</html>
"""

    def __init__(self):
        pass

class ScriptKanji:
    header = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Link Swiper's CSS -->
        <link rel="stylesheet" href="../../Swiper/swiper-bundle.min.css" />
        <link href="https://fonts.googleapis.com/css?family=Sawarabi+Mincho" rel="stylesheet" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="shortcut icon" type="image/x-icon" href="../../Home/Images/japanese-alphabet.png" />
        <link rel="stylesheet" type="text/css" href="../CSS/style.css" />
        <link rel="stylesheet" type="text/css" href="../Config/CSS/style.css" />
    </head>

    <body id="Background">
        <div class="homeButton">
            <a href="../../index.html"><button class="homeBtn" type="button"><i class="fa fa-home	"
                        style="color:white;font-size: 2vh;"></i> Home</button></a>
        </div>
        <div class="container">
"""

    bodyNewWord = """
            <!-- //////////////////////////////////// START NEW WORD //////////////////////////////////// -->
            <div class="wordKanji">
                <div class="onKanjikun"> <!-- ////////// START KANJI ////////// -->
                    <div class="on">
                        おん
                    </div>
                    <div class="kanji">
                        <div class="flashcard">
                            <div class="question">
                                <div class="content japan">
                                    <img src="../../GIF/kanji/gif/150x150/.gif" class="border_all"/>
                                </div>
                            </div>
                            <div class="answer">
                                <div class="content vietnam">
                                    contentVietnam
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="kun">
                        くん
                    </div>
                </div> <!-- ////////// END KANJI ////////// -->
"""
    bodyStartOnKun ="""
                <div class="onkun"> <!-- ////////// START ON-KUN KANJI ////////// -->

                    <div class="onKanji"> <!-- ///// START ON ///// -->
"""
    bodyFlashCard = """
                        <div class="card"><!-- START WORD-->
                            <div class="imgBx">
                                <div>
                                    <p class="japan">1</p>
                                </div>
                            </div>
                            <div class="content2">
                                <div>
                                    <p class="japan">2</p>
                                </div>
                                <div>
                                    <p class="romaji"></p>
                                </div>
                            </div>
                        </div> <!-- END WORD-->
"""

    bodyEndOn = """
                    </div> <!-- ///// END ON ///// -->
"""

    bodySatrtKun = """
                    <div class="kunKanji"> <!-- ///// START KUN ///// -->
"""

    bodyEndOnKun = """
                    </div> <!-- ///// END KUN ///// -->

                </div> <!--  ////////// END ON-KUN KANJI ////////// -->
"""

    bodyNewWordEnd = """
            </div>
            <!-- //////////////////////////////////// END NEW WORD //////////////////////////////////// -->
"""
    bodyEnd = """
        </div>

        <div class="footer">
            <img src="https://hitwebcounter.com/counter/counter.php?page=11583648&style=0006&nbdigits=7&type=page&initCount=0"
                title="Counter Widget" Alt="Visit counter For Websites" />
        </div>
        <script src="../Config/Script/script.js"></script>
    </body>
</html>
"""
    def __init__(self):
        pass

class ScriptKanjiV2:
    header = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title></title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <!-- Link Swiper's CSS -->
        <link rel="stylesheet" href="../../Swiper/swiper-bundle.min.css" />
        <link
          href="https://fonts.googleapis.com/css?family=Sawarabi+Mincho"
          rel="stylesheet"
        />
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />
        <link
          rel="shortcut icon"
          type="image/x-icon"
          href="../../Home/Images/japanese-alphabet.png"
        />
        <link rel="stylesheet" type="text/css" href="../Config/Style/style.css" />
    </head>

    <body id="Background">
        <script src="../Config/Script/script.js"></script>
        <script src="../../Swiper/swiper-bundle.min.js"></script>

        <div>
          <a href="../../index.html"
            ><button class="homeBtn" type="button">
              <i class="fa fa-home" style="color: white; font-size: 2vh"></i> Home
            </button></a
          >
        </div>

        <div class="swiper mySwiper">
            <div class="swiper-wrapper">
"""
    bodySwipper1 = """
                <div class="swiper-slide slide">
                    <div class="japan">
                        <img src="../../GIF/kanji/gif/150x150/.gif" class="border_all" />
                    </div>
                    <div class="pop_up">
                        <button class="open_button slide" type="button">Help</button>
                    </div>
                </div>
"""

    bodySwipper2 = """
                <div class="swiper-slide slide">
                    <div class="japan">
                      <img
                        src="../../GIF/kanji/gif/150x150/1.gif"
                        class="border_topleft_bottomleft"
                      />
                      <img
                        src="../../GIF/kanji/gif/150x150/2.gif"
                        class="border_topright_bottomright"
                      />
                    </div>
                    <div class="pop_up">
                      <button class="open_button slide" type="button">Help</button>
                    </div>
                </div>
"""

    bodySwipper3 = """
                <div class="swiper-slide slide">
                    <div class="top_gif1 japan">
                      <img
                        src="../../GIF/kanji/gif/150x150/1.gif"
                        class="size_gif1 border_topleft_bottomleft"
                      />
                      <img src="../../GIF/kanji/gif/150x150/2.gif" class="size_gif1" />
                      <img
                        src="../../GIF/kanji/gif/150x150/3.gif"
                        class="size_gif1 border_topright_bottomright"
                      />
                    </div>
                    <div class="pop_up">
                      <button class="open_button slide" type="button">Help</button>
                    </div>
                </div>
"""
    bodyEnd = """
            </div>
            <div class="box">
                <p class="heading">Help</p>
                <div class="message_box">
                    <p class="message"></p>
                    <p class="mean"></p>
                    <div class="button_box">
                        <button class="close_button" type="button">OK</button>
                    </div>
                </div>
            </div>
    </div>
    <div class="footer">
        <img src="https://hitwebcounter.com/counter/counter.php?page=11583648&style=0006&nbdigits=7&type=page&initCount=0"
          title="Counter Widget" Alt="Visit counter For Websites" />
        </div>
    </body>
</html>
"""
    def __init__(self):
        pass