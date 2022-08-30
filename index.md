---
layout: page
---
<style>
  :root {
    --main-dark:#191919;
    --main-boarder:#121212;
  }

  a {
    color: #ffcc00;
  }

  .project_card {
    border-radius: 10px;
    border-style: solid;
    border-color: var(--main-boarder);
    border-width: 4px;
    background-color: var(--main-dark);
  }

  .profile_image {
    border-radius: 50px;
    border-style: solid;
    border-width: 4px;
    border-color: var(--main-boarder);
  }

  #INTRO {
    background-color: var(--main-dark);
    border-style: solid;
    border-width: 4px;
    border-color: var(--main-boarder);
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


<div class="container-flex">
  <div class="row align-items-center p-3" id="INTRO" >
    <div class="col-lg-3 offset-lg-1 d-flex justify-content-center justify-content-lg-end">
      <img src="/content/images/portfolioMain.jpg" class="rounded w-75 profile_image">
    </div>

    <div class="col-lg-4 text-center">
      <h1 class="display-1">Tim Polnow</h1>
      <h1 class="display-3">Software Engineer</h1>
    </div>
  </div>

  <!-- RSGS Project Card -->
  <div class="row text-center m-3">
    <div id="RSGS" class="project_card col-md-10 offset-md-1">
      <h1 class="display-3 pt-5"><a href="/rsgs">RSGS</a></h1>
      <h2 class="pb-5"><b>Robotic Servicing of Geosynchronous Satellites</b></h2>
    </div>
  </div>

  <!-- Cosmic KSP Project Card -->
  <div class="row text-center m-3">
    <div id="COSMIC" class="project_card col-md-10 offset-md-1">
      <div class="row p-2">

        <div class="col-lg-2 offset-1 d-none d-lg-flex align-items-center">
          <a href="https://ballaerospace.github.io/cosmos-website"><img class="figure-img img-fluid mx-auto" src="https://ballaerospace.github.io/cosmos-website/img/COSMOS.png"></a>
        </div>

        <div class="col-lg-6 text-center">
          <h1 class="display-3 pt-5"><a href="/cosmic_ksp">COSMIC KSP</a></h1>
          <h2 class="pb-5"><b>Commanding KSP with COSMOS</b></h2>
        </div>

        <div class="col-lg-2 d-none d-lg-flex align-items-center">
          <!-- <a href="https://www.kerbalspaceprogram.com/"><img class="figure-img img-fluid mx-auto" src="https://www.kerbalspaceprogram.com/wp-content/uploads/2019/08/mercury-logo-white-new.png"></a> -->
          <a href="https://www.kerbalspaceprogram.com/"><img class="figure-img img-fluid mx-auto" src="/content/images/KSP.png"></a>
        </div>

        <div class="col-lg-6 d-flex d-lg-none">
          <div class="row p-2">

            <div class="col d-flex align-items-center">
              <img class="figure-img img-fluid mx-auto w-75" src="https://cosmosc2.com/img/COSMOS.png">
            </div>

            <div class="col d-flex align-items-center ">
              <!-- <img class="figure-img img-fluid mx-auto h-75" src="https://www.kerbalspaceprogram.com/wp-content/uploads/2019/08/mercury-logo-white-new.png"> -->
              <img class="figure-img img-fluid mx-auto h-75" src="/content/images/KSP.png">
            </div>

          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- Blackjack Bot Project Card -->
  <div class="row text-center m-3">
    <div class="project_card col-md-10 offset-md-1">
      <div class="row p-2">

        <div id="CARDSTRIP" class="col-2 offset-1 d-none d-md-flex align-items-center">
        </div>

        <div class="col-md-6 text-center">
          <!-- <h1 class="display-3 pt-5"><a href="https://rebrand.ly/r1ckr0l13r">Blackjack Bot</a></h1> -->
          <h1 class="display-3 pt-5">Blackjack Bot</h1>
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
    <div id="VEX" class="project_card col-md-10 offset-md-1 h-100">
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

</div>
