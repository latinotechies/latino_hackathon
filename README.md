# latino_hackathon
Code from the Latino Hackathon on International Open Data Day (21-02-2015)

We worked to identify foreclosed single-family houses in Cook County that have been bought by [Invitation Homes](http://invitationhomes.com/), a subsidiary of the global private equity firm [Blackstone](http://www.blackstone.com/).

We can find the properties via the [Cook County Recorder of Deeds website](http://12.218.239.82/i2/default.aspx?AspxAutoDetectCookieSupport=1), albeit through a clumsily manual process. [This document describes the manual process involved](https://docs.google.com/document/d/1BL_egyUkr5G6GBLSj7K78OaEecZK7Lc_eyXjmVOOCtc/pub).

Trying to improve upon this manual process, I worked on scraping from this site. It's an ASP.NET site apparently created by a Xerox contract in 2010 for the [Cook County Recorder of Deeds](http://12.218.239.82/i2/default.aspx?AspxAutoDetectCookieSupport=1), and this type of site is notoriously difficult to scrape.

I'm using the web browser automation library [selenium](http://docs.seleniumhq.org/) with the headless browser PhantomJS to create a new session ID. I'm then simulating the POST requests of the real website using the Python library [requests](http://docs.python-requests.org/en/latest/), based on monitoring the actual POST requests using the Developer Tools in Google Chrome. I'm using cookies also pulled from an actual session in Google Chrome.
