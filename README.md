# Projeto-Python

A command-line music management system developed as part of the **Fundamentals of Algorithms** course.

The project simulates the core functionality of a music streaming platform, allowing users to search for songs, manage playlists, rate tracks, and access their listening preferences through a text-based interface.

## Overview

The application, named **Spotifei**, was developed to practice fundamental programming concepts using Python.

The system provides user authentication, music search, playlist management, and interaction with songs through likes and dislikes. User data, playlists, and interaction history are persisted using plain text files (`.txt`), without relying on an external database.

The project focuses on applying programming fundamentals to a complete, interactive application rather than implementing a simple collection of isolated exercises.

## Features

### User Management

* User registration
* User login and authentication
* Password confirmation during registration
* User-specific data management

### Music Search

* Search for songs by title
* Display song information, including:

  * Title
  * Artist
  * Duration
  * Album
* Simulated music playback through the command line

### Song Interactions

Users can interact with songs through:

* Like
* Dislike
* Add to playlist

The system also maintains separate histories for liked and disliked songs.

### Playlist Management

Users can:

* Create playlists
* Add songs to playlists
* Remove songs from playlists
* Delete existing playlists
* View the songs contained in a playlist

### Data Persistence

The application stores information using plain text files, including:

* User accounts
* Music library
* Playlists
* Liked songs
* Disliked songs

This approach was intentionally used to practice file handling and persistent data management without introducing a database.

## Technologies

* **Python**
* File handling
* Functions
* Lists and dictionaries
* Conditional statements and loops
* String manipulation
* User input validation
* Basic authentication logic
* Persistent data storage using `.txt` files

## Project Structure

```text
Projeto-Python/
│
├── PROJETO.py      # Main application
├── MUSICAS.txt     # Music library
└── README.md       # Project documentation
```

The application generates and uses additional `.txt` files during execution to persist user accounts, playlists, and interaction histories.

## How It Works

The application starts with an initial menu where the user can either register, log in, or exit.

After authentication, the user is presented with the main menu:

```text
1 - Search
2 - Playlists
3 - History
0 - Exit
```

From there, the user can search the music catalog, interact with songs, manage playlists, or review their listening history.

The application uses the logged-in username to associate user-specific interactions with the corresponding data.

## Data Storage

Instead of using a relational or NoSQL database, the project uses plain text files as its persistence layer.

Music records follow a structured format containing information such as:

```text
Song,Artist,Duration,Album
```

User and interaction data are similarly stored as structured text records.

This implementation provides a simple way to demonstrate concepts such as:

* File I/O
* Data serialization
* Reading and writing persistent data
* Parsing structured text
* Managing application state

## Learning Objectives

The main objective of the project was to apply programming fundamentals to the development of a functional application.

Through this project, I practiced:

* Designing menu-driven applications
* Structuring a program using functions
* Managing collections of data
* Working with files and persistent storage
* Handling user input
* Implementing basic authentication
* Managing relationships between users, songs, playlists, and histories
* Developing application logic through conditional flows and loops

## Limitations

This project was designed as an academic exercise, so it intentionally uses a simple architecture.

Some of its current limitations include:

* Plain text files instead of a database
* Basic authentication without password encryption
* Command-line interface
* Local music data rather than an external music API
* Simulated playback instead of actual audio streaming

These limitations provide opportunities for future improvements and further development.

## Possible Improvements

Future versions of the project could include:

* Database integration using SQLite or PostgreSQL
* Password hashing and improved authentication
* A graphical or web-based interface
* Integration with a music API
* Actual audio playback
* More advanced search and filtering
* Playlist sharing
* Song recommendations based on user preferences
* Improved error handling and input validation
* Separation of the application into modules following a cleaner architecture

## Academic Context

This project was developed for the **Fundamentals of Algorithms** course as an exercise in applying programming concepts to a complete software system.

**Language:** Python
**Interface:** Command Line
**Storage:** Plain Text Files
**Project Type:** Academic Project

## Author

**Gabriel Pacioni Coelho**

[GitHub](https://github.com/Gabriel-p-coelho) · [Portfolio](https://portfoliogabrielpacioni.netlify.app/) · [LinkedIn](https://www.linkedin.com/in/gabriel-pacioni-coelho-b73168310)
