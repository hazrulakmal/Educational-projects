# Task 1. Streaming service user and playlist

---

## Background

In this task, we aim to make our previous implementation of the streaming service more realistic by including one important element - people subscribing / using the service (`User`), and include the class `FavouritePlaylist` so that we can now have a more realistic way to represent different playlists like "watch later" and "favourite".

---

## Description

1. We first change a little bit of the implementation of the `Playlist` from problem set 9. When we "play" a show, apart from printing out "Playing the show xxxx (yyyy)", it will also return the corresponding show (type: `Show`)
2. Create the class `FavouritePlaylist` for which it represents "favourite" playlists. It is very similar to the class `Playlist` above except that we do NOT remove the show once it is played. You need to be careful what it would do when you ask an instance of `FavouritePlaylist` to play a show several times without providing the name of the show. Should it just play the same show again and again?
3. Create the class `User` for which it represents users of an streaming service. Each instance of `User` has the instance attributes representing / storing the following:
  * birthday of the user
  * a container to store the history that the user has watched
  * a "watch later" playlist
  * a "favourite" playlist

  The class `User` has the methods to do the following:
  * Add a show to "watch later" playlist. Input: show (type: `Show`)
  * Remove a show from "watch later" playlist. Input: show name (type: `str`)
  * Play a show from "watch later" playlist. Input: show name (type: `str`). The show will add to "history" once it is played
  * Add a show to "favourite" playlist. Input: show (type: `Show`)
  * Remove a show from "favourite later" playlist. Input: show name (type: `str`)
  * Play a show from "favourite". Input: show name (type: `str`). The show will add to history once it is played. Note that if the show is also in "watch later", it should be removed from "watch later" as well (as it has already been watched!)
  * Get history: return all the history (can return a container or a generator)
  * Clear history: empty the container storing the history information
  * Get the age of the user: return the age of users (type: `int`). Age can be calculated as the difference between today and the birthday of the user

Note that for simplicity, we assume that user only can play shows from "watch later" or "favourite". You are welcome, however, to add more functionality to make it more realistic if you want to.

4. Please test `User` to make sure it is working

---

## Things to show in the report

* Testing result
* Show how `User` works by creating at least one instance and calling the methods

---

## Hint

You can use the module `datetime` to create an instance to store the birthday data, and get today's day. See [here](https://docs.python.org/3/library/datetime.html#examples-of-usage-date) to learn more.
