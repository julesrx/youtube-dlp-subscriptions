# youtube-dlp-subscriptions

Downloads new videos from your YouTube subscription feeds since the last run.

## Requirements

This script requires either docker and docker compose or python3.

## Usage

First off, clone the repository and cd into it:

```console
git clone https://github.com/julesrx/youtube-dlp-subscriptions
cd youtube-dlp-subscriptions
```

Create a `subs.opml` file inside `downloads/` and populate it with your channels to download from. See `subs.sample.opml` for an example.  
See "[More on subs.opml](#more-on-subs.opml)" chapter below for more info.

### Docker-Compose

If you are familiar with what docker is, and what docker-compose is to docker, this is the recommended method to use.

Start the process: `docker-compose up`

### Manual

This method requires python3.

First, install the dependencies: `pip install -r app/requirements.txt`

Then, you can then run the script: `python3 dl.py`

## More on subs.opml

Start with this initial template:

```xml
<opml version="2.0">
  <body>
    <outline text="YouTube Subscriptions" title="YouTube Subscriptions">
      <outline title="ANYTHING" type="rss" xmlUrl="https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID" />
    </outline>
  </body>
</opml>
```

The ONLY factor that you must change is the string of `CHANNEL_ID`. the text ANYTHING is only for self-comments (and is useful for maintaining a long list 😉).

## SyncThing

Syncthing can be set up to sync from the downloads folder onto any other device (such as an android). Quite useful for long trips without cellular internet (or a data plan).

## Automation

A cron job can be set up to run the process at specified intervals. Be sure to cd into the directory first before running docker run from cron.

i.e: every day at 2AM, log stdout/stderr to log as well

```cron
0 2 * * * cd <path-to-script>/ && docker-compose up 2>&1 | tee log.txt
```

## Thanks

A thanks to mewfree and <https://github.com/mewfree/youtube-dl-subscriptions> for the original script and pukkandan for dlp.
