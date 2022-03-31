<!doctype html>
---
layout: projectpage
---
<html lang="en">
  <head>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  </head>

  <style>
    .project_card {
      border-radius: 10px;
      border-style: solid;
      border-width: 8px;
    }

    .profile_image {
      border-radius: 50px;
      border-style: solid;
      border-width: 4px;
    }

    #INTRO {
      border-style: solid;
      border-width: 8px;
    }

    #RSGS {
      background-size: cover;
      background-position: 50% 42%;
      background-repeat: no-repeat;
      background-image: url(https://images.unsplash.com/photo-1451187580459-43490279c0fa);
    }

    #COSMIC {
    }

    #CARDSTRIP {
      background-repeat: no-repeat;
      background-position: 22% 100%;
      background-attachment: fixed;
      background-image: url(/content/images/cardStrip.png); */
    }

    #VEX {
    }
  </style>

  <body>
    <div id="header">
      <nav>
        <ul>
          <li class="fork"><a href="www.timin8er.com">Tim Polnow</a></li>
        </ul>
      </nav>
    </div><!-- end header -->

    <div class="container-flex">
      <div class="row align-items-center p-3" id="INTRO" >
        <div class="col-lg-3 offset-lg-1 d-flex justify-content-center justify-content-lg-end">
          <img src="https://drive.google.com/uc?export=download&id=1wASzez30pO4nMcvge6kvWWpmi8FrAgqH" class="figure-img img-fluid rounded w-75 profile_image">
          <!-- <img src="/content/images/portfolioMain.jpg" class="figure-img img-fluid rounded profile_image"> -->
        </div>

        <div class="col-lg-4 text-center">
          <h1 class="display-1">Tim Polnow</h1>
          <h1 class="display-3">Software Engineer</h1>

          <div class="row">
            <div class="col-sm-2 offset-sm-4">
              <h1 class="display-5"><a type="button" class="btn btn-outline-primary p-2" href="/content/Resume_2022_03_28.pdf">Resume</a></h1>
            </div>
            <div class="col-sm-2">
              <h1 class="display-5"><a type="button" class="btn btn-outline-primary p-2" href="mailto: jobhunt@timin8er.com">Contact</a></h1>
            </div>
          </div>
        </div>
      </div>

      <!-- RSGS Project Card -->
      <div class="row text-center m-3">
        <div id="RSGS" class="project_card col-10 offset-1 p-2">
          <h1 class="display-3 pt-5"><a href="https://rebrand.ly/r1ckr0l13r">RSGS</a></h1>
          <h2 class="pb-5"><b>Robotic Servicing of Geosynchronous Satellites</b></h1>
        </div>
      </div>

      <!-- Cosmic KSP Project Card -->
      <div class="row text-center m-3">
        <div id="COSMIC" class="project_card col-10 offset-1">
          <div class="row p-2">

            <div class="col-lg-2 offset-1 d-none d-lg-flex align-items-center">
              <img class="figure-img img-fluid mx-auto" src="https://cosmosc2.com/img/COSMOS.png">
            </div>

            <div class="col-lg-6 text-center">
              <h1 class="display-3 pt-5"><a href="https://rebrand.ly/r1ckr0l13r">COSMIC KSP</a></h1>
              <h2 class="pb-5"><b>Commanding KSP with COSMOS</b></h2>
            </div>

            <div class="col-lg-2 d-none d-lg-flex align-items-center">
              <img class="figure-img img-fluid mx-auto" src="https://www.kerbalspaceprogram.com/wp-content/uploads/2019/08/mercury-logo-white-new.png">
            </div>

            <div class="col-lg-6 d-flex d-lg-none">
              <div class="row p-2">

                <div class="col d-flex align-items-center">
                  <img class="figure-img img-fluid mx-auto w-75" src="https://cosmosc2.com/img/COSMOS.png">
                </div>

                <div class="col d-flex align-items-center ">
                  <img class="figure-img img-fluid mx-auto h-75" src="https://www.kerbalspaceprogram.com/wp-content/uploads/2019/08/mercury-logo-white-new.png">
                </div>

              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- Blackjack Bot Project Card -->
      <div class="row text-center m-3">
        <div class="project_card col-10 offset-1">
          <div class="row p-2">

            <div id="CARDSTRIP" class="col-2 offset-1 d-none d-md-flex align-items-center">
            </div>

            <div class="col-md-6 text-center">
              <h1 class="display-3 pt-5"><a href="https://rebrand.ly/r1ckr0l13r">Blackjack Bot</a></h1>
              <h2 class="pb-5"><b>Neural Networks Playing Blackjack.</b></h2>
            </div>
            <!-- <div class="col-2 d-flex align-items-center">
              <img class="figure-img img-fluid mx-auto" src="/content/images/blackjackBotScreenshot_abridged.PNG" alt="Sim Abridged">
            </div> -->
          </div>
        </div>
      </div>

      <!-- VEX Project Card -->
      <div class="row text-center m-3">
        <div id="VEX" class="project_card col-10 offset-1 h-100">
          <div class="row p-2">

            <div class="col-lg-2 offset-lg-1 d-flex align-items-center">
              <img class="figure-img img-fluid mx-auto w-75" src="/content/images/Vex-Logo.jpg" alt="Logo">
            </div>

            <div class="col-lg-6 text-center">
              <h1 class="display-3 pt-5">Vex Robotics Team</h1>
              <h2 class="pb-5"><b>Old Dominion University</b></h2>
            </div>

            <div class="col-lg-2 d-none d-lg-flex align-items-center">
              <img class="figure-img img-fluid mx-auto" src="/content/images/vex_group_shot_greyscale.jpg" alt="Sim Abridged">
            </div>

          </div>
        </div>
      </div>


      <!-- Footer -->
      <div class="row align-items-center p-3" id="INTRO" >
        <div class="col-md-2 offset-sm-4 text-center">
          <h1 class="display-5"><a type="button" class="btn btn-outline-primary p-2" href="/content/Resume_2022_03_28.pdf">Resume</a></h1>
        </div>

        <div class="col-md-2 text-center">
          <h1 class="display-5"><a type="button" class="btn btn-outline-primary p-2" href="mailto: jobhunt@timin8er.com">Contact</a></h1>
        </div>

      </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
</html>