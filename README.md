# Django Tutorial

This repository contains my work through the following [online tutorial](https://www.youtube.com/watch?v=jBzwzrDvZ18&t=19745s&ab_channel=freeCodeCamp.org) with some additional work that I've done myself.

It contains some very basic apps which I list and explain below.

## MyApp
This app was conceived as a practice of the basic Django features, so it has a lot of unrelated functionality and might be a bit chaotic. The app allows user sign up, login and logout from the home page. There is a mock members table where anyone can add, delete or edit members. There will also be a true member list which only logged in user can see, with actual usernames.

## Blog

This a very simple blog where I can make posts as an admin. I also allow comments from anyone. The email field is optional. The comments need to be approved by an admin (not because I believe in censorship but because I wanted to try this feature).

## WeatherApp
In this app you can search a city a get information of the weather. At the moment is just an API and the city can be sent through a post request. In this request you can add `"temp_unit"` to be  `"C"`, `"F"` or `"K"` for Celsius, Fahrenheit and Kelvin temperature. You can also add `"wind_unit"` to be `"ms"`, `"kmh` or `"mh"` to display the wind speed in meter per second, kilometers per hour or miles per hour. There is some front-end done, but I wasn't satisfied with the ways in which I could allow the user to set the units, so it is not being used at the moment.
 
## RealtimeApp

