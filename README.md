# movie-search

Movie Search allows you to search for any movie available on [OMDb API](http://www.omdbapi.com/). It lists available information, for example the plot or the film ratings from different reviewers.

# Setup

Before we handle with setting up the program, make sure you have [Pipenv](https://docs.pipenv.org/) installed. This allows us to create the `venv` required for the program to work.

Navigate to the correct directory and to create the `venv` and installed the dependencies execute this command:

`$ pipenv install --dev`

To start the shell execute:

`$ pipenv shell`

You can now run the program, however it will not work as you need an [API Key from OMDb](http://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0x0euvR%2FzVv1jLU3mGetH4R3kWtYKWACCaYcfoP1IY8g%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU5GG7XylwYou%2BzznFv7FbZmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulN6vYN8IikxxqwtGWTciOwQ4e4xie4N992dlfbpyqd1D&at=freeAcct&Email=). This free API Key allows for a daily limit of 1,000 requests.

Finally, to run the program, execute:

`$ python run.py --key [insert key here]`
