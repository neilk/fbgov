fbgov
=====

It is not easy to see the changes in Facebook's governance documents, so I made these 
cleaned-up documents, along with a visual "diff" to see the changes clearly.

Note that:

* This is not an official publication of Facebook. I have no association with Facebook other than
  being a user. This is my analysis of the documents, which I hope will be useful. I believe this falls
  under fair use, much as a journalist might analyze any other document released by Facebook.

* This is not authoritative. During my analysis I had to manipulate the files to get an easy to 
  understand comparison. Errors and omissions may have inadvertently occurred.

## The diffs! ##

The Statement of Rights and Responsibilities: http://htmlpreview.github.com/?https://github.com/neilk/fbgov/blob/master/srr-diff.html

The Data Use Policy: http://htmlpreview.github.com/?https://github.com/neilk/fbgov/blob/master/dup-diff.html

## Notes ##

These are based on the documents I downloaded from Facebook at about Mon Dec 3 23:47:41 2012 -0800.

The Data Use Policy documents are all in one document in the proposed version, and broken into
many pages in the existing version. So I combined all the existing version pages into one, for
an easier comparison.

To verify that I haven't altered the contents, or made mistakes when massaging these files into
easy-to-diff formats, you can peruse the git history of this project.

I started with the raw files and then cleaned them up with scripts in this project and
HTML Tidy (/usr/bin/tidy in Mac OS X, released 2006-10-31 build 15.6).

I am not intending or suggesting that you 'fork' Facebook's policies to your own liking. 
These are simply for the benefit of Facebook users who want an easier way to see the changes 
in those documents, and to have some degree of assurance that I'm not altering what Facebook's
documents say.

If Facebook makes further changes to their proposed policies, I will try to keep current but
pull requests would be most welcome.

I tried to see what it would look like if the new "proposed" documents were in their own branch, but 
the HTML diff on Github didn't give me good results. 

-- Neil K.
