Title: Kickstarter Experience
Date: 2017-09-02
Category: Blog
Tags: python, general
Slug: kickstarter


My first successful open source project was [pgcli](https://www.pgcli.com). It was launched more than
two years ago. It was very well-received at that time. It topped the charts on
Github, HackerNews and Reddit.

I received a few requests via twitter to add support for mysql database in
pgcli. Somehow this didn't seem right because I knew that pgcli wasn't quite up
to par with psql and I wasn't going to distract my focus by adding mysql
support to pgcli. So I kept postponing. Slowly a few core devs joined the pgcli
team and they were able to share a portion of development effort.

I started to think about mysql support. I wanted to keep it separate from pgcli
because I didn't think a unified db client would do justice to either of the
databases. I was also interested in learning how to do marketing for an
OpenSource project. So I decided that it might be fun to crowd-fund the
development of this new tool.

I picked Kickstarter because it was the most popular crowd-funding site. I
chose an arbitrary goal of $3000. The preparation to launch the kickstarter was
a lot of work.

## Preparation:

I knew I needed a video for the kickstarter campaign. I was too camera shy to
put my face on the video so I chose to do a screencast instead. I learned how
to use Camtasia and chose to use their 30 day trial to record a screencast. I'm
a big fan of [VimCasts](http://vimcasts.org), so I emailed Drew Neil (creator of VimCasts) and asked
for some tips. He gave me useful pointers and I realized that I could record
the screen and voice separately and then splice them together. This saved me so
much anxiety because I realized I can't narrate while I'm typing. After about a
week of multiple recordings and editing I had the final version which was
slightly under 2 mins. As I said, lot of work.

## Launch:

I decided to call this new tool mysql-cli. I bought the domain name and
redirected it to the kickstarter campaign. Writing copy for the kickstarter
campaign took another couple of days. After receiving some feedback from
friends it was ready for launch. I wrote a blog post about the kickstarter
campaign on the pgcli blog. Tweeted out the announcement and posted it to
Facebook.

During the first day of launch the campaign received more than $300. I was
thrilled by the fact that we reached 10% of the goal in just one day. Second
day was a bit slower but I figured it was just an off day. It kept getting
worse. I posted on Reddit and HackerNews but it went nowhere. I was very
confused. By the second week there were no pledges and the campaign was
hovering around $800. So I was going through a bit of emotional turmoil.

I had planned the kickstarter to coincide with PyCon. I gave a lightning talk
at PyCon about pgcli and plugged for the kickstarter. Zilch! No takers. People
were impressed by pgcli but no pledges for mycli. While at PyCon I was
approached by an Oracle employee who reminded me that the name "mysql" is
trademarked and I can't call my tool mysql-cli. I was frustrated but I didn't
want Oracle coming after my $900, so I decided to call the campaign "CLI for
MySql and MariaDB". 

During the flight from Montreal (Pycon) to Portland (home), I managed to get
the first implementation of the tool working. It was fairly straight-forward
since I had already done it once for pgcli. So now I had a mostly working clone
of pgcli. I reached out to the local MySQL group in Portland and showed the
half-working version. This was a successful presentation that earned another
$100 towards to the campaign. 

By the third week I was desperate, I tried advertising via google adwords and
twitters ads. I spent about $50 total, no conversions. By now I started sending
cold emails to companies that use MySQL. I sent an email to Youtube, Dropbox,
Percona etc. No replies. Then I googled for mysql consultants and found a few
OpenSource leaning consultants. When I emailed them, I received a few
'no' replies but then one person responded with a 'yes'. The campaign was
hovering around $1500 by now. This company offered to put forth $1500 which
would put me over the goal. I was ecstatic. This was TBS (Tech Blue Software)
Inc. They hadn't pledged yet since they were working out the details
internally.

I decided to push hard on the last week of the campaign, just in case they fell
through. When I posted on Google+ MySql community it took off. I received a lot
of pledged from there. Then someone posted it on Reddit and a lot of pgcli
users started pledging because they wanted to support pgcli and didn't know how
else to give money. I was humbled by the support. Three days before the end of
the campaign a ton of coworkers and friends from NewRelic started pledging and
they pushed the campaign over the goal. 

On the final day TBS pledge ($1500) came through and it put us well over the
goal. So in the end the campaign looked like it was a grand success. But
marketing for the campaign was constant work. I was glad it was over because
now I can go back to doing what I know well, coding.

I created a github org and invited all the backers. I gave them all access to
the early preview. I started delivering on my promises ahead of schedule and it
was mostly well-received. Since the launch I've received two donations via
paypal. One for $15 and another for $25. I've donated both contributions to
charities since I am gainfully employed and making a good salary.

## Conclusion:

Later I found out that the first week and the last week of Kickstarter
campaigns are the most active periods. So what I experienced was not out of
ordinary but it was still an emotional roller-coaster. It was a great
experience and I learned some valuable lessons in marketing. I wouldn't
recommend it as a way to fund ongoing development costs of a project. 

ps: The name mycli was recommended by an early backer. I don't remember the
name of the backer but I decided to use that name for my final launch.
