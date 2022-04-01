---
layout: projectpage
title: Cosmic KSP
---

# Cosmic KSP

## **[Git](https://github.com/Timin8er/KOS-Commander)**

![Image](https://cosmosc2.com/img/COSMOS.png)![Image](https://www.kerbalspaceprogram.com/wp-content/uploads/2019/08/mercury-logo-white-new.png)

### Overview
A project to command the video game **[Kerbal Space Program](https://www.kerbalspaceprogram.com/)** using real ground station software, **[Cosmos](https://cosmosc2.com/)**.

### Project Goals
- Send commands to KSP spacecraft from COSMOS
- Receive Telemetry from KSP in COSMOS
- Initialize a *simulation* instance of KSP and screen commands before sending them to the *real* instance
- Create a mission planning app for verifying commands in simulation prior to execution

## **Communication**
KPS does not support external commanding or telemetry out of the box. To address this I use two mods provided by the KSP fan community to enable this.

### [KOS](https://ksp-kos.github.io/KOS/)
The Kerbal Operating System, KOS, mod enables running scripts 'onboard' the spacecraft from either a built in terminal or remotely from a Telnet connection.
The ability to run scripts also enables more complicated automated behavior than what can be sent in a single command. Such as:
- automated abort conditions
- PID control loops
- repeatable maneuvers
- modular behaviors

### [Telemachus](https://github.com/TeleIO/Telemachus-1)
The Telemachus mod provides a easy to use telemetry stream from KSP to a standard computer socket.
The telemetry covers almost everything players would want to know about the state of the spacecraft. Including:
- Position, Rotation and Orbit parameters
- Resource levels
- environment status

## **Relays**
While the above mods add a lot of needed interfaces, they are not directly compatible with cosmos and need a translation layer.

On the Telemetry side, Cosmos accepts fixed width strings to decode into data while Telemachus sends json formatted text.
So a relay, written in Python, subscribes to the Telemachus stream, reformats the data into the format Cosmos needs, then sends in to a different socket for Cosmos to receive.

On the commanding side, we have the same formatting problem but also KOS can only be commanded via telnet. So the commanding relay subscribes to the socket for Cosmos commands, reformats the commands and sends them to KSP via telnet.

These two relays form the translation layer between Cosmos and KSP. They also include several injection points for testing and screening data flow.

## **Simulation**
An important function of any ground station is the screening and simulation functions, important for verification. In this case the simulation is just a second instance of KSP, set up to be initialized quickly from the state of the real instance.

This is done through save file manipulation. A quick-save file acts as a 'snapshot' of the game state and is copied onto the simulation game state reloaded be hijacking the KSP load file.

The simulation is commanded directly through the SMA or MPA.

## **Simulation Manager App**
The Simulation Manager App, SMA, is the app that manages the simulation state and can send commands to it. It can initialize the sim from the real, and send commands to the sim using the cosmos format.

The SMA is used during the real missions to screen commands prior to commanding the real spacecraft. This serves as a final check to make sure the command will function as expected.

#### Features:
- Manage the initialization of the *sim* from the *real* instance.
- Directly command the *sim* instance

## **Mission Planning App**
The Mission Planning App, MPA, is an app to construct sequences of commands and validate them using the simulation game instance. It does everything the SMA can do plus the function for creating mission commands.

#### Features:
- Construct a list of commands in order of execution
- Export the commands as a procedure document with instructions for the operator
- All SMA functions
