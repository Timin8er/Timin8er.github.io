---
layout: projectpage
title: Cosmic KSP
---

# **Cosmic KSP**

## **[View on GitHub](https://github.com/Timin8er/CosmicKSP)**

<div class="row p-1 my-3" style="border-radius: 10px; border-style: solid; border-color: #121212; border-width: 4px; background-color: #191919;">

  <div class="col d-flex align-items-center">
    <img class="figure-img img-fluid mx-auto w-75" src="https://ballaerospace.github.io/cosmos-website/img/COSMOS.png">
  </div>

  <div class="col d-flex align-items-center ">
    <!-- <img class="figure-img img-fluid mx-auto h-75" src="https://www.kerbalspaceprogram.com/wp-content/uploads/2019/08/mercury-logo-white-new.png"> -->
    <img class="figure-img img-fluid mx-auto h-75" src="/content/images/KSP.png">
  </div>

</div>

## **Overview**
A project to command the video game **[Kerbal Space Program](https://www.kerbalspaceprogram.com/)** using real ground station software, **[Cosmos](https://cosmosc2.com/)**.

### Project Goals
- Send commands to KSP spacecraft from COSMOS
- Receive Telemetry from KSP in COSMOS
- Initialize a *simulation* instance of KSP and screen commands before sending them to the *real* instance
- Create a simulation manager app for verifying commands in simulation prior to execution

<div class="row p-1 my-3" style="border-radius: 10px; border-style: solid; border-color: #121212; border-width: 4px; background-color: #191919;">
  <div class="col d-flex align-items-center">
    <img class="figure-img img-fluid mx-auto w-90" src="/content/images/CosmicKspDataFlow.png">
  </div>
</div>

___

## **Game Instance Communication**
KPS does not support external commanding or telemetry out of the box. To add this I use two mods provided by the KSP fan community.

### **KOS**
The [Kerbal Operating System](https://ksp-kos.github.io/KOS/), KOS, mod enables running scripts "onboard" the spacecraft from either a built in terminal or remotely from a Telnet connection.
The ability to run onboard scripts also enables more complicated automated behavior than what can be sent in a single command. Such as:
- Automated abort conditions
- PID control loops
- Precise maneuvers
- Behaviors trees

### **Telemachus**
The [Telemachus](https://github.com/TeleIO/Telemachus-1) mod provides a telemetry stream from KSP to a standard computer socket.
The telemetry covers almost everything players would want to know about the state of the spacecraft. Including:
- Position, Rotation and Orbit parameters
- Resource levels
- Environment status

## **Translation Relay**
While the above mods add a lot of needed interfaces, they are not directly compatible with COSMOS and need a translation layer.

On the Telemetry side, COSMOS accepts fixed width byte strings while Telemachus sends json formatted text.
So a relay, written in Python, subscribes to the Telemachus stream, reformats the data into the format COSMOS needs, then sends it to a different socket for COSMOS to receive.

On the commanding side, we have the same formatting problem but KOS can only be commanded via telnet. So the commanding relay subscribes to the socket for COSMOS commands, reformats the commands and sends them to KSP via telnet.

These two relay threads form the translation layer between COSMOS and KSP. They also include several injection points for testing and screening data flow.

## **COSMOS**
[COSMOS](https://cosmosc2.com/) by Ball Aerospace is a command and control system providing commanding, scripting, and data visualization capabilities for embedded systems. COSMOS is intended for use during all phases of testing and during operations.
COSMOS 5 is a cloud native build and comes in the form of a docker container. For this reason, COSMOS is actually running on a separate server machine I own, and is interfaced with over a browser.

___

## **Wrokflow and Instance Configurations**
<div class="row p-1 my-3" style="border-radius: 10px; border-style: solid; border-color: #121212; border-width: 4px; background-color: #191919;">
  <div class="col d-flex align-items-center">
    <img class="figure-img img-fluid mx-auto w-90" src="/content/images/realSimflow.png">
  </div>
</div>
In order to emulate real workflow and command center procedures, KSP can be launched under two different configurations: Simulation, and Real. COSMOS can switch between them as two different targets. These Targets can be used together to emulate a commanding, screening, or planning workflow.

### **The Real Instance**
This instance of KSP represents the reality of the spacecraft. It is interacted with as if there are no do overs.

### **The Simulation Instance**
This instance of KSP represents a simulation of reality. It has extra abilities to copy the game state from the real instance and is used to plan operations, or screen commands prior to execution on the real instance. This serves as a final check to make sure the command will function as expected.

## **Simulation Manager App**
The Simulation Manager App, **SMA**, is the application that manages the simulation state. It can initialize the sim from the real KSP state without closing either game.
Initialization is done through save file manipulation. A quick-save file acts as a snapshot of the real KSP, is copied onto the simulation KSP, and reloaded.
