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

  h1 {
    text-shadow: 0 0 4px #000;
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
    background-size: cover;
    background-position: 50% 50%;
    background-repeat: no-repeat;
    background-image: url(/content/images/jool.png);
  }

  #OFR {
    background-size: cover;
    background-position: 50% 42%;
    background-repeat: no-repeat;
    background-image: url(https://wallpapercave.com/wp/wp3396917.jpg);
    background-color: #fff;
    background-blend-mode: luminosity;
  }

  #VEX {
  }
</style>


<div class="container-flex">
  <div class="row align-items-center p-3" id="INTRO" >
    <div class="col-lg-3 offset-lg-1 d-flex justify-content-center justify-content-lg-end">
      <img src="/content/images/TTP.png" class="rounded w-75">
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
        <h1 class="display-3 pt-5"><a href="/cosmic_ksp">Cosmic KSP</a></h1>
        <h2 class="pb-5"><b>Commanding Kerbal Space Program with Cosmos</b></h2>
      </div>
    </div>
  </div>

  <!-- Open Feed Reader Project Card -->
  <div class="row text-center m-3">
    <div id="OFR" class="project_card col-md-10 offset-md-1">
      <div class="row p-2">
        <h1 class="display-3 pt-5"><a href="https://hub.docker.com/r/progradedv/open-feed-reader">Open Feed Reader</a></h1>
        <h2 class="pb-5" style="color: black; text-shadow: 0 0 2px #fff;"><b>An open source, self hosted, RSS Feed Website.</b></h2>
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
